# Generated by Django 3.2.9 on 2021-12-24 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0005_alter_businesstaskchildcomment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstask',
            options={'permissions': [('task_edit_field_permisson', 'Task Edit Field Permission')], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
