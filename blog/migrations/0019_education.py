# Generated by Django 3.0.7 on 2020-06-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200630_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField(default='')),
                ('institution', models.TextField(default='')),
                ('duration', models.TextField(default='')),
                ('item1', models.TextField(default='')),
                ('item1_grade', models.DecimalField(decimal_places=2, default=40.0, max_digits=2)),
                ('item2', models.TextField(default='')),
                ('item2_grade', models.DecimalField(decimal_places=2, default=40.0, max_digits=2)),
                ('item3', models.TextField(default='')),
                ('item3_grade', models.DecimalField(decimal_places=2, default=40.0, max_digits=2)),
            ],
        ),
    ]
