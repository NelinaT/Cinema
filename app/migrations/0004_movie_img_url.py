# Generated by Django 4.0.4 on 2024-01-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_seat_col_alter_seat_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img_url',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
