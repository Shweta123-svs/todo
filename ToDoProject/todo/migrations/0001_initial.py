# Generated by Django 4.0.1 on 2022-09-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('is_deleted', models.CharField(max_length=20)),
            ],
        ),
    ]
