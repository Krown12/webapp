# Generated by Django 5.0.3 on 2024-04-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_liked', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(blank=True, max_length=150, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user/images/')),
            ],
        ),
    ]