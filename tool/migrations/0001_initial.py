# Generated by Django 3.2.19 on 2023-05-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionDBConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=50, null=True)),
                ('db_config', models.JSONField(null=True)),
            ],
        ),
    ]
