# Generated by Django 4.2.2 on 2023-06-15 17:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_notice_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
