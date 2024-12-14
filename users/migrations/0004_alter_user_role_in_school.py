# Generated by Django 5.1.4 on 2024-12-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_ic_user_nc_user_role_in_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_in_school',
            field=models.CharField(choices=[('MG', 'MANAGER'), ('MO', 'MODERATOR'), ('ST', 'STUDENT')], default='STUDENT', max_length=100),
        ),
    ]