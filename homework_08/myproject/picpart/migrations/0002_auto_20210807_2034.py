# Generated by Django 3.2.4 on 2021-08-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picpart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pictureupgrade',
            old_name='solve',
            new_name='answers',
        ),
        migrations.RenameField(
            model_name='pictureupgrade',
            old_name='state',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='pictureupgrade',
            old_name='text',
            new_name='x',
        ),
        migrations.AddField(
            model_name='pictureupgrade',
            name='y',
            field=models.JSONField(default=dict),
        ),
    ]