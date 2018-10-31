"""dy_research_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
import xadmin
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from template.views import TemplateViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')
router.register(r'template', TemplateViewSet, base_name='template')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title='研究系统', )),#(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    url(r'^jwt_auth', obtain_jwt_token)
]
