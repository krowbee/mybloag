# Generated by Django 4.2.4 on 2023-09-10 20:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_post_post_text"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="post_text",
            new_name="text",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="post_title",
            new_name="title",
        ),
    ]