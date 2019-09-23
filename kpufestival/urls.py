from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import info.views

'''
handler404 = info.views.handler404
handler500 = info.views.handler500
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info.views.home,name="home"),

    # URL을 연결하기 위한 import 부분
    path('account/',include('account.urls')),
    path('board/',include('board.urls')),
    path('info/',include('info.urls')),
    path('intro/',include('intro.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
