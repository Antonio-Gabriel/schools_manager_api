import filetype


class FileTypeAdapter:
    @classmethod
    def is_excel_file(cls, file):
        """check if the file uploaded is valid or not"""

        content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        try:
            filetype.guess(file)
            if filetype.guess(file).mime == content_type:
                return True
        except:
            ...

        return False
