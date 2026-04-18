from ninja import NinjaAPI
from ninja.security import django_auth_superuser, django_auth
from ninja.throttling import AnonRateThrottle, UserRateThrottle, AuthRateThrottle
from django.conf import settings

options = {
    'openapi_url': '/openapi.json' if settings.DEBUG else None,
    'throttle': [
        AnonRateThrottle(rate='5/s'),
        AuthRateThrottle(rate='10/s'),
        UserRateThrottle(rate='20/s'),
    ]
}

apiV1 = NinjaAPI(title=f"Public API", version="1.0.0", description=f"Public API for the your project.", urls_namespace="api", **options)

@apiV1.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

apiPrivate = NinjaAPI(    
    title=f"Private API", 
    version="1.0.0", 
    description=f"Private API for your project (Private API).",
    urls_namespace="private_api",
    auth=django_auth_superuser,
    **options
)