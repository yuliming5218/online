# Generated by Django 2.0.6 on 2018-06-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationinfo',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程总数'),
        ),
    ]
