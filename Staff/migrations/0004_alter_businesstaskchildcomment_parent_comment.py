# Generated by Django 3.2.9 on 2021-12-23 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0003_auto_20211223_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstaskchildcomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_tasks_child', to='Staff.businesstaskcomment', verbose_name='Parent Comment'),
        ),
    ]
