# Generated by Django 2.1.2 on 2021-04-12 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_student_no_dues'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.CharField(max_length=100)),
                ('accept', models.BooleanField(default=False)),
                ('reject', models.BooleanField(default=False)),
                ('confirm_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='repair',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('N', 'None'), ('M', 'Male'), ('F', 'Female')], default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='selection.Room'),
        ),
        migrations.AddField(
            model_name='leave',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selection.Student'),
        ),
    ]
