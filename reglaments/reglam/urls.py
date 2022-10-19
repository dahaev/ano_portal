from django.urls import path
from .views import *
from rest_framework import routers
from django.urls import include

router = routers.SimpleRouter()
router_task = routers.SimpleRouter()
router.register(r'reglam', ReglamentListApiView)
router_task.register(r'task', TasksListApiView)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('reg/<slug:post_slug>', ReglamView.as_view(), name='show_post_reg'),
    path('reg/', ReglamIndex.as_view(), name='reglaments'),
    path('projects', ProjectList.as_view(), name='projects'),
    path('projects/<task_pk>', ProjectView.as_view(), name='view'),
    path('reports/', report, name='reports'),
    path('instructions', instruction, name='instruction'),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router_task.urls)),
    path('news', NewsListView.as_view()),
    path('updatedb', db_update, name='update'),

]
