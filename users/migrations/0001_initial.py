# Generated by Django 5.1.4 on 2024-12-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('grade', models.IntegerField(default=7)),
                ('IC', models.IntegerField(default=11111111)),
            ],
            options={
                'db_table': 'simpleuser',
            },
        ),
    ]
