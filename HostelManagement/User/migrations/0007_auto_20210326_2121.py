# Generated by Django 3.1.7 on 2021-03-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20210326_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sd_feedback',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sd_fees',
            field=models.CharField(max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sd_remark',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sd_university_register',
            field=models.CharField(max_length=50, null=True),
        ),
    ]