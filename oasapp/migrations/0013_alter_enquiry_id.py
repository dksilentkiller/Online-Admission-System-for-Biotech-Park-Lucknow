# Generated by Django 5.1 on 2024-09-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0012_tbl_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
