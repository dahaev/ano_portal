from django.db import models
from django.urls import reverse


class Reglaments(models.Model):
    reg_name = models.CharField(max_length=255, verbose_name='Название регламента')
    reg_date = models.DateField(auto_now=False, verbose_name='Дата создания')
    reg_status = models.BooleanField(null=True, verbose_name='Статус')
    slug = models.SlugField(max_length=50)
    reg_type = models.ForeignKey('ReglamentsType', on_delete=models.PROTECT, verbose_name='Тип регламента')
    reg_dep = models.ForeignKey('ReglamentsDepartment', on_delete=models.PROTECT, verbose_name='Организация')
    reg_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Регламенты'
        verbose_name_plural = 'Регламенты'

    def __str__(self):
        return self.reg_name

    def get_absolute_url(self):
        return reverse('show_post_reg', kwargs={'post_slug': self.slug})


class ReglamentsType(models.Model):
    reg_type = models.CharField(max_length=255, verbose_name='Тип регламента')
    reg_slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Тип регламента'
        verbose_name_plural = 'Тип регламента'

    def __str__(self):
        return self.reg_type


# Create your models here.

class ReglamentsDepartment(models.Model):
    reg_dep = models.CharField(max_length=255, verbose_name='Организация')
    reg_slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

    def __str__(self):
        return self.reg_dep


class AnoTasks(models.Model):
    project_id = models.CharField(max_length=50, blank=True, null=True)
    project_name = models.CharField(max_length=250, blank=True, null=True)
    task_code = models.CharField(max_length=50, blank=True, null=True)
    task_name = models.CharField(max_length=250, blank=True, null=True)
    task_date_start = models.DateField(blank=True, null=True)
    task_date_end = models.DateField(blank=True, null=True)
    task_done_percent = models.FloatField(blank=True, null=True)
    task_base_start = models.DateField(blank=True, null=True)
    task_base_end = models.DateField(blank=True, null=True)
    task_status = models.CharField(max_length=50, blank=True, null=True)
    task_active = models.CharField(max_length=50, blank=True, null=True)
    reaper_task = models.CharField(max_length=50, blank=True, null=True)
    reaper_3q2022_plan = models.DateField(blank=True, null=True)
    reaper_4q2022_plan = models.DateField(blank=True, null=True)
    reaper_1q2023_plan = models.DateField(blank=True, null=True)
    reaper_2q2023_plan = models.DateField(blank=True, null=True)
    reaper_3q2023_plan = models.DateField(blank=True, null=True)
    upload_date = models.DateField(null=True)

    # slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('view', kwargs={'task_pk': self.pk})

    class Meta:
        managed = False
        db_table = 'ano_tasks'


class Test(models.Model):
    test = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('test', kwargs={'test': self.pk})


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Новости')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(blank=True, verbose_name='Текст новости')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
