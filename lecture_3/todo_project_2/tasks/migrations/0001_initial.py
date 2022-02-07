# Generated by Django 4.0.2 on 2022-02-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('CO', 'Completed'), ('PE', 'Pending'), ('DR', 'Dropped')], default='PE', max_length=2)),
                ('tag', models.ManyToManyField(to='tasks.Tag')),
            ],
        ),
    ]