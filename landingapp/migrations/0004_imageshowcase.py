# Generated by Django 2.2.6 on 2019-10-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingapp', '0003_auto_20191027_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageShowCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
