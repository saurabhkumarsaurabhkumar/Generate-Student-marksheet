# Generated by Django 2.1.7 on 2019-10-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0019_auto_20191007_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarksheetdata',
            name='degree1',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
