''' An old, true, and sordid tale of Python
    featuring raisins, pushy relatives, checkerboards,
    business cards, web pages, and getting
    much needed rest.
'''

from urllib.request import urlopen
from urllib.parse import urlencode
import csv

def make_vcard(fname, lname, title, phone, email):
    'Create an electronic business card in a VCard 2.1 format'
    return vcard_template.format(fname=fname, lname=lname, title=title, phone=phone, email=email)


vcard_template = '''BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Raisins R Us, Inc.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:{email}
REV:20181031T195243Z
END:VCARD
'''

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> {fname} {lname} </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> {fname} {lname} </em> </h1>
<hr>
<dl>
    <dt> Full name </dt>            <dd> {fname} {lname} </dd>
    <dt> Job time </dt>             <dd> {title} </dd>
    <dt> Work phone </dt>           <dd> {phone} </dd>
</dl>
</body>
</html>
'''

with open('notes/raisin_team_update.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        basename = email.replace('@', '_at_').replace('.', '_dot_')

        vcard = make_vcard(fname, lname, title, phone, email)
        filename = f'{basename}.vcf'
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard)
        print(f'Wrote: {filename}')

        html = html_template.format(fname=fname, lname=lname, title=title, phone=phone, email=email)
        filename = f'{basename}.html'
        with open(filename, 'w') as html_file:
            html_file.write(html)
        print(f'Wrote: {filename}')

        # QR Code from the Google Chart REST API documented at:
        # https://developers.google.com/chart/infographics/docs/qr_codes
        qr_url = 'https://chart.googleapis.com/chart?'
        query = dict(cht='qr', chs='300x300', chl=vcard)
        url = qr_url + urlencode(query)
        with urlopen(url) as u:
            image = u.read()

        filename = f'{basename}.png'
        with open(filename, 'wb') as image_file:
            image_file.write(image)
        print(f'Wrote: {filename}')
    



