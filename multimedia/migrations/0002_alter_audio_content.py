# Generated by Django 3.2.2 on 2021-05-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='content',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
