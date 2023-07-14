"""
Common views with the most important being the DeveloperServer view, this works
sort of like a normal webserver, however it is slow and not secure so only use
it for local development.
"""
import pathlib

from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView
from django.views.static import directory_index


class DeveloperServer(View):
    def get(self, request, *args, **kwargs):
        relative = pathlib.PurePath(request.path).relative_to("/")
        absolute = pathlib.Path(settings.STATIC_ROOT.parent) / relative
        index = absolute / "index.html"

        if not absolute.exists():
            message = f"404; Path not found: {relative}, {args}, {kwargs}"
            return HttpResponseNotFound(message)

        if absolute.is_file():
            return FileResponse(open(str(absolute), "rb"))

        if index.exists():
            return FileResponse(open(str(index), "rb"))

        return directory_index(str(relative), absolute)


class APIRootIndex(TemplateView):
    template_name = "base.tmp"
    patterns = []
    auth_urls = [
        ["Authentication:Login", "auth/login/"],
        ["Authentication:Logout", "auth/logout/"],
        ["Authentication:Password:Reset", "auth/password/reset/"],
        [
            "Authentication:Password:Reset:Confirm",
            "auth/password/reset/confirm/",
        ],
        ["Authentication:Password:Change", "auth/password/change/"],
        ["Authentication:User", "auth/user/"],
        #  ["Authentication:Token:Verify", "auth/token/verify/"],
        #  ["Authentication:Token:Refresh", "auth/token/refresh/"],
    ]

    def get_context_data(self, *args, **kwargs):
        app_urls = []
        for _ in self.patterns:
            app_urls.append(
                [_.app_name.split(".")[1], str(_.pattern)],
            )
        context = super().get_context_data(*args, **kwargs)
        context["auth_urls"] = self.auth_urls
        context["app_urls"] = app_urls
        return context
