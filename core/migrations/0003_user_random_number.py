# Generated by Django 2.2.1 on 2019-05-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='random_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]