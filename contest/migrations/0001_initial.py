# Generated by Django 3.1.1 on 2021-06-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('qr_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('is_winner', models.BooleanField(blank=True, default=False, null=True)),
                ('special_code', models.CharField(blank=True, max_length=100, null=True)),
                ('exhibitions', models.ManyToManyField(blank=True, related_name='clients', to='contest.Exhibition')),
            ],
        ),
    ]
