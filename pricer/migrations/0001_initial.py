# Generated by Django 2.2.1 on 2019-05-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
            ],
        ),
    ]
