# Generated by Django 4.0.2 on 2022-02-26 04:31

import apps.ai.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 날짜')),
                ('video_url', models.FileField(default='posts/default', upload_to=apps.ai.models.upload_to)),
                ('user_id', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'record_video',
            },
        ),
    ]
