# Generated by Django 2.1.5 on 2019-02-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20190225_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='id',
            field=models.AutoField(help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
