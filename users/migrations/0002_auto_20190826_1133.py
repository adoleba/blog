# Generated by Django 2.2.4 on 2019-08-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_user',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='intro_user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]