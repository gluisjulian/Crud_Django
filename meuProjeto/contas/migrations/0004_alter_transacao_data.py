# Generated by Django 4.1.7 on 2023-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_alter_transacao_data_alter_transacao_observacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
