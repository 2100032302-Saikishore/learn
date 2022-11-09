from django.urls import path
from . import views
urlpatterns =[# path('admin/', admin.site.urls),
              path('login/',views.login,name='login' ),
              path('dlogin/', views.dlogin, name='dlogin'),
              path('',views.home,name='home'),
              path('contact/',views.contact,name='contact'),
              path('about/',views.about,name='about'),
              path('faqs/',views.faqs,name='faqs'),
              path('register/',views.register,name='register'),
              path('registerD/', views.registerD, name='registerD'),
              path('base2/', views.base2,name='base2'),
              path('dh/', views.dh, name='dh'),
              path('logselect/',views.logselect,name='logselect'),
              path('movies/', views.movies, name='movies'),
              #  path('movies/',views.movies1,name='movies1'),
              path('music/', views.music1, name='music'),
              # path('catering/', views.catering, name='catering'),
              path('marriage/', views.marriage1, name='marriage1'),
              path('userregisteruser',views.userregisteruser ,name='regis'),
              path('userloginuser',views.userloginuser,name='logs'),
              path('dr',views.dr,name='dr'),
              path('dlogin' ,views.dlogin,name='dlogin'),
              path('catering/',views.Catering,name='catering'),
]