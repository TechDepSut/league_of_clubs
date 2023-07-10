# Generated by Django 4.2.2 on 2023-06-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("election", "0002_club_votes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="choice",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="election.club",
            ),
        ),
    ]
