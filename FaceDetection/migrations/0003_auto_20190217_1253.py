# Generated by Django 2.1.7 on 2019-02-17 05:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceDetection', '0002_auto_20190217_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetection',
            name='rects',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), max_length=4, size=None), size=None),
        ),
    ]
