# Generated by Django 3.1.5 on 2021-10-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, upload_to='files')),
            ],
        ),
    ]
