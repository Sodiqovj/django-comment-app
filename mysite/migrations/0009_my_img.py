# Generated by Django 4.0.5 on 2022-06-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_down'),
    ]

    operations = [
        migrations.AddField(
            model_name='my',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
