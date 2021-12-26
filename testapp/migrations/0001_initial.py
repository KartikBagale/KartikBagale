# Generated by Django 3.1.7 on 2021-12-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('esal', models.FloatField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]