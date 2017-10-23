# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20171022_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='university_bachelor',
            field=models.CharField(default='-', max_length=70),
        ),
        migrations.AddField(
            model_name='education',
            name='university_master',
            field=models.CharField(default='-', max_length=70),
        ),
        migrations.AddField(
            model_name='education',
            name='university_phD',
            field=models.CharField(default='-', max_length=70),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='เบอร์โทรบ้าน(ปัจจุบัน)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='birth_date',
            field=models.DateField(verbose_name='วัน/เดือน/ปี เกิด'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='blood_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=6, verbose_name='กรุ๊ปเลือด'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='card_number',
            field=models.CharField(max_length=20, verbose_name='เลขบัตรประชาชน'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='domicile_province',
            field=models.CharField(max_length=30, verbose_name='ภูมิลำเนาเดิม จังหวัด'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstname_eng',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริง(อังกฤษ)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstname_father_thai',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริง(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstname_spouse_eng',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริงคู่สมรส(อังกฤษ)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstname_spouse_thai',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริงคู่สมรส(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstname_thai',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริง(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='firstnamename_father_eng',
            field=models.CharField(max_length=30, verbose_name='ชื่อจริง(อังกฤษ)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastname_eng',
            field=models.CharField(max_length=30, verbose_name='นามสกุล(อังกฤษ)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastname_father_thai',
            field=models.CharField(max_length=30, verbose_name='คำนำหน้า(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastname_spouse_eng',
            field=models.CharField(max_length=30, verbose_name='นามสกุลคู่สมรส(อังกฤษ)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastname_spouse_thai',
            field=models.CharField(max_length=30, verbose_name='นามสกุลคู่สมรส(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lastname_thai',
            field=models.CharField(max_length=30, verbose_name='นามสกุล(ไทย)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='religion',
            field=models.CharField(max_length=20, verbose_name='ศาสนา'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='status',
            field=models.CharField(choices=[('MR', 'Married(แต่งงาน)'), ('SN', 'Single(โสด)'), ('DV', 'Divorce(หย่า)'), ('WD', 'Widow(หม้าย)')], max_length=10, verbose_name='สถานะ'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.(นาย)'), ('MRS', 'Mrs.(นาง)'), ('MISS', 'Miss.(นางสาว)')], max_length=6),
        ),
    ]