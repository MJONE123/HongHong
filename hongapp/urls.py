from django.urls import path
from . import views  # 현재위치의 viwes.py 가져오기

urlpatterns = [

    path("cafe/", views.cafe),
    path("total/", views.total),
    path("main/", views.main),
    path("", views.main),
    path("geo/", views.geo),
    path("map/", views.map),
    path("pcjoin/", views.pcjoin),
    path("pclogin/", views.pclogin),
    path("lostidpw/", views.lostidpw),
    path("map_front/", views.map_front),
    path("map_back/", views.map_back),
    path("map_big/", views.map_big),
    path("map_gugiback/", views.map_gugiback),
    path("map_jochi/", views.map_jochi),
    path("userag/", views.userag),
    path("privacy/", views.privacy),
    path("adsform/", views.adsform),

    # path('user/signup/', views.user_signup),
]
