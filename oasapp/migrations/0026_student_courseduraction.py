# Generated by Django 5.0.6 on 2024-09-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0025_tbl_course_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courseduraction',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
