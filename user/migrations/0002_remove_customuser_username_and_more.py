# Generated by Django 4.1.4 on 2023-05-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(default="", max_length=200),
        ),
    ]
