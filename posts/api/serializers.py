from rest_framework.fields import SerializerMethodField, CurrentUserDefault, HiddenField
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField, SlugRelatedField, \
    HyperlinkedRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from categories.models import Category
from comments.models import PostComment
from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    comments_count = SerializerMethodField()
    author = SerializerMethodField()
    category = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Post
        fields = ['url', 'title', 'category', 'author', 'status', 'published', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        return obj.category.name


class PostDetailSerializer(ModelSerializer):
    category = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='categories-api:detail',
        lookup_field='slug'
    )

    main_photo = SerializerMethodField()
    thumbnail_photo = SerializerMethodField()
    author = SerializerMethodField()
    comments = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='body'
     )

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'sub_title',
            'slug',
            'category',
            'created',
            'published',
            'status',
            'main_photo',
            'thumbnail_photo',
            'intro',
            'body',
            'comments',
        ]

    def get_main_photo(self, obj):
        try:
            main_photo = obj.main_photo.url
        except:
            main_photo = None
        return main_photo

    def get_thumbnail_photo(self, obj):
        try:
            thumbnain_photo = obj.thumbnail_photo.url
        except:
            thumbnain_photo = None
        return thumbnain_photo

    def get_comments(self, obj):
        obj_id = obj.id
        return PostComment.objects.filter(post_id=obj_id)

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        print(obj.name)
        category_name = obj.name
        return Post.objects.filter(category__name=category_name)


class PostCreateUpdateDestroySerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'sub_title',
            'slug',
            'category',
            'created',
            'published',
            'status',
            'main_photo',
            'thumbnail_photo',
            'intro',
            'body',
        ]

    def create(self, validated_data):
        title = validated_data.get('title')
        author = validated_data.get('author')
        sub_title = validated_data.get('sub_title')
        slug = validated_data.get('slug')
        categories = validated_data.get('category')
        created = validated_data.get('created')
        published = validated_data.get('published')
        status = validated_data.get('status')
        main_photo = validated_data.get('main_photo')
        thumbnail_photo = validated_data.get('thumbnail_photo')
        intro = validated_data.get('intro')
        body = validated_data.get('body')

        categories = Category.objects.filter(name__in=categories)

        post = Post.objects.create(title=title, sub_title=sub_title, slug=slug, created=created, published=published,
                                   status=status, main_photo=main_photo, thumbnail_photo=thumbnail_photo, intro=intro,
                                   body=body, author=author)

        post.category.set(categories)

        return post
