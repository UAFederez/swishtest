# Generated by Django 2.2.5 on 2021-01-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20210103_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
