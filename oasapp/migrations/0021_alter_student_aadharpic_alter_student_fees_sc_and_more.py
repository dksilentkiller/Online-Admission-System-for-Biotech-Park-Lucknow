# Generated by Django 5.1 on 2024-09-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasapp', '0020_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aadharpic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='fees_sc',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='hs_marksheet',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='inter_marksheet',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='sign',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
