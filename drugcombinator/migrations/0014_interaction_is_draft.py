# Generated by Django 2.2.10 on 2020-04-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugcombinator', '0013_auto_20200425_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='is_draft',
            field=models.BooleanField(default=True, verbose_name='brouillon'),
        ),
    ]