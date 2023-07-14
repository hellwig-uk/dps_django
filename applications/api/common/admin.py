"""
Convinience function to just register all the models within an app.
"""

from django.apps import apps
from django.contrib import admin
from django.db.models.fields.reverse_related import ManyToOneRel


def _model_admin_factory(model):
    hidden_fields = []
    # pylint: disable= W0212 # _meta is the preferred api.
    for field in model._meta.get_fields():
        if isinstance(field, ManyToOneRel):
            continue

        if hasattr(field, "primary_key") and field.primary_key:
            hidden_fields.append(field.name)
        elif not field.editable:
            hidden_fields.append(field.name)

    if "dts_archived" in hidden_fields:
        hidden_fields.remove("dts_archived")

    class ModelAdmin(admin.ModelAdmin):
        readonly_fields = hidden_fields

    return ModelAdmin


def register_models_by_appconfig(config):
    app_name = config.name.split(".")[-1]
    for model in apps.get_app_config(app_name).get_models():
        admin.site.register(model, _model_admin_factory(model))
