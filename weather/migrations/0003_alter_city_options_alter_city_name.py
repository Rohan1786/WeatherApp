# Generated by Django 5.0.6 on 2024-07-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_city_options_alter_city_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
