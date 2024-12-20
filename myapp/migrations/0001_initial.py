# Generated by Django 5.1.3 on 2024-11-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('fe', 'Female')], default=None, max_length=6)),
                ('birth_date', models.DateField()),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
