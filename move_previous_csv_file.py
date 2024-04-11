import os
import re

def movePreviousCsvFile():
    database_path = r"\block\Bases"
    dir_list = os.listdir(database_path)
    for item in dir_list:
        if re.findall(".csv$", item):
            os.rename(
                os.path.join(database_path, item),
                os.path.join(database_path, "Historico", item)
            )

if (__name__ == "__main__"):
    movePreviousCsvFile()