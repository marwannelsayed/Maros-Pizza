# Generated by Django 5.1.6 on 2025-03-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_medium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_large', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='beverage',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.AddField(
            model_name='order',
            name='drink_data',
            field=models.JSONField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='size_data',
            field=models.JSONField(default='s'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Beverage',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
