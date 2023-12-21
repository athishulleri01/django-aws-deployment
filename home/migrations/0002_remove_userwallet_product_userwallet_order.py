# Generated by Django 4.2.5 on 2023-11-01 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_notification'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='product',
        ),
        migrations.AddField(
            model_name='userwallet',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
            preserve_default=False,
        ),
    ]
