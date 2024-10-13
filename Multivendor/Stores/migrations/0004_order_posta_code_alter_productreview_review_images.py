# Generated by Django 5.1.1 on 2024-09-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='posta_code',
            field=models.CharField(default='0000', max_length=20),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
