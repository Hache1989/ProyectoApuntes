# Generated by Django 2.0.7 on 2018-07-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180717_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_img_url',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
