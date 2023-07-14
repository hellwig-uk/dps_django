"""
Define default_app_config here so that we can just register this app as
applications.<appname>
The config is actually just called config, which makes it easier to use common
techniques like registering default admin models.
"""

# pylint: disable=C0103
default_app_config = "applications.api.apps.Config"
