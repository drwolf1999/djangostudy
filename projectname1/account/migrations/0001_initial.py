# Generated by Django 2.2.3 on 2019-08-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('userId', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('nick', models.CharField(max_length=10)),
            ],
        ),
    ]
