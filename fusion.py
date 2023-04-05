import subprocess
import os
import glob

ruta_ffmpeg = 'D:\\ffmpeg\\bin\\ffmpeg.exe'
carpeta_videos_audios = r'D:\mis_videos'
carpeta_salida_fusion = r'D:\mis_videos\salida'

# Obtener los archivos de la carpeta
archivos = os.listdir(carpeta_videos_audios)
prefijos = []  # Lista de prefijos de los archivos de video ejm: [2, 3, "9b", 10, 14, 15, 16, "16b", 21, 22]

# Leemos los archivos .mp4 y obtenemos los prefijos
for archivo in archivos:
    if archivo.endswith('.mp4'):
        prefijo = archivo.split('-')[0]
        if prefijo not in prefijos:
            prefijos.append(prefijo)

# Procedemos a fusionar a goku y vegeta
for i in prefijos:
    archivo_video = glob.glob(os.path.join(carpeta_videos_audios, f"{i}-*.mp4"))[0]
    nombre_archivo_video = os.path.splitext(os.path.basename(archivo_video))[0]
    # cadena_sin_subcadena = cadena.replace("(720p with 30fps)", "")
    nombre_archivo_video = nombre_archivo_video.replace("(720p with 30fps)", "")
    archivo_audio = glob.glob(os.path.join(carpeta_videos_audios, f"{i}-*-audio.mp4"))[0]
    archivo_salida = os.path.join(carpeta_salida_fusion, f"{nombre_archivo_video}.mp4")
    # invocamos a ffmpeg para la fusion
    subprocess.run(f"{ruta_ffmpeg} -i \"{archivo_video}\" -i \"{archivo_audio}\" -c:v copy -c:a copy \"{archivo_salida}\"")
