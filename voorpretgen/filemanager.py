def lineup_parser(file_path):
    result = []
    with open(file_path) as f_in:
        lines = (line.rstrip() for line in f_in)
        lines = list(line for line in lines if line)
        for x in lines:
            result.append(x.lower())
        print 'lines ==' , result

    return result
