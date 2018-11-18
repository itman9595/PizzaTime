# Generated by Django 2.1.3 on 2018-11-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Number', models.IntegerField()),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Filling', models.CharField(max_length=500)),
                ('Dough_Layer', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Discount', models.FloatField()),
            ],
        ),
    ]
