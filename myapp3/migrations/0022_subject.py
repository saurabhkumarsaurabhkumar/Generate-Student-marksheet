# Generated by Django 2.1.7 on 2019-10-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0021_auto_20191007_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=100)),
            ],
        ),
    ]
