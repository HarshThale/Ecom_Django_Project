# Generated by Django 4.2.7 on 2023-12-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('MC', 'Mac'), ('ID', 'IPad'), ('IP', 'IPhone'), ('WT', 'Watch'), ('AP', 'Airpods'), ('TV', 'TV & Home'), ('ET', 'Entertainment'), ('AC', 'Accessories')], max_length=2, null=True),
        ),
    ]