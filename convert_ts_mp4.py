import subprocess
import os
import glob

ruta_ffmpeg = 'D:\\ffmpeg\\bin\\ffmpeg.exe'
carpeta_videos_audios = r'D:\Cursos\code-easy'
carpeta_salida_fusion = r'D:\Cursos\code-easy\salida'

# Obtener los archivos de la carpeta
archivos = os.listdir(carpeta_videos_audios)
prefijos = []  # Lista de prefijos de los archivos de video ejm: [2, 3, "9b", 10, 14, 15, 16, "16b", 21, 22]

archivos = sorted(archivos)
# Leemos los archivos .mp4 y obtenemos los prefijos
for archivo in archivos:
    if archivo.endswith('.ts'):
        prefijo = archivo.split('-')[0]
        if prefijo not in prefijos:
            prefijos.append(prefijo)

# Procedemos a convertir el archivo .ts a .mp4
for i in prefijos:
    archivo_video = glob.glob(os.path.join(carpeta_videos_audios, f"{i}-*.ts"))[0]
    nombre_archivo_video = os.path.splitext(os.path.basename(archivo_video))[0]
    # cadena_sin_subcadena = cadena.replace("(720p with 30fps)", "")
    nombre_archivo_video = nombre_archivo_video.replace(" - Curso de React con Typescript-playlist", "")
    archivo_salida = os.path.join(carpeta_salida_fusion, f"{nombre_archivo_video}.mp4")
    # invocamos a ffmpeg para la conversión
    print("\033[32m" + f"Convirtiendo... {archivo_video} --> {archivo_salida}" + "\033[0m")
    subprocess.run(f"{ruta_ffmpeg} -hide_banner -nostats -loglevel error -i \"{archivo_video}\" -c:v libx264 \"{archivo_salida}\"")
