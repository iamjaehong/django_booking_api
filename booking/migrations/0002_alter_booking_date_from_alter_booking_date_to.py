# Generated by Django 4.2.3 on 2023-07-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
