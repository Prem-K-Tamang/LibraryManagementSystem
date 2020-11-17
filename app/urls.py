from django.urls import path
from . import views


urlpatterns  = [
    path('', views.dashboard, name ='dashboard'),

    path('books/', views.list_book, name = 'list_book'),
    path('books/new/', views.create_book, name = 'create_book'),
    path('books/update/<str:pk>/', views.update_book, name = 'update_book'),
    path('books/delete/<str:pk>/', views.delete_book, name = 'delete_book'),

    path('faculties/', views.list_faculty, name = 'list_faculty'),
    path('faculties/new/', views.create_faculty, name = 'create_faculty'),
    path('faculties/update/<str:pk>/', views.update_faculty, name = 'update_faculty'),
    path('faculties/delete/<str:pk>/', views.delete_faculty, name = 'delete_faculty'),

    path('semesters/', views.list_semester, name = 'list_semester'),
    path('semesters/new/', views.create_semester, name = 'create_semester'),
    path('semesters/delete/<str:pk>/', views.delete_semester, name = 'delete_semester'),

    path('students/', views.list_student, name = 'list_student'),
    path('students/new/', views.create_student, name = 'create_student'),
    path('students/update/<str:student_id>/', views.update_student, name = 'update_student'),
    path('students/delete/<str:student_id>/', views.delete_student, name = 'delete_student'),
    # path('students/select-faculty/', views.select_faculty, name = 'select_faculty'),


    path('cards/', views.cards, name='cards'),
    path('gate-pass/', views.gate_pass, name="gate_pass"),
    path('gate-pass/create/', views.create_gate_pass, name='create_gate_pass'),
    path('gate-pass/delete/<str:pk>/', views.delete_gate_pass, name='delete_gate_pass'),


    path('issued/', views.list_issued, name='list_issued'),
    path('issued/create/', views.create_issue, name = 'create_issue'),
    path('issued/delete<str:pk>/', views.delete_issue, name='delete_issue'),
    path('issued/due-about-to-expire/', views.due_about_to_expire, name='due_about_to_expire'),

    path('returend/', views.list_returned, name = 'list_returned'),
    path('returned/create/', views.create_return, name='create_return'),
    path('returned/delete/<str:pk>/', views.delete_return, name='delete_return'),
    

]