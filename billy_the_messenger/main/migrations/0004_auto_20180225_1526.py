# Generated by Django 2.0.2 on 2018-02-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180225_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='primary', max_length=50),
        ),
    ]
