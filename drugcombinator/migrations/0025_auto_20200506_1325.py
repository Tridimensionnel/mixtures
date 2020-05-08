# Generated by Django 3.0.6 on 2020-05-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugcombinator', '0024_auto_20200506_1318'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='interaction',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='interaction',
            constraint=models.UniqueConstraint(fields=('from_drug', 'to_drug'), name='interactants_unique_together'),
        ),
    ]
