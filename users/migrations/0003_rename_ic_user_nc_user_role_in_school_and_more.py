# Generated by Django 5.1.4 on 2024-12-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_major'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='IC',
            new_name='NC',
        ),
        migrations.AddField(
            model_name='user',
            name='role_in_school',
            field=models.CharField(choices=[('MG', 'MANAGER'), ('MO', 'MODERATOR'), ('ST', 'STUDENT')], default=('STUDENT',), max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, default=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]