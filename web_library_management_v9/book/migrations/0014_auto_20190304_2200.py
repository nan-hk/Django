# Generated by Django 2.1.5 on 2019-03-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_borrow_return_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrow',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.AddField(
            model_name='borrow',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='d', help_text='Book availability', max_length=1),
        ),
    ]