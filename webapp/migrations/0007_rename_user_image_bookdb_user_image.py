# Generated by Django 5.0.6 on 2024-06-15 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_bookdb_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdb',
            old_name='User_image',
            new_name='User_Image',
        ),
    ]
