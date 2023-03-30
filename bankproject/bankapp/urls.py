from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('new_page_view/', views.new_page_view, name='new_page_view'),
    path('new_registration/', views.new_registration, name='new_registration'),
    # path('get-branches/<int:district_id>/',views.get_branches, name='get_branches'),
    # path('get-branches/', views.get_branches, name='get_branches'),

    path('success/',views.success,name='success'),
    path('home/', views.home, name='home'),

    # path('add/', views.person_create_view, name='person_add'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    #
    # path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX
    # path('branch/', views.branch, name='branch'),
]


    # path('', views.new_registration, name='new_registration'),

