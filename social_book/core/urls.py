from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('import_video', views.import_video, name='import_video'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^delete-post/(?P<post_id>[\w-]+)/$', views.delete_post, name='delete_post'),
]