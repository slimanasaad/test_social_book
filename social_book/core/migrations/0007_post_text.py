# Generated by Django 5.0.2 on 2024-03-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
