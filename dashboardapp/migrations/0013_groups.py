# Generated by Django 4.1.2 on 2022-11-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0012_student_9a_rename_student2a_student_10a_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('1D', '1D'), ('1F', '1F'), ('2A', '2A'), ('2B', '2B'), ('2D', '2D'), ('2F', '2F'), ('3A', '3A'), ('3B', '3B'), ('3D', '3D'), ('3F', '3F'), ('4A', '4A'), ('4B', '4B'), ('4D', '4D'), ('4F', '4F'), ('5A', '5A'), ('5B', '5B'), ('5D', '5D'), ('5F', '5F'), ('6A', '6A'), ('6B', '6B'), ('6D', '6D'), ('6F', '6F'), ('7A', '7A'), ('7B', '7B'), ('7D', '7D'), ('7F', '7F'), ('8A', '8A'), ('8B', '8B'), ('8D', '8D'), ('8F', '8F'), ('9A', '9A'), ('9B', '9B'), ('9D', '9D'), ('9F', '9F'), ('10A', '10A'), ('10B', '10B'), ('10D', '10D'), ('11A', '11A'), ('11B', '11B'), ('11D', '11D'), ('11F', '11F')], default='1A', max_length=30)),
            ],
        ),
    ]
