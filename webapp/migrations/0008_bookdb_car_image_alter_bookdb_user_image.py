# Generated by Django 5.0.6 on 2024-06-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_rename_user_image_bookdb_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdb',
            name='Car_image',
            field=models.ImageField(blank=True, null=True, upload_to='Booking Images'),
        ),
        migrations.AlterField(
            model_name='bookdb',
            name='User_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Booking Images'),
        ),
    ]
