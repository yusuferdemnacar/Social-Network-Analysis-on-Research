# Generated by Django 4.1.3 on 2022-11-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.TextField(null=True),
        ),
    ]
