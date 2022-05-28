# Generated by Django 4.0.4 on 2022-05-28 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brend name')),
                ('img', models.ImageField(upload_to='media', verbose_name='Brend image')),
            ],
            options={
                'verbose_name': 'Brend',
                'verbose_name_plural': 'Brends',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Shoose name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_shoose', to='main.category')),
            ],
            options={
                'verbose_name': 'Shoose',
                'verbose_name_plural': 'Shooses',
            },
        ),
        migrations.DeleteModel(
            name='Bag',
        ),
        migrations.AddField(
            model_name='brend',
            name='shoose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoose_brend', to='main.shoose'),
        ),
    ]