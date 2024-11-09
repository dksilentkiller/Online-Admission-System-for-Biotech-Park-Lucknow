# Generated by Django 5.1 on 2024-09-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0011_alter_enquiry_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_course',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=300)),
                ('course_fees', models.CharField(max_length=100)),
                ('course_session', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]