from django.urls import path
from . import views

#33389
app_name = "main"

urlpatterns = [
	
	path('', views.index, name="index"),

	]