# Generated by Django 3.2.4 on 2021-08-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picpart', '0002_auto_20210807_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictureupgrade',
            name='state',
            field=models.JSONField(default=dict),
        ),
    ]
