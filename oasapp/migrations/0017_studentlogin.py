# Generated by Django 5.1 on 2024-09-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0016_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
