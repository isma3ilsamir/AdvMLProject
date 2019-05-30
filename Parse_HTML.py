import os
from bs4 import BeautifulSoup
import csv
import re
from multiprocessing import Pool
import glob
import timeit


def mp_handler():

    csv_file = open('output.csv', 'w+', encoding='utf8')
    csv_writer = csv.writer(csv_file, delimiter='|', lineterminator = '\n')
    csv_writer.writerow(['article_id', 'text', 'eurovoc_label'])

    p = Pool()
    files = glob.glob('*.html')
    with open('output.csv', 'a+', encoding='utf8') as f:
        for result in p.imap(process_file, files):
            f.write('{}.\n' .format(result))

def process_file(file):
    with open(file, encoding='utf8') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    # title = soup.find('div', class_ ='tabContent')
    # title = '' if title is None else title.h1.text
    # title = re.sub('\s+', ' ', title).strip().replace(',', ' ')

    title = soup.find('div', class_='PageTitle')
    title = '' if title is None else title.h1.text
    title = re.sub('\s+', ' ', title).strip()

    #lang = '' if soup.find('div',id='PPAuth_Contents') is None else soup.find('div',id='PPAuth_Contents')

    eurovoc = soup.find('div',id='PPClass_Contents')
    eurovoc = '' if eurovoc is None else eurovoc.dd.text
    eurovoc = re.sub('\s+', ' ', eurovoc).strip()

    text = soup.find('div',id='TexteOnly')
    text = '' if text is None else text.text
    text = re.sub('\s+', ' ', text).strip().replace(',',' ')

    line = title + '|' + text + '|' + eurovoc
    return line

    #dates = '' if soup.find('div',id='PPDates_Contents') is None else soup.find('div',id='PPDates_Contents')

    #print(lang.dd.text , dates.dl.text , eurovoc.dd.text, text.div.text)


if __name__ == '__main__':

    start = timeit.default_timer()

    HTML_folder = 'C:/Users/Ismail/Desktop/OVGU/DKE Subjects/Machine Learning 2/Project/sample1/'
    #HTML_folder = 'C:/Users/Ismail/Desktop/OVGU/DKE Subjects/Machine Learning 2/Project/HTML files/'
    os.chdir(HTML_folder)

    mp_handler()

    stop = timeit.default_timer()
    print('Time: ', stop - start)