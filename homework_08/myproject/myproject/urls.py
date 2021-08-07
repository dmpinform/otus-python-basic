"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from picpart.views import index_view, detail_view, about_view, PictureListView, \
    PictureDetailView, PictureUpdateView, PictureDeleteView, PictureCreateView, PictureUpgradeCreateView, \
    PicturePreviewDetailView, PictureUpgradeDeleteView, register, FavoriteView, UserCreateView, AuthView,\
    MyUserLogoutView, ActionView, update_state

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PictureListView.as_view()),
    path('picpart/<int:pk>/', PictureDetailView.as_view(), name="detail"),
    path('picpart/delete/<int:pk>/', PictureDeleteView.as_view()),

    path('picpart/delete_upgrade/<int:pk>/', PictureUpgradeDeleteView.as_view()),

    path('picpart/edit/<int:pk>/', PictureUpdateView.as_view()),
    path('picpart/create/', PictureCreateView.as_view()),

    path('picpart/preview/create/<int:picture_id>/', PictureUpgradeCreateView.as_view(), name="upgrade"),

    path('picpart/preview_picture/<int:pk>/', PicturePreviewDetailView.as_view(), name="picture_preview"),

    path('favorite/', FavoriteView.as_view(), name="favorite"),

    path('about/', about_view),

    path('picpart/action/<int:pk>/', ActionView.as_view()),
    path('picpart/update_state/', update_state),

    path('register/', UserCreateView.as_view(), name='register'),

    path('login/', AuthView.as_view(), name='login'),
    path('logout/', MyUserLogoutView.as_view(), name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
