# Generated by Django 3.2.11 on 2022-02-22 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_commenttopic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commenttopic',
            old_name='coment',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='commenttopic',
            name='view_count',
        ),
    ]