from django.contrib import admin
from django.urls import path
from TAScheduler import views  # Import your custom views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication Views
    path('', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.home, name='home'),

    # Role-based Home Pages
    path('home/ta/', views.home_ta, name='home_ta'),  # TA home page
    path('home/instructor/', views.home_instructor, name='home_instructor'),  # Instructor home page

    # Notifications
    path('notifications/clear/', views.clear_notifications, name='clear_notifications'),

    # Course Management
    path('home/managecourse/', views.manage_course, name='manage_course'),
    path('home/managecourse/create/', views.create_course, name='create_course'),
    path('home/managecourse/edit/<str:course_id>/', views.edit_course, name='edit_course'),
    path('home/managecourse/delete/<str:course_id>/', views.delete_course, name='delete_course'),
    path('home/managecourse/assign/<str:course_id>/', views.assign_instructors_to_course, name='assign_instructors_to_course'),

    # Section Management
    path('home/managesection/', views.manage_section, name='manage_section'),
    path('home/managesection/create/', views.create_section, name='create_section'),
    path('home/managesection/edit/<int:section_id>/', views.edit_section, name='edit_section'),
    path('home/managesection/delete/<int:section_id>/', views.delete_section, name='delete_section'),

    # Account Management
    path('home/accountmanagement/', views.account_management, name='account_management'),
    path('home/accountmanagement/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('assign/<int:user_id>/', views.assign_user_role, name='assign_user_role'),
    path('account/assign/<int:user_id>/', views.assign_instructor_to_course_account_dashboard, name='assign_instructor_to_course'),

    # Forgot Password
    path('forgot_password/', views.forgot_password, name='forgot_password'),

path('send_temp_password/', views.send_temp_password, name='send_temp_password'),

]
