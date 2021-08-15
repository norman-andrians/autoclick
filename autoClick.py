# simpel auto click oleh Norman Andrians
# bila belum menginstal python, download di https://python.org/
# simak dan pelajari >:)

# menggunakan module pyautogui
# bila tidak memiliki pyautogui ketik di terminal command: pip install pyautogui
from pyautogui import click
# ini gk perlu sih, cuma mengatur warna text nya saja
# nambahin ini biar keren kek hekel hehe :v
# bila perlu namun belum di install ketik di terminal command: pip install colorama
import colorama
from colorama import Fore, Back, Style
# menggunakan module time untuk mengatur waktu
import time

colorama.init()

# ubah warna
class warna:
	G = '\033[1;32;40m'

print(warna.G + 'Simple Auto Click oleh Norman Andrians')
# jumlah klik
jumlah = int(input("jumlah klik (bilangan bulat): "))
# delay tiap klik dalam detik
delay = float(input("delay tiap klik (detik, bilangan pecahan disarankan. 0 bila tidak perlu): "))
# hitung mundur sebelum memulai dalam detik (bilangan bulat)
timeout = int(input("hitung mundur sebelum memulai (detik hanya bilangan bulat): "))

print('auto click dimulai dalam:')

# memulai hitungan mundur
while timeout > 0:
	print(timeout)
	timeout -= 1
	time.sleep(1)

# memulai auto click
while jumlah > 0:
	click()
	time.sleep(delay)
	jumlah -= 1

print('selesai')

"""
never gonna give you up
never gonna let you down
never gonna turn round and desert you
never gonna make you cry never gonna say goodbye
never gonna tell a lie and hurt you
"""