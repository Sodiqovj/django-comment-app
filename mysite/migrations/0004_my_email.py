# Generated by Django 4.0.5 on 2022-06-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_remove_my_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='my',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
