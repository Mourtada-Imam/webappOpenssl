# Generated by Django 2.1 on 2020-10-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDomain', models.TextField()),
                ('nomOrg', models.TextField()),
                ('deprt', models.TextField()),
                ('ville', models.TextField()),
                ('region', models.TextField()),
                ('code', models.TextField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
