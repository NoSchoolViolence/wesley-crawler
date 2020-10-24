from __future__ import print_function, unicode_literals
import os
from boxsdk.exception import BoxAPIException

import persistence.box.boxconfig as boxconfig
import persistence.box.boxfolder as boxfolder
import logging.config

log = logging.getLogger('debugLogger')
class BoxFileManager():

    def __init__(self, client):
        self._client = client

    def upload_file(self, file_path):
        '''
		Upload a file to the folder.
        The contents are taken from the given file path, and it will have the given name.
        the uploaded file will take its name from file_path.

        Upload_file upload the file in file_path to folder
        if there is no folder with folder_name, a folder will be created first.

		:param folder_name:
			Upload the file to folder has folder_name
		:type folder_name:
			`unicode` or None
		:param file_path:
			Upload file from file_path
		:type file_path:
			`unicode` or None
		:return:
			A :class:`File` object with the given file id.
    	:rtype:
        	:class:`File`
        '''

        target_folder = boxfolder.get_folder_byname(self._client, boxconfig.BOX_RAW_DATA_FOLDER)
        #target_folder = self._client.folder('0')
        '''get file name from the relative path. /usr/temp/file.csv '''
        file_name=file_path.split('/')[-1]
        try:
            local_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path)
            new_file = target_folder.upload(local_file_path, file_name=file_name)
            log.info('{0}  uploaded: '.format(new_file.get()['name']))
        except BoxAPIException as e:
            log.error('File exists. Updating contents='+local_file_path, exc_info=True)
            file_id = e.context_info['conflicts']['id']
            new_file = self._client.file(file_id).update_contents(local_file_path)
        finally:
            log.debug('Upload Done.')

        return new_file

    def download_file(self, file_id, to_download_path):
        '''
        Download the file; write it to the given stream.
        :param file_id:
            The box id of the :class:`File` object.
        :type file_id:
            `unicode`
        '''

        with open(to_download_path, 'wb') as open_file:
            self._client.file(file_id).download_to(open_file)
            open_file.close()
            log.debug(to_download_path+" is uploaded!")