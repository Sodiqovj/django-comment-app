# Generated by Django 4.0.5 on 2022-06-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_remove_my_email_remove_my_name2_my_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
