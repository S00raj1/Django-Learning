# Generated by Django 4.2.2 on 2023-06-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_rename_edate_book_location_endingdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_location',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]