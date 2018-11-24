from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
	# ex: /pizza_list/
	path('', views.IndexView.as_view(), name='index'),
	#path('postman/', views.task_list),
	#path('postman/<int:pk>/', views.task_list_detail),
	#path('login/', views.login)
];