# Generated by Django 5.0.2 on 2024-02-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_project_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_category',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('Database', 'Database'), ('Machine Learning', 'Machine Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Data Science', 'Data Science')], default='WB', max_length=255),
        ),
    ]
