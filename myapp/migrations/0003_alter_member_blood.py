# Generated by Django 5.1.3 on 2024-11-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_member_blood_member_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='blood',
            field=models.CharField(max_length=2, null=True),
        ),
    ]