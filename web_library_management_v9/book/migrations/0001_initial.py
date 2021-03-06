# Generated by Django 2.1.5 on 2019-02-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=20)),
                ('rentalStatus', models.IntegerField()),
                ('summary', models.CharField(max_length=200)),
                ('releaseDate', models.DateField()),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['releaseDate'],
            },
        ),
    ]
