# Generated by Django 4.1.7 on 2023-06-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoul_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkJsonPoisAreasHourData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sk_pois_hour_data', models.JSONField()),
                ('sk_areas_hour_data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
