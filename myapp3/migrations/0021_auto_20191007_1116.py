# Generated by Django 2.1.7 on 2019-10-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0020_studentmarksheetdata_degree1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarksheetdata',
            name='degree1',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
