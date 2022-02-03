import time
import pyautogui
from lxml import html
import requests
import datetime

page = requests.get('https://namazvakitleri.diyanet.gov.tr/tr-TR/9206/ankara-icin-namaz-vakti') #URL
tree = html.fromstring(page.content)
buyers = tree.xpath('//div[@class="tpt-time"]/text()') #Verimizi Çektik
imsak = buyers[0]
ogle = buyers[2]
ikindi = buyers[3]
aksam = buyers[4]
yatsi = buyers[5]

imsak = "03:49"

while True:
    an = datetime.datetime.now()
    if imsak==(an.strftime("%H:%M")): #Ezan saati ile güncel saat kıyaslandı
        pyautogui.press('volumemute') #Bilgisayarın sesini kapatıyoruz
        time.sleep(200) #Ezanın bitmesi için tahmini süreler tanımlandı
        pyautogui.press('volumeup')
    elif ogle==(an.strftime("%H:%M")):
       pyautogui.press('volumemute')
       time.sleep(120)
       pyautogui.press('volumeup')
    elif ikindi==(an.strftime("%H:%M")):
       pyautogui.press('volumemute')
       time.sleep(120)
       pyautogui.press('volumeup')
    elif aksam==(an.strftime("%H:%M")):
       pyautogui.press('volumemute')
       time.sleep(120)
       pyautogui.press('volumeup')
    elif yatsi == (an.strftime("%H:%M")):
       pyautogui.press('volumemute')
       time.sleep(120)
       pyautogui.press('volumeup')


