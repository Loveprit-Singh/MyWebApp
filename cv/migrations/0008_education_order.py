# Generated by Django 2.1a1 on 2018-08-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_experience_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='order',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
