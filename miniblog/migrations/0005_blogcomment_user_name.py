# Generated by Django 2.2.2 on 2019-06-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0004_blogreader'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniblog.BlogReader'),
        ),
    ]