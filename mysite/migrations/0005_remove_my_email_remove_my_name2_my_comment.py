# Generated by Django 4.0.5 on 2022-06-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_my_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my',
            name='email',
        ),
        migrations.RemoveField(
            model_name='my',
            name='name2',
        ),
        migrations.AddField(
            model_name='my',
            name='comment',
            field=models.TextField(default=1, max_length=700),
            preserve_default=False,
        ),
    ]
