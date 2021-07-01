# Generated by Django 3.1.1 on 2021-06-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_client_num_visited'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibition',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='exhibition',
            name='clients_visited',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
