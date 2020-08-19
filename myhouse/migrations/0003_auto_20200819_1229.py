# Generated by Django 3.1 on 2020-08-19 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0002_auto_20200819_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='bedroom',
            field=models.CharField(choices=[('1', '1室1厅'), ('2', '2室1厅'), ('3', '2室2厅'), ('4', '3室1厅'), ('5', '3室2厅'), ('6', '4室2厅')], max_length=1, verbose_name='房型'),
        ),
    ]
