from bs4 import BeautifulSoup
import sys
import time

# python assets/scripts/foxnews/html_parse1.py test/test.html


def html_parse1(html, out):
    soup = BeautifulSoup(open(html).read(), 'html.parser')
    for span in soup.find_all('span', attrs={'class', 'js-display-url'}):
        out.write(span.text + '\n')
    # for a in soup.find_all('a', attrs={'class', 'twitter-timeline-link u-hidden'}):
    #     out.write('find something: ')
    #     out.write(a['href'] + '\n')
    out.close()

if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) != 2:
        print 'USAGE: python html_parse1.py <input html>'
        print 'this script will extract all news links in a html file'
    else:
        html = sys.argv[1]
        out = html.replace('.html', '.links1')
        out = open(out, 'w')
        html_parse1(html, out)
    print("--- %s seconds ---" % (time.time() - start_time))