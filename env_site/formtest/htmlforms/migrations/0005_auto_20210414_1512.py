# Generated by Django 3.1.7 on 2021-04-14 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0004_auto_20210414_1510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jsonFormEntry',
            new_name='jsonEntry',
        ),
        migrations.RenameField(
            model_name='jsonentry',
            old_name='jentry',
            new_name='jEntry',
        ),
    ]