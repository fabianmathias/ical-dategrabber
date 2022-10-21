import requests
import pandas
from icalendar import Calendar

urls = ['https://abo.kleiner-kalender.de/ical/c48-feiertage-in-deutschland.ics']

def make_event_list(url: str) -> list:
    event_list = []
    calendar_string = Calendar.from_ical(requests.get(url).text)
    for event in calendar_string.walk("VEVENT"):
            for i in pandas.date_range(start=event.get('dtstart').dt,end=event.get('dtend').dt,freq='d'):
                event_list.append(i.strftime('%Y-%m-%d'))
    return event_list


def blockdates():
    events = []
    for url in urls:
        try:
            events += make_event_list(url)
        except:
            print("Faulty URL: " + url)
    return events
