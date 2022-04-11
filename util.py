def underline(text):
    n = len(text)
    text_u = "{:s}\n{:s}\n".format(text, 2 * n * "-")

    return text_u


def box(text):
    n = len(text)
    lines = f"{2*n*'='}"
    text_u = "{:s}\n{:s}\n{:s}\n".format(lines, f"|{text}|", lines)

    return text_u


def close(a, b, range):
    smallest = min(a, b)
    return abs(a - b) / smallest <= range
