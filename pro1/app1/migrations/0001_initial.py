# Generated by Django 5.0.6 on 2024-06-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('laptop_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
