# Generated by Django 4.2 on 2023-08-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_demo_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesettings',
            name='layoutPage_button_text',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='websitesettings',
            name='layoutPage_image1',
            field=models.ImageField(default=1, upload_to='layImage1/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='websitesettings',
            name='layoutPage_image2',
            field=models.ImageField(upload_to='layImage2/'),
        ),
        migrations.AlterField(
            model_name='websitesettings',
            name='layoutPage_subtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='websitesettings',
            name='layoutPage_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]