# Generated by Django 5.1.3 on 2024-11-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='blood',
            field=models.CharField(choices=[('b', 'B'), ('a', 'A'), ('o', 'O')], default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='language',
            field=models.CharField(choices=[('a', 'A+'), ('c', 'c#'), ('d', 'Dart'), ('f', 'Flutter'), ('n', 'Nodejs'), ('n', 'Networking'), ('p', 'Python')], default=None, max_length=20),
        ),
    ]