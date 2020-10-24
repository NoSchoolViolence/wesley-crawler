
import config
from .box.boxmanager import BoxManager

import logging.config

log = logging.getLogger('debugLogger')

class CSFManager():
    def __init__(self):
        self._boxmanager= None
        self._awsmanager= None
        self._gdrivemanager= None

    def __get_box_manager(self):
        if not self._boxmanager:
            self._boxmanager = BoxManager()
        return self._boxmanager

    def __get_awss3_manager(self):
        return self._awsmanager

    def __get_gdrive_manager(self):
        return self._gdrivemanager

    def __getCSFManager(self, csf_vendor=None):
        if not csf_vendor:
            csf_vendor = config.APP_CSF_VENDOR

        if csf_vendor == config.APP_CSF_VENDOR_BOX:
            return self.__get_box_manager()
        elif csf_vendor == config.APP_CSF_VENDOR_AWSS3:
            return self.__get_awss3_manager()
        elif csf_vendor == config.APP_CSF_VENDOR_GDRIVE:
            return self.__get_gdrive_manager()
        else:
            return self.__get_box_manager()

    def upload(self, file_path):
        csf = self.__getCSFManager()
        uploaded_file =csf.upload(file_path)
        return uploaded_file

    def download(self, file_id, to_download_path):
        self.__getCSFManager().download(file_id, to_download_path)