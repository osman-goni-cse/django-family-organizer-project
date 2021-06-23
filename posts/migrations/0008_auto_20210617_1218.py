# Generated by Django 3.2 on 2021-06-17 06:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20210617_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 17, 6, 18, 35, 523307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 17, 6, 18, 35, 523307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='todo_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 17, 6, 18, 35, 523307, tzinfo=utc)),
        ),
    ]