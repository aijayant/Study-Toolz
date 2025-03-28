from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('semester/<int:semester_id>/', semester_detail, name='semester_detail'),
    path('semester/<int:semester_id>/<str:category>/', category_list, name='category_list'),
    # path('pdf_list',pdf_list,name='pdf_list'),
    # path('music',music_list,name='music'),
    # path('questions',question_list,name='questions'),
]