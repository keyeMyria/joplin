# Generated by Django 2.0.5 on 2018-06-14 17:25

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20180614_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processpagestep',
            name='overview_content',
        ),
        migrations.AddField(
            model_name='processpagestep',
            name='overview_steps',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Write out the steps a resident needs to take to use the service'),
        ),
        migrations.AddField(
            model_name='processpagestep',
            name='overview_steps_ar',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write out the steps a resident needs to take to use the service'),
        ),
        migrations.AddField(
            model_name='processpagestep',
            name='overview_steps_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write out the steps a resident needs to take to use the service'),
        ),
        migrations.AddField(
            model_name='processpagestep',
            name='overview_steps_es',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write out the steps a resident needs to take to use the service'),
        ),
        migrations.AddField(
            model_name='processpagestep',
            name='overview_steps_vi',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Write out the steps a resident needs to take to use the service'),
        ),
    ]