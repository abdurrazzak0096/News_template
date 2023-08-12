# Generated by Django 4.2 on 2023-08-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=50)),
                ('budget', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]