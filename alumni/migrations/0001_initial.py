# Generated by Django 2.1.7 on 2019-09-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
