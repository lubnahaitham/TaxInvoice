# Generated by Django 4.0.2 on 2022-03-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_alter_pos_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
