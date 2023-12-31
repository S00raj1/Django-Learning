# Generated by Django 4.2.2 on 2023-06-27 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_location',
            name='g_phone',
        ),
        migrations.RemoveField(
            model_name='add_location',
            name='guide',
        ),
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
