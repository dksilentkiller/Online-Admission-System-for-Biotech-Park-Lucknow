# Generated by Django 5.1 on 2024-09-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0006_delete_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
