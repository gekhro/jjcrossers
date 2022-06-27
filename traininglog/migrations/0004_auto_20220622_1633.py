# Generated by Django 3.2.13 on 2022-06-22 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('traininglog', '0003_auto_20220622_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.CharField(max_length=50)),
                ('time2', models.CharField(max_length=50)),
                ('time3', models.CharField(max_length=50)),
                ('time4', models.CharField(max_length=50)),
                ('time5', models.CharField(max_length=50)),
                ('time6', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
