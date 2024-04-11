from zipfile import ZipFile

def extractZip(zip_path, path_to_save):
    with ZipFile(zip_path, 'r') as zip_object:
        zip_object.extractall(path=path_to_save)

if (__name__ == "__main__"):
    extractZip( r"", r"\blocks\Bases\Historico")
