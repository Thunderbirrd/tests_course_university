import os


class FileGetter:
    @staticmethod
    def get_files(path):
        encrypting_files = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                encrypting_files.append(path + "/" + filename)
        return encrypting_files
