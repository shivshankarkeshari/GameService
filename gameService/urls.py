

from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


version = "v1"
schema_view = get_schema_view(
   openapi.Info(
      title="gameApp API Documentation",
      default_version=version,
      contact=openapi.Contact(email="shiv.s.keshari@gmail.com"),
    #   description="description-->",
    #   terms_of_service="terms_of_service-->",
    #   license=openapi.License(name="SSK License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"api/{version}/",
        include([
                path('', include("gameApp.urls")),
                re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
            ]
        )
    ),
]
