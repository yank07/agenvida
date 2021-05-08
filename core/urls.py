from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    PropositoList,
    PropositoDetail,
    OracionList,
    OracionDetail,
    MarcacionList,
    MarcacionDetail,
    UserPerfilDetail,
    UserList,
    UserCreate,
    UserDetail,

  
   
)
router = routers.DefaultRouter()




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

   

    path(r'propositos/', PropositoList.as_view()),
    path(r'propositos/<int:pk>/', PropositoDetail.as_view()),
    path(r'oraciones/', OracionList.as_view()),
    path(r'oraciones/<int:pk>/', OracionDetail.as_view()),
    path(r'marcaciones/', MarcacionList.as_view()),
    path(r'marcaciones/<int:pk>/', MarcacionDetail.as_view()),
    path(r'userProfile/', UserPerfilDetail.as_view()),
    path(r'usuarios/', UserList.as_view()),
    path(r'usuario_create/', UserCreate.as_view()),

   # path(r'^users/$', UserList.as_view()),
    path(r'users/<int:pk>/', UserDetail.as_view()),
    

]


urlpatterns = format_suffix_patterns(urlpatterns)
