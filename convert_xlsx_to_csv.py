import pandas as pd

def convertXlsxToCsv(file_path, path_to_save):
    read_file = pd.read_excel(file_path)

    read_file.to_csv(path_to_save, index=None, header=True, sep=';')

if (__name__ == "__main__"):
    convertXlsxToCsv(
        r"\Historico\block_221231.xlsx",
        r"\Bases\block_221231.csv"
    )