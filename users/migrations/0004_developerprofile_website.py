# Generated by Django 5.0.2 on 2024-03-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_status_developerprofile_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]