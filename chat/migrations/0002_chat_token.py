# Generated by Django 4.2 on 2024-12-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="token",
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]
