# Generated by Django 2.1.5 on 2019-02-27 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20190226_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]