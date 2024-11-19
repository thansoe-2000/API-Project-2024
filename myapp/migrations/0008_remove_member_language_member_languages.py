# Generated by Django 5.1.3 on 2024-11-12 17:24

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_member_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='language',
        ),
        migrations.AddField(
            model_name='member',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'A+'), ('c', 'c#'), ('d', 'Dart'), ('f', 'Flutter'), ('n', 'Nodejs'), ('n', 'Networking'), ('p', 'Python')], max_length=13, null=True),
        ),
    ]
