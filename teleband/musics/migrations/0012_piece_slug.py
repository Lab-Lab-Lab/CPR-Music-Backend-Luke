# Generated by Django 3.2.11 on 2022-01-30 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musics", "0011_seed_piece_parts_parttranspositions"),
    ]

    operations = [
        migrations.AddField(
            model_name="piece",
            name="slug",
            field=models.SlugField(null=True),
        ),
    ]
