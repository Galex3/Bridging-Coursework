# Generated by Django 3.0.7 on 2020-06-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.TextField(blank=True, default=''),
        ),
    ]
