# Generated by Django 4.0.4 on 2024-02-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_ticket_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(max_length=10, null=True),
        ),
    ]