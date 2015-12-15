from bs4 import BeautifulSoup as BS
# import urllib3
import lxml
import time

INPUT_FOLDER = '../data/'
FILE_NAME = 'genome3TransposonData'
OUT_FILE_NAME = 'g3'
ext = '.html'

def main():
    with open(INPUT_FOLDER + FILE_NAME + ext, 'r') as infile:
        out = infile.read() # take raw html file
    soup = BS(out, "lxml")
    dataTables = soup.find_all('table')
    with open(INPUT_FOLDER + OUT_FILE_NAME + ext, 'w+') as outfile:
        outfile.write('\n\n'.join(map(str, dataTables)))
    print("Done")


def scrapeNutrition(link):
    http = urllib3.PoolManager()
    req = http.request('GET', link)
    page = req.data
    soup = BS(page, "lxml")
    name = soup.find('div', attrs={"align": "left"}).text.strip()
    if not name:
        print('NULL ENTRY:', link)
        name = 'NULL ENTRY: ' + link
    s = lambda x: x.string.strip().replace('\n', '') if x.string else x.string
    desc = lambda x: [ s(el) for el in x if s(el) ]
    td = soup.find_all('table')
    if len(td) <= 2: #no nutrition has two td
        return [ ['Name', name] ]
    par = soup.find_all('p')
    for p in par: p.unwrap()  # remove pesky paragraphs along cals and such
    for item in td:
        if item.li:
            item.li.unwrap()  # remove those stupid calcium list shit i.e. at td[30]
    c = [ desc(child) for child in td if desc(child) ]
    dd = handleCalHeader(c[0]) + c[5:-1] # remove junk (allergens is c[-1])
    pIds = [4,6,8,10,14,17] # percentages were at 2,4,6,8, 12, 15 before swap
    pfunc = lambda x: [x-1, x]
    pairs = [pfunc(p) for p in pIds]
    for p,c in pairs:
        if c >= len(dd):
            print('ERROR with item', dd)
            continue
        dd[c] = makePercentageKeyValPair(dd[p], dd[c])
    dd = [ ['Name', name ] ] + dd
    return dd

if __name__ == '__main__':
    main()