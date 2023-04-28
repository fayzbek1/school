# Generated by Django 4.1.4 on 2023-01-04 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboardapp', '0019_user_profiles_delete_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(max_length=70)),
                ('about', models.TextField()),
                ('adress', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('avatar', models.ImageField(upload_to='profile')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User_profiles',
        ),
    ]
