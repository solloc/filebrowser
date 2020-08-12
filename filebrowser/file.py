""" file model for browser """

import os
import random

class File:
    """ file model class """

    def __init__(self):
        self._root_dir = ''
        self._files = []
        self._current_file_index = 0

    def _get_root_dir(self):
        return self._root_dir
    def _set_root_dir(self, root_dir):
        self._root_dir = root_dir
        print('root dir: ' + str(self._root_dir))
        self._analyze_dir()

    root_dir = property(None, _set_root_dir)

    def _analyze_dir(self):
        self._files = []
        self._scan_dir(self._root_dir)

    def _scan_dir(self, target_directory):
        with os.scandir(target_directory) as it:
            for entry in it:
                if entry.is_file():
                    file_name = (os.path.join(target_directory, entry.name))
                    self._files.append(file_name)
                elif entry.is_dir():
                    self._scan_dir(os.path.join(target_directory, entry.name))

    def next(self):
        self._current_file_index = random.randrange(0, len(self._files)-1)

    def get_current_file(self):
        return self._files[self._current_file_index]

    def get_current_file_number(self):
        """ returns current file index + 1 """
        return self._current_file_index + 1

    def get_total_file_number(self):
        return len(self._files)
