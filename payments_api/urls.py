"""
URL configuration for payments_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import permissions
from django.conf.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView



# Schema View config
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Payments API",
#         default_version='v1',
#         description="API documentation for Paystack Payments",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="support@example.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('payments.urls')),

    # Schema (raw OpenAPI json)
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI (beautiful interactive docs)
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc (alternative beautiful docs)
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
