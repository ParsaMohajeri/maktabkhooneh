# Generated by Django 3.2.25 on 2024-03-15 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240315_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created_date',)},
        ),
    ]