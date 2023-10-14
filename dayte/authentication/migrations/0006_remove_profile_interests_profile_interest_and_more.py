# Generated by Django 4.2.5 on 2023-09-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_profile_finished_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.CharField(blank=True, choices=[('Travelling', 'Travelling'), ('Music', 'Music'), ('Sports', 'Sports'), ('Reading', 'Reading'), ('Movies', 'Movies'), ('Cooking', 'Cooking'), ('Gaming', 'Gaming'), ('Photography', 'Photography'), ('Dancing', 'Dancing'), ('Painting', 'Painting'), ('Gardening', 'Gardening'), ('Writing', 'Writing'), ('Fishing', 'Fishing'), ('Shopping', 'Shopping'), ('Hiking', 'Hiking'), ('Camping', 'Camping'), ('Running', 'Running'), ('Swimming', 'Swimming'), ('Cycling', 'Cycling'), ('Yoga', 'Yoga'), ('Meditation', 'Meditation'), ('Singing', 'Singing'), ('Acting', 'Acting'), ('Learning', 'Learning'), ('Volunteering', 'Volunteering'), ('Socializing', 'Socializing'), ('Eating', 'Eating'), ('Drinking', 'Drinking'), ('Sleeping', 'Sleeping'), ('Partying', 'Partying'), ('Clubbing', 'Clubbing'), ('Gambling', 'Gambling'), ('Working', 'Working'), ('Studying', 'Studying')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='finished',
            field=models.BooleanField(choices=[(False, 'Incomplete'), (True, 'Complete')], default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='plan',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('basic', 'Basic'), ('premium', 'Premium')], max_length=20, null=True),
        ),
    ]
