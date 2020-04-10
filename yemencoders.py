# Yemen Coders
# Created by Eng: Abdulsalam ALROAS on 10/4/2020.
# Copyright © 2020  www.kodatik.com . All rights reserved.

from bs4 import BeautifulSoup
import re
import time
import requests


with open("udemy.txt", "r") as f:
  for line in f:
    stripped_line = line.strip()
    url = stripped_line
    
    quote_page = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    html = quote_page.content
    soup = BeautifulSoup(html, 'html.parser')


    title_box = soup.find('h1', attrs={'class': 'clp-lead__title'})
    title = re.sub(r'\n\s*\n', r'\n', title_box.get_text().strip(), flags=re.M)

    save_file = open(title+'.txt', 'w+')
    save_file.write(title + "\n")

    Sub_box = soup.find('div', attrs={'class': 'clp-lead__headline'})
    Sub = re.sub(r'\n\s*\n', r'\n', Sub_box.get_text().strip(), flags=re.M)
    save_file.write(Sub + "\n")
   


    expiration_box = soup.find('div', attrs={'class': 'discount-expiration ud-component--clp--discount-expiration'})
    expiration = expiration_box.get_text().strip().split(' ')[:2]
    save_file.write("Discount Expire in: " + ' '.join(expiration) + "\n")


    info_box = soup.findAll('span', attrs={'class': 'incentives__text'})
    save_file.write("This course includes: \n")

    for info in info_box:
        info_elements = re.sub(r'\n\s*\n', r'\n',info.get_text().strip(), flags=re.M)
        save_file.write(" - " + info_elements + "\n")

    
    rating_box = soup.find('span', attrs={'class': 'tooltip-container'})
    rating = re.sub(r'\n\s*\n', r'\n', rating_box.text.strip().split('\n')[0], flags = re.M)
    ratingCount = re.sub(r'\n\s*\n', r'\n',rating_box.text.strip().split('\n')[1], flags=re.M)
    save_file.write("Rating: " + rating + " " + ratingCount + "\n")
 



    enrollment_box = soup.find('div', attrs={'data-purpose': 'enrollment'})
    enrollment = re.sub(r'\n\s*\n', r'\n',enrollment_box.get_text().strip().split(' ')[0], flags=re.M)
    save_file.write("Enrolled Students: " + enrollment + "\n")

    
    

    update_box = soup.find('div', attrs={'class': 'last-update-date'})
    update = re.sub(r'\n\s*\n', r'\n', update_box.get_text().strip().split(' ')[2], flags=re.M)
    save_file.write("Last Update: " + update + "\n")
   
    
    

    language_box = soup.find('div', attrs={'class': 'clp-lead__language'})
    language = re.sub(r'\n\s*\n', r'\n', language_box.get_text().strip(), flags=re.M)
    save_file.write("Language & Subtitle: " )
    save_file.write(language + "\n")
  
    
    
    save_file.write("URL: ")
    save_file.write(url + "\n\n")


    save_file.write("Yemen Coders \n شارك رابط المجموعة ليستفيد غيرك \n مجموعة متخصصه في التكنولوجيا والبرمجة و  نشر دورات مجانية \n مجموعة الوتساب \n https://chat.whatsapp.com/HsTXazA9nhdC1Ar6kjvVD2 \n مجموعة التليجرام \n لمشاهدة الرسائل السابقة انضم إلى مجموعة التليجرام \n https://t.me/yemencoders \n")
   
    save_file.close()
    print(stripped_line)
    time.sleep(60)
print("Done")
