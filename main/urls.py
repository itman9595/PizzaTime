from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
	# ex: /pizza_list/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /pizza_list/postman/
	path('postman/', views.pizza_list),
	# ex: /pizza_list/postman/<int:pk>/
	path('postman/<int:pk>/', views.pizza_list_detail),
	# ex: /pizza_list/login/
	path('login/', views.login)
];