# Generated by Django 2.2.2 on 2019-06-22 19:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0007_auto_20190622_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular blog entry across whole blog', primary_key=True, serialize=False),
        ),
    ]