# Generated by Django 4.0.2 on 2022-11-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data',
            field=models.DateField(null=True),
        ),
    ]