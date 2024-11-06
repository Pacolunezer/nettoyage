# Generated by Django 4.2.3 on 2024-10-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nettoyage', '0004_alter_cleaningservice_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='nom',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='prenom',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='telephone',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
    ]
