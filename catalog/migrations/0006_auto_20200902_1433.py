# Generated by Django 3.0.8 on 2020-09-02 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200902_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_edit_authors', 'Edit authors'),)},
        ),
    ]
