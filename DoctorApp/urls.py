
from django.urls import path,include
from DoctorApp import views

urlpatterns = [
   
    path('',views.doc),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]
