# Generated by Django 2.1.7 on 2019-10-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0032_auto_20191012_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
