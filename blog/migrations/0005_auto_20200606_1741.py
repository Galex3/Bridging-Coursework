# Generated by Django 3.0.7 on 2020-06-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200606_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
