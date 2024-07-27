# Generated by Django 4.2 on 2024-07-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'منابع',
                'verbose_name_plural': 'منابع',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن خبر')),
                ('resources', models.ManyToManyField(related_name='منابع', to='news.resources')),
                ('tags', models.ManyToManyField(related_name='تگ', to='news.tags')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]
