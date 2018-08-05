
from bs4 import BeautifulSoup
import requests
import csv


quelle = requests.get('http://coreyms.com/').text

soup = BeautifulSoup(quelle, 'lxml')

from bs4 import BeautifulSoup
import requests

quelle = requests.get('http://coreyms.com/').text

suppe = BeautifulSoup(quelle, 'lxml')
# print(suppe.prettify())

# artikel = suppe.find_all('article')
# print(artikel.prettify())

csv_datei = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_datei)
csv_writer.writerow(['Titel', 'Beschreibung', 'Video_Link'])

for artikel in suppe.find_all('article'):

    titel = artikel.h2.a.text.encode('utf-8')
    print(titel)

    beschreibung = artikel.find('div', class_='entry-content').p.text.encode('utf-8')
    print(beschreibung)

    try:
        video_quelle = suppe.find('iframe', class_='youtube-player')['src'].encode('utf-8')
        # print(video_quele)
        video_quelle = video_quelle.split('/')[4]
        vid_id = video_quelle.split('?')[0]
        # print(video_quelle)
        # print(vid_id)
        youtube_link = 'http://www.youtube.com/watch?v={}'.format(vid_id)
    except Exception as e:
        youtube_link = None
    print(youtube_link)

    print(" ")

    csv_writer.writerow([titel, beschreibung, youtube_link])

csv_datei.close()