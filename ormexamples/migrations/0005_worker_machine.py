# Generated by Django 4.2.2 on 2023-07-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormexamples', '0004_alter_customer_table_alter_customer_one_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('workers', models.ManyToManyField(related_name='Machine', to='ormexamples.worker')),
            ],
        ),
    ]