# Generated by Django 4.2.2 on 2023-06-26 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_alter_book_location_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_location',
            name='guide',
        ),
        migrations.AlterField(
            model_name='book_location',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location.add_location'),
        ),
        migrations.AddField(
            model_name='book_location',
            name='guide',
            field=models.ManyToManyField(related_name='guide', to='location.guide'),
        ),
    ]
