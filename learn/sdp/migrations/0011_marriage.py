# Generated by Django 4.1.1 on 2022-11-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0010_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='marriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=200)),
                ('halladd', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200)),
                ('pricepe', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=200)),
                ('phno', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]