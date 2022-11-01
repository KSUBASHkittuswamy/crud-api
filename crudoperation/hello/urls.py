from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.home,name='home'),
    path('indexview/',views.index,name='index'),
    path('create',views.create_user,name="create"), 
    path('retrieve',views.retrieve_user,name="retrieve"), 
    path('edit/<int:id>/',views.edit_user,name="edit"),
    path('update/<int:id>/',views.update_user,name="update"),  
    path('delete/<int:id>',views.delete_user,name="delete")
 ]
