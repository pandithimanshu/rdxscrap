# Generated by Django 3.0.7 on 2020-09-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='defaulttitle', max_length=100)),
                ('author', models.CharField(default='defaultauthor', max_length=100)),
                ('tag', models.CharField(default='defaulttag', max_length=100)),
            ],
        ),
    ]
