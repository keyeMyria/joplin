# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 21:18
from __future__ import unicode_literals

import base.blocks
from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20180323_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='call_to_action',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='call_to_action_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='call_to_action_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='call_to_action_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='call_to_action_vi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='dynamic_content',
            field=wagtail.core.fields.StreamField((('map_block', base.blocks.SnippetChooserBlockWithAPIGoodness('base.Map', icon='site')), ('what_do_i_do_with_block', base.blocks.WhatDoIDoWithBlock()), ('collection_schedule_block', base.blocks.CollectionScheduleBlock()), ('recollect_block', base.blocks.RecollectBlock())), verbose_name='Add any forms, maps, apps, or content that will help the resident use the service'),
        ),
    ]
