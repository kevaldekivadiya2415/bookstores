# Generated by Django 4.0.1 on 2022-02-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_remove_book_thumbnailurl_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/review'),
        ),
    ]
