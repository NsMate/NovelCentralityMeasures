

class FileHandling:

    def __init__(self, file_name):
        self.file_name = file_name

    def open_for_write(self):
        self.file = open(str(self.file_name), 'w', encoding='utf-8')

    def write_to_file(self, string):
        self.file.write(string)

    def close_file(self):
        self.file.close()

