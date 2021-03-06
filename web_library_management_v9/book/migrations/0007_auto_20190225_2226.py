# Generated by Django 2.1.5 on 2019-02-25 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0006_auto_20190224_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.IntegerField(help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('borrow_date', models.DateField(blank=True, null=True)),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='borrower',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='book',
            name='borrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Borrow'),
        ),
    ]
