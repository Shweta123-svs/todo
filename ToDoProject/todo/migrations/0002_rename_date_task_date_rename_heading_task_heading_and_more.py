# Generated by Django 4.0.1 on 2022-09-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='heading',
            new_name='Heading',
        ),
        migrations.AlterField(
            model_name='task',
            name='is_deleted',
            field=models.CharField(max_length=2),
        ),
    ]