# Generated by Django 4.1.2 on 2022-11-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0002_delete_mentor_student_klass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('student', models.CharField(max_length=50)),
                ('spesalis', models.CharField(choices=[('math', 'math'), ('motherlangue', 'motherlangue'), ('physc', 'physc'), ('geografe', 'geografe'), ('music', 'music'), ('archihtura', 'archihtura'), ('work', 'work'), ('english', 'english'), ('russian', 'russian'), ('history', 'history'), ('literature', 'literature')], default='math', max_length=50)),
            ],
        ),
    ]
