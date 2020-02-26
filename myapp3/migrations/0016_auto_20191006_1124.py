# Generated by Django 2.1.7 on 2019-10-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0015_studentmarksheetdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarksheetdata',
            name='degree',
            field=models.CharField(default='uuid.uuid1', max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='studentmarksheetdata',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentmarksheetdata',
            name='branch_cse',
            field=models.CharField(default='00000', max_length=100, null=True),
        ),
    ]
