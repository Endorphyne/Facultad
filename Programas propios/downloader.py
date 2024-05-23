from pytube import YouTube
import os

def descargar_video(url, carpeta_destino):
    # Crea un objeto YouTube con la URL del video
    youtube = YouTube(url)

    # Descarga el video
    video = youtube.streams.get_highest_resolution()
    video.download(output_path=carpeta_destino)

def descargar_audio(url, carpeta_destino):
    # Crea un objeto YouTube con la URL del video
    youtube = YouTube(url)

    # Descarga el audio
    audio = youtube.streams.get_audio_only()
    audio.download(output_path=carpeta_destino)

# URL del video de YouTube que quieres descargar
url = input("Ingrese la URL")  # Reemplaza esto con la URL de tu video

# Carpeta de destino donde quieres guardar el video y el audio
carpeta_destino_video = os.path.join(os.getcwd(), "videos")  # Reemplaza esto con la ruta de tu carpeta de destino para el video
carpeta_destino_audio = os.path.join(os.getcwd(), "audios")  # Reemplaza esto con la ruta de tu carpeta de destino para el audio

descargar_video(url, carpeta_destino_video)
descargar_audio(url, carpeta_destino_audio)
