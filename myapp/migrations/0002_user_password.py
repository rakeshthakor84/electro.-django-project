# Generated by Django 4.1.2 on 2022-10-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
