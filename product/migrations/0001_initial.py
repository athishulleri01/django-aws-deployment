# Generated by Django 4.2.5 on 2023-09-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('images', models.ImageField(upload_to='images/products/')),
                ('image1', models.ImageField(upload_to='images/products/')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('original_price', models.FloatField()),
                ('selling_prince', models.FloatField()),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_data', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.sub_category')),
            ],
        ),
    ]