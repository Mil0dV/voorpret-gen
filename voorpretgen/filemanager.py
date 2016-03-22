def readlines(file_path):
    # todo size check -> > X KB -> error
    l = open(file_path)
    # todo regex om newlines eruit te slopen
    return l.readlines()
