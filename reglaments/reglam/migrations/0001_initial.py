# Generated by Django 4.1.2 on 2022-10-19 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnoTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(blank=True, max_length=50, null=True)),
                ('project_name', models.CharField(blank=True, max_length=250, null=True)),
                ('task_code', models.CharField(blank=True, max_length=50, null=True)),
                ('task_name', models.CharField(blank=True, max_length=250, null=True)),
                ('task_date_start', models.DateField(blank=True, null=True)),
                ('task_date_end', models.DateField(blank=True, null=True)),
                ('task_done_percent', models.FloatField(blank=True, null=True)),
                ('task_base_start', models.DateField(blank=True, null=True)),
                ('task_base_end', models.DateField(blank=True, null=True)),
                ('task_status', models.CharField(blank=True, max_length=50, null=True)),
                ('task_active', models.CharField(blank=True, max_length=50, null=True)),
                ('reaper_task', models.CharField(blank=True, max_length=50, null=True)),
                ('reaper_3q2022_plan', models.DateField(blank=True, null=True)),
                ('reaper_4q2022_plan', models.DateField(blank=True, null=True)),
                ('reaper_1q2023_plan', models.DateField(blank=True, null=True)),
                ('reaper_2q2023_plan', models.DateField(blank=True, null=True)),
                ('reaper_3q2023_plan', models.DateField(blank=True, null=True)),
                ('upload_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'ano_tasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Новости')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('content', models.TextField(blank=True, verbose_name='Текст новости')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='ReglamentsDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_dep', models.CharField(max_length=255, verbose_name='Организация')),
                ('reg_slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организация',
            },
        ),
        migrations.CreateModel(
            name='ReglamentsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_type', models.CharField(max_length=255, verbose_name='Тип регламента')),
                ('reg_slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Тип регламента',
                'verbose_name_plural': 'Тип регламента',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reglaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=255, verbose_name='Название регламента')),
                ('reg_date', models.DateField(verbose_name='Дата создания')),
                ('reg_status', models.BooleanField(null=True, verbose_name='Статус')),
                ('slug', models.SlugField()),
                ('reg_text', models.TextField(blank=True, null=True)),
                ('reg_dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reglam.reglamentsdepartment', verbose_name='Организация')),
                ('reg_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reglam.reglamentstype', verbose_name='Тип регламента')),
            ],
            options={
                'verbose_name': 'Регламенты',
                'verbose_name_plural': 'Регламенты',
            },
        ),
    ]
