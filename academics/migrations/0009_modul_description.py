# Generated by Django 2.0.7 on 2018-07-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0008_auto_20180721_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
