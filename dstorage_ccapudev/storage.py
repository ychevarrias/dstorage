from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomStorage(Storage):
    def __init__(self, auth_token=None, bucket=None, service_url=None):
        if not auth_token:
            self._auth_token = settings.DSTORAGE_AUTH_TOKEN
        if not bucket:
            self._bucket = settings.DSTORAGE_BUCKET_NAME
        if not service_url:
            self._service_url = settings.DSTORAGE_SERVICE_URL

    def deconstruct(self):
        """
            Handle field serialization to support migration
        """
        name, path, args, kwargs = \
            super(CustomStorage, self).deconstruct()
        if self._service_email is not None:
            kwargs["auth_token"] = self._auth_token

    def _save(self, name, content):
        pass
