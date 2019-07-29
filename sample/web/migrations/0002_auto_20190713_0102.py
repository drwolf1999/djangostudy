# Generated by Django 2.2.3 on 2019-07-12 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
