# Generated by Django 3.0 on 2021-07-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(1, 'Guest'), (2, 'Manager'), (3, 'User')], default=1, max_length=10),
        ),
    ]
