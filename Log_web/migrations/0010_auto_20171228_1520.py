# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Log_web', '0009_auto_20171225_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distributor',
            old_name='godown_id',
            new_name='godown',
        ),
        migrations.RenameField(
            model_name='distributor_package',
            old_name='distributor_id',
            new_name='distributor',
        ),
        migrations.RenameField(
            model_name='distributor_package',
            old_name='package_id',
            new_name='package',
        ),
        migrations.RenameField(
            model_name='godown_staff',
            old_name='godown_id',
            new_name='godown',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='distributor_id',
        ),
        migrations.RemoveField(
            model_name='godown_staff',
            name='staff_id',
        ),
        migrations.AddField(
            model_name='distributor',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log_web.Login_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distributor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='godown_staff',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='godown_staff',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log_web.Login_user'),
            preserve_default=False,
        ),
    ]