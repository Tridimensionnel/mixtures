# Generated by Django 2.2.10 on 2020-04-24 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugcombinator', '0012_auto_20200424_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='from_drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='drugcombinator.Drug', verbose_name='première substance'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='to_drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='drugcombinator.Drug', verbose_name='seconde substance'),
        ),
    ]