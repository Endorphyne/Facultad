from pytube import YouTube
def descargarVideo(url,destino):
    try:
        print(f"Intentando descargar {url} en {destino}")
        YouTube(url).streams.first().download(destino)
    except:
        print("Decarga Fallida")
    print(f"Descarga Realizada en {destino}")
def descargarAudio(url,destino):
    try:
        print(f"Intentando descargar {url} en {destino}")
        YouTube(url).streams.filter(only_audio=True).first().download(destino)
    except:
        print("Decarga Fallida")
    print(f"Descarga Realizada en {destino}")
url = "FORMATO"
destino = input("Ingrese la carpeta de destino: \n")
while url.upper() != "SALIR" :
    if url.upper() == "FORMATO":
        try:
            eleccion = input("Ingrese que formato desea descargar: \n 1: Video \n 2: Audio \n :")
            eleccion == "1" or eleccion == "2"
        except:
            eleccion = input("Ingrese que formato desea descargar: \n 1: Video \n 2: Audio \n (VALOR INGRESADO INVALIDO)\n :")
    if eleccion == "1":
        try:
            print("Ingrese la url del video o SALIR (Ingrese FORMATO para cambiar de formato): \n")
            url = input()
            url.upper() != "FORMATO"
            descargarVideo(url,destino)
        except:
            print("Lero lero candelero")
    elif eleccion == "2": 
        try:
            print("Ingrese la url del video o SALIR (Ingrese FORMATO para cambiar de formato): \n")
            url = input()
            url.upper() != "FORMATO"
            descargarAudio(url,destino)
        except:
            print("Lero lero candelero")