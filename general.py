import locale
import calendar

URLS = [
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mercato/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mensa/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/raemi59/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/platte-14/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/lichthof-rondell/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/cafeteria-zzm/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mercato-abend/{}.html",
]

# GERMAN DAYS
locale.setlocale(locale.LC_ALL, "de_DE")

DAYS = list(calendar.day_name)
WORKDAYS = DAYS[:5]


RANGE = 0.1
