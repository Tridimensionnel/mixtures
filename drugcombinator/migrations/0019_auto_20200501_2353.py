# Generated by Django 2.2.10 on 2020-05-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugcombinator', '0018_drug_risks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='risks',
            field=models.TextField(blank=True, default='', help_text='Risques ou précautions spécifiques à la combinaison de cette substance avec d\'autres qui ne dépendent pas d\'une interaction particulière.<br/>La syntaxe <a href="https://commonmark.org/help/">markdown</a> est autorisée. Les paragraphes sont séparés par deux retours à la ligne.', verbose_name='risques généraux'),
        ),
    ]
