# Generated by Django 4.2.4 on 2023-09-07 17:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_posts_post_text_alter_posts_post_title"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Posts",
            new_name="Post",
        ),
    ]
