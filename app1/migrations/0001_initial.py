# Generated by Django 5.1.3 on 2025-05-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=20)),
                ('sub1', models.IntegerField()),
                ('sub2', models.IntegerField()),
            ],
        ),
    ]
