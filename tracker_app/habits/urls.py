"""habits URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import path 
from . import views


urlpatterns =[ 
# 1) list of a user's habits
path('', views.habit_list, name = 'habit_list'),
# 2) a more detailed view of a specific habit (needs a pk)
path('<int:pk>/', views.habit_detail, name='habit_detail'),
# 3) a view for adding a habit
path('create/', views.habit_new, name='habit_new'),
# 4) a view for updating a habit (requires a primary key)
path('update/<int:pk>/', views.habit_edit, name='habit_edit'),
# 5) a view for deleting a habit (requires a primary key)
path('delete/<int:pk>/', views.habit_delete, name='habit_delete'),
]

