# Generated by Django 3.0.5 on 2023-05-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_contact', models.CharField(max_length=10)),
                ('user_password', models.CharField(max_length=6)),
                ('user_city', models.CharField(max_length=20)),
                ('user_state', models.CharField(max_length=25)),
                ('user_pincode', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
    ]
