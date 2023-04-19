# Generated by Django 4.2 on 2023-04-19 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.organization'),
            preserve_default=False,
        ),
    ]
