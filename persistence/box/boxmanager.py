from __future__ import print_function, unicode_literals
from boxsdk import OAuth2, Client

import persistence.box.boxconfig as boxconfig
from persistence.box.boxfilemanager import BoxFileManager

import logging.config

log = logging.getLogger('debugLogger')

class BoxManager():

    def __init__(self):
        self.auth = OAuth2(
            client_id=boxconfig.CLIENT_ID,
            client_secret=boxconfig.CLIENT_SECRET,
            access_token=boxconfig.ACCESS_TOKEN,
        )
        self._client = None
        self._fm = None

    def _get_client(self):
        if not self._client:
            self._client = Client(self.auth)
            log.debug('Box connection is successfull.')
        return self._client

    def _get_file_manager(self):
        if not self._fm:
            self._fm = BoxFileManager(self._get_client())
        return self._fm

    def upload(self, file_path):
        uploaded_file =self._get_file_manager().upload_file(file_path)
        return uploaded_file

    def download(self, file_id, to_download_path):
        self._get_file_manager().upload_file(file_id, to_download_path)

