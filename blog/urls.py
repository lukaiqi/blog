"""smallsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from article.views import ArticleViewSet, ArticleTypeViewSet
from users.views import UserViewSet, CodeViewSet, QQLogin, OauthBindViewSet, WbLogin
from client.views import ClientViewSet
router = SimpleRouter()
router.register('article', ArticleViewSet, basename='article'),
router.register('articleType', ArticleTypeViewSet, basename='articleType'),
router.register('sendCode', CodeViewSet, basename='sendCode'),
router.register('user', UserViewSet, basename='user'),
router.register('oauthBind', OauthBindViewSet, basename='oauthBind'),
router.register('client', ClientViewSet, basename='client'),

urlpatterns = [
    path('', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/login', obtain_jwt_token),  # JWT认证
    path('api/qqlogin', QQLogin.as_view()),
    path('api/wblogin', WbLogin.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
