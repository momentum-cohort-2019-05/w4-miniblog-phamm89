# Generated by Django 2.2.2 on 2019-06-24 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]