# Generated by Django 2.2.1 on 2019-05-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.TextField(max_length=65, null=True),
        ),
    ]
