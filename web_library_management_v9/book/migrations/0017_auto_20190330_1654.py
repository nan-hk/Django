# Generated by Django 2.1.5 on 2019-03-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20190310_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
