# Generated by Django 3.2.9 on 2021-11-19 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_pk',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_pk',
            new_name='comment_user',
        ),
    ]
