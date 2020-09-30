def make_readable(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    seconds -= minutes * 60
    minutes -= hours * 60
    res = str(hours).rjust(2,'0') + ":" + str(minutes).rjust(2,'0') + ":" + str(seconds).rjust(2,'0')
    return res
