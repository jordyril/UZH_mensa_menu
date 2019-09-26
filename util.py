def underline(text):
    n = len(text)
    text_u = "{:s}\n{:s}\n".format(text, n * "-")

    return text_u


def box(text):
    n = len(text)
    lines = (n + 2) * "-"
    text_u = "{:s}\n{:s}\n{:s}\n".format(lines, f"|{text}|", lines)

    return text_u


def close(a, b, range):
    smallest = min(a, b)
    return abs(a - b) / smallest <= range
