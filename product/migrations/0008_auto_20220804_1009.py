# Generated by Django 3.2.14 on 2022-08-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_predictproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PredictProduct',
        ),
        migrations.AddField(
            model_name='product',
            name='answer',
            field=models.CharField(default='default', max_length=70),
        ),
    ]
