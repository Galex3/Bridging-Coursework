# Generated by Django 3.0.7 on 2020-06-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200630_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
