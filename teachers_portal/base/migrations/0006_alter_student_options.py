# Generated by Django 5.0.3 on 2024-03-27 08:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_student"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["name"]},
        ),
    ]
