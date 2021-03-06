# Generated by Django 2.1.7 on 2019-03-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0002_tree'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AlterField(
            model_name='tree',
            name='genus',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tree',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tree',
            name='origin',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tree',
            name='species',
            field=models.CharField(max_length=32),
        ),
    ]
