from html.parser import HTMLParser
import re

class KeyDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found_td = True
        self.found_td_data = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if re.match('td', tag) and 'm' in d.get('class', 'm'):
            self.found_td = True
        if re.match('td', tag) and 's' in d.get('class', 's'):
            self.found_td = True
        if re.match('td', tag) and 'a' in d.get('class', 'm'):
            self.found_td = True

    def handle_data(self, data):
        if self.found_td:
            self.found_td_data.append(data)
            self.found_td = False

    def feed(self, content):
        super().feed(content)
