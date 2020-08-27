# Generated by Django 3.0.6 on 2020-08-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_web', '0002_auto_20200812_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('introduction', models.TextField()),
                ('area', models.CharField(max_length=15)),
                ('party_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='DjangoBoard',
        ),
    ]