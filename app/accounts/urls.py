from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users_ext', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^users/$', views.Userslist.as_view(), name='users')
]
