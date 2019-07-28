import locale
import calendar

URLS = [
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mercato/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/raemi59/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mercato-abend/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/zentrum-mensa/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/cafeteria-uzh-plattenstrasse/{}.html",
    "https://www.mensa.uzh.ch/de/menueplaene/lichthof-rondell/{}.html",
]

# GERMAN DAYS
locale.setlocale(locale.LC_ALL, "de_DE")

DAYS = list(calendar.day_name)
WORKDAYS = DAYS[:5]
