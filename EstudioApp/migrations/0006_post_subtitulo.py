# Generated by Django 4.0.4 on 2022-05-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EstudioApp', '0005_remove_comment_post_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]