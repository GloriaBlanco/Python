#####
###
####

from dateutil.easter import easter
from datetime import datetime, date
import emoji

dia = datetime.today().date()
pascoa = easter(dia.year)
diahoje = date.today()

print(diahoje)
print(pascoa)
print(dia)

if dia == pascoa and dia == diahoje:
    emojic = emoji.emojize(':rabbit_face:')
    # site de emojis http://www.webfx.com/tools/emoji-cheat-sheet/
    print("Feliz Pascoa 🙏  💝 ", emojic)
                  