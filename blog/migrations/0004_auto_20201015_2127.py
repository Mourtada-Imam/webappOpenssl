# Generated by Django 2.1 on 2020-10-15 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20201015_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='cert',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cert',
            name='nomDomain',
            field=models.CharField(max_length=100),
        ),
    ]
