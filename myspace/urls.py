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
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import SimpleRouter
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from article.views import ArticleListViewSet
from users.views import UserViewSet, SMSCodeViewSet, QqLogin, QQInfo,QQBindViewSet
from homepic.views import HomePicViewSet, DanmuView
from comment.views import CommentViewSet

router = SimpleRouter()
router.register('artical', ArticleListViewSet, base_name='artical'),
router.register('send_code', SMSCodeViewSet, base_name='send_code'),
router.register('user', UserViewSet, base_name='user'),
router.register('homepic', HomePicViewSet, base_name='homepic'),
router.register('comment', CommentViewSet, base_name='comment'),
router.register('qqbind', QQBindViewSet, base_name='qqbind'),

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('web/', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('docs/', include_docs_urls(title='梦落无声')),
    path('web/login', obtain_jwt_token),  # JWT认证
    path('web/danmu', DanmuView.as_view()),
    path('web/qqlogin', QqLogin.as_view()),
    path('web/qqinfo', QQInfo.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
