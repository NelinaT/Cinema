# Generated by Django 4.0.4 on 2024-02-01 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_alter_movie_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_empty', models.BooleanField(default=True)),
                ('projection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.projection')),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.seat')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Seats_for_projection',
        ),
    ]