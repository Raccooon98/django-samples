# Generated by Django 4.2 on 2023-04-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="img",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
