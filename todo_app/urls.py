from django.urls import path
from .views import Worklist, Workdetail, WorkCreate, WorkUpdate, WorDelete

urlpatterns = [
    path('', Worklist.as_view(), name='works'),
    path('work/<str:pk>/', Workdetail.as_view(), name='work'),
    path('work/<str:pk>/update', WorkUpdate.as_view(), name='update'),
    path('work/<str:pk>/delete', WorDelete.as_view(), name='delete'),
    path('create/', WorkCreate.as_view(), name='work_create'),
]
