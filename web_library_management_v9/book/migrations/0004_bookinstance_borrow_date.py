# Generated by Django 2.1.5 on 2019-02-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrow_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
