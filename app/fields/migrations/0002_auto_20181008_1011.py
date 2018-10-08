# Generated by Django 2.1.2 on 2018-10-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]