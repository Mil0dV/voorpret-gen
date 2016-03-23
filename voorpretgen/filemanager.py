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
    # reads ini file and returns variables as key-value pairs, where key is type of variable
    docum = open(file_path)
    lines = docum.readlines()
    for x in lines:
        if x[0] == "[":
            lines.remove(x)
    return {'topX':lines[0], 'SPOTIPY_CLIENT_ID':lines[1], 'SPOTIPY_CLIENT_SECRET':lines[2], 'SPOTIPY_REDIRECT_URI':lines[3]}
