# Generated by Django 4.0.1 on 2022-02-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='thumbnailUrl',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images/review'),
        ),
    ]