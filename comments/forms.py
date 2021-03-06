from django import forms

from comments.models import PostComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('author_name', 'email', 'body')
