from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start : '+tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
        print('End   : '+tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty : '+tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

n = int(input())
html_code = ""
for i in range(n):
    html_code += input()

parser = MyHTMLParser()
parser.feed(html_code)
