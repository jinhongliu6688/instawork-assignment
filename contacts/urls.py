from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add-contact/', views.Add.as_view(), name='add-contact'),
    path('edit-contact/<str:pk>', views.Edit.as_view(), name='edit-contact'),
    path('delete-contact/<str:pk>', views.deleteContact, name='delete-contact'),
]