# Generated by Django 2.2.1 on 2020-07-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_text', models.CharField(max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/posts/')),
            ],
        ),
    ]
