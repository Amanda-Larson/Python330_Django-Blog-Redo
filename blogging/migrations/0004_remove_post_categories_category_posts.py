# Generated by Django 4.1 on 2022-09-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0003_alter_category_options_remove_category_posts_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="categories",),
        migrations.AddField(
            model_name="category",
            name="posts",
            field=models.ManyToManyField(
                blank=True, related_name="categories", to="blogging.post"
            ),
        ),
    ]