# Generated by Django 5.0.2 on 2024-02-21 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_alter_post_body_alter_post_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['userId']},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(),
        ),
        migrations.AddField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='posts.user'),
        ),
    ]