# Generated by Django 2.1.7 on 2019-02-17 05:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceDetection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetection',
            name='rects',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None),
        ),
    ]
