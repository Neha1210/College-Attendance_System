from django.conf.urls.static import  static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns=[
  path('',views.Dashboard,name="Dashboard"),
  path('dd',views.upldatabase,name='upld'),
  path('ams_clerk',views.home,name="home"),
  path('add_file',views.createupload,name='createupload'),
  path('update_file<str:pk>',views.update,name='updatefile'),
  path('delete_File<str:pk>',views.delete,name='deletefile'),
  path('search_file',views.search,name='searchfile'),
  path('loginpage_clerk',views.loginpage,name='loginpage_clerk'),
  path('registerpage',views.registerpage,name='register'),
  path('faculty_home',views.facultyhome,name='faculty'),
  path('faculty_registration',views.facultyreg,name='facultyreg'),
  path('faculty_loginpage',views.floginpage,name='floginpage'),
  path('faculty_create_profile',views.facultyprofile,name='facultyprofile'),
  path('faculty_update_profile<str:pk>',views.fupdateprofile,name='fupdateprofile'),
  path('faculty_view_profile<str:pk>',views.fview,name='fview'),
  path('facultydemoatt<str:pk>',views.atten,name='getat'),
  path('update_Attendance<str:pk>',views.updateatten,name='updateatten'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)