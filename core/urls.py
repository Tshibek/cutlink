from django.urls import path

from . import views
app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('shortcut', views.shortcutCreate, name='create_link'),
    path('<slug>', views.shortcutShow, name='show_link')
]