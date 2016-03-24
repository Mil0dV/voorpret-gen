def lineup_parser(file_path):
    # leest strings in lijst, split op hardreturns, negeert blank lines, en lowercased strings
    # returns list of artists as strings
    result = []
    with open(file_path) as f_in:
        lines = (line.rstrip() for line in f_in)
        lines = list(line for line in lines if line)
        for x in lines:
            result.append(x.lower())
        print 'lines ==' , result

    return result

def read_settings(file_path):
    # reads ini file and returns variables in a list of strings
    docum = open(file_path)
    lines = docum.readlines()
    result = []
    for x in lines:
        if x[0] == "[":
            next
        else: result.append(x.split('=')[1])
    return result
