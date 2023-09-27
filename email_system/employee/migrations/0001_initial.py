# Generated by Django 3.2.18 on 2023-08-10 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('level', models.CharField(choices=[('INFO', 'Info'), ('ERROR', 'Error'), ('WARNING', 'Warning'), ('SUCCESS', 'Success')], default='INFO', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Marriage Anniversary', 'Marriage Anniversary'), ('Work Anniversary', 'Work Anniversary')], max_length=50)),
                ('event_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]