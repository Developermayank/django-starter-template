from ninja import NinjaAPI
from ninja.security import django_auth_superuser, django_auth
from ninja.throttling import AnonRateThrottle, UserRateThrottle, AuthRateThrottle
from decouple import config
from django.conf import settings

project_name = config('PROJECT_NAME', default='')

options = {
    'openapi_url': '/openapi.json' if settings.DEBUG else None,
    'throttle': [
        AnonRateThrottle(rate='5/s'),
        AuthRateThrottle(rate='10/s'),
        UserRateThrottle(rate='20/s'),
    ]
}

apiV1 = NinjaAPI(title=f"{project_name} API", version="1.0.0", description=f"API for the {project_name} project.", urls_namespace="api", **options)

@apiV1.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

apiPrivate = NinjaAPI(    
                title=f"{project_name} Private API", 
                version="1.0.0", 
                description=f"API for the {project_name} project (Private API).",
                urls_namespace="private_api",
                auth=django_auth_superuser,
                **options
            )