# Generated by Django 2.1.7 on 2020-02-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboPortal', '0007_auto_20200221_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]