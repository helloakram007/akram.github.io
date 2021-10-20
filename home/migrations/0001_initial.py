# Generated by Django 3.1.5 on 2021-10-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
