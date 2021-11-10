# Generated by Django 3.1.7 on 2021-10-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'very good'), (2, 'Good'), (3, 'Not Good'), (4, 'Excellent'), (5, 'Ultra Excellent')]),
        ),
    ]
