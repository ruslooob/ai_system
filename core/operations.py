# НЕ---------------
def not_zade(y):
    return 1 - y


def not_sugeno(y, lmd):
    return (1 - y) / (1 + lmd * y)


# И---------------
def t_min(y1, y2):
    return min(y1, y2)


def t_prod(y1, y2):
    return y1 * y2


def t_max(y1, y2):
    return max(0, y1 + y2 - 1)


def t_drastic(y1, y2):
    if y1 == 1:
        return y2
    elif y2 == 1:
        return y1
    return 0


# ИЛИ---------------

def s_max(y1, y2):
    return max(y1, y2)


def s_sum(y1, y2):
    return y1 + y2 - y1 * y2


def s_min(y1, y2):
    return min(y1 + y2, 1)


def s_drastic(y1, y2):
    if y1 == 0:
        return y2
    elif y2 == 0:
        return y1
    return 1
