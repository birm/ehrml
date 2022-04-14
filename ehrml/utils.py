# utilities which are not exposed to the user

def readTime(s):
    if s:
        fs = "%Y-%m-%dT%H:%M:%S"
        return datetime.datetime.strptime(s, fs)
    else:
        return s
