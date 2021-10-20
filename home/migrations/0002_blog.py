# Generated by Django 3.1.5 on 2021-10-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True)),
                ('author', models.CharField(blank=True, max_length=1000)),
                ('tags', models.CharField(blank=True, max_length=1000)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='blog/images')),
                ('time', models.DateTimeField(blank=True)),
                ('readtime', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
