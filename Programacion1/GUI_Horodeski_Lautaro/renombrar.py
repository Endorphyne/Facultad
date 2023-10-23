import os 
import calendar
from translate import Translator
Translator = Translator(to_lang="sp")
mes = calendar.month_name[1]
directorio = "GUI_Horodeski_Lautaro\meses"
archivos = os.listdir(directorio)
for nombre_archivo in archivos:
    if nombre_archivo.startswith("Enero"):
        pass 
mes = Translator.translate(mes)
print(mes)