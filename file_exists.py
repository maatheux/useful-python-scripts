from os.path import exists, expanduser

expandeduser = expanduser('~')

def fileExists(path):
    return exists(r"{}\{}".format(expandeduser, path))

if (__name__ == "__main__"):
    fileExists(r"Downloads\{}".format("**nome-zip**"))