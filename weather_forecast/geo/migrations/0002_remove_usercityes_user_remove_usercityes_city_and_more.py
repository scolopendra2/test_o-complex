# Generated by Django 5.0.7 on 2024-07-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercityes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usercityes',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='request_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserCityes',
        ),
    ]