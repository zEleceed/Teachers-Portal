# Generated by Django 5.0.3 on 2024-03-29 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
