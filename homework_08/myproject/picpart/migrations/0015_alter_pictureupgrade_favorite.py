# Generated by Django 3.2.4 on 2021-08-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picpart', '0014_alter_pictureupgrade_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictureupgrade',
            name='favorite',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
