from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView, ListView
from .models import *
from .serializers import Reglam_Serizalizer, Task_Serializer
from rest_framework import generics, viewsets
from ano_connect import db_python_config
from reglam.tasks import update_data_base_celery
import datetime

class NewsListView(ListView):
    template_name = 'reglam/news.html'
    model = News
    context_object_name = 'news'


class ReglamIndex(ListView):
    template_name = 'reglam/reglam.html'
    model = Reglaments
    context_object_name = 'reg_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReglamView(DetailView):
    template_name = 'reglam/reglam_view.html'
    model = Reglaments
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


def ShowReglament(request, order_slug):
    a = get_object_or_404(Reglaments, reg_slug=order_slug)
    context = {'post': a}
    return render(request, 'reglam/reglam_view.html', context=context)


class ProjectList(ListView):
    template_name = 'reglam/projects.html'
    model = AnoTasks
    context_object_name = 'rv_task'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        result = AnoTasks.objects.all().filter(task_code='7.4', upload_date=f'{datetime.datetime.now().date()}').order_by(
            'task_date_end').count()
        context['project_count'] = result
        return context

    def get_queryset(self):
        return AnoTasks.objects.all().filter(task_code='7.4', upload_date=f'{datetime.datetime.now().date()}').order_by('task_date_end')


class ProjectView(DetailView):
    template_name = 'reglam/project_view.html'
    model = AnoTasks
    pk_url_kwarg = 'task_pk'
    context_object_name = 'post'


def report(request):
    return render(request, 'reglam/reports.html')


def instruction(request):
    return render(request, 'reglam/instructions.html')


class IndexView(ListView):
    model = AnoTasks
    template_name = 'reglam/index.html'
    context_object_name = 'index_view'
    paginate_by = 18

    def get_queryset(self):
        return AnoTasks.objects.all().filter(reaper_4q2022_plan__isnull=False, upload_date=f'{datetime.datetime.now().date()}').order_by('task_date_end','project_name')


class ReglamentListApiView(viewsets.ModelViewSet):
    queryset = Reglaments.objects.all()
    serializer_class = Reglam_Serizalizer


class TasksListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = AnoTasks.objects.all()
    serializer_class = Task_Serializer


def db_update(request):
    start_time = datetime.datetime.now()
    db_python_config.update_data_base()
    end_time = datetime.datetime.now()
    # update_data_base_celery.delay()
    return HttpResponse(f'Обновление базы данных запущено: {start_time - end_time}')

