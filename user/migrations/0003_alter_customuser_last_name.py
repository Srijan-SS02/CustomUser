# Generated by Django 4.1.4 on 2023-05-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_customuser_username_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(default="", max_length=200),
        ),
    ]