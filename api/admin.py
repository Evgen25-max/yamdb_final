from django.apps import apps
from django.contrib import admin

api = apps.get_app_config('api')
models = api.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        continue
