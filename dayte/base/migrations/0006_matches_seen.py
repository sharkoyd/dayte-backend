# Generated by Django 4.2.5 on 2023-10-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_matches_disliked_alter_profile_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
