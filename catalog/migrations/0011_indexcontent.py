# Generated by Django 3.0.8 on 2020-09-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200903_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
    ]
