import subprocess
import os
import glob

ruta_ffmpeg = 'D:\\ffmpeg\\bin\\ffmpeg.exe'
carpeta_videos_ts = r'D:\Cursos\code-easy'
carpeta_salida_conversion = r'D:\Cursos\code-easy\salida'
sub_cadena = " - Curso de React con Typescript-playlist"

# Verificar si existe la carpeta de salida y si no existe la creamos
if not os.path.exists(carpeta_salida_conversion):
    os.makedirs(carpeta_salida_conversion)

# Obtener los archivos de la carpeta
archivos = os.listdir(carpeta_videos_ts)
prefijos = []  # Lista de prefijos de los archivos de video ejm: [2, 3, "9b", 10, 14, 15, 16, "16b", 21, 22]

archivos = sorted(archivos)
# Leemos los archivos .ts y obtenemos los prefijos
for archivo in archivos:
    if archivo.endswith('.ts'):
        prefijo = archivo.split('-')[0]
        if prefijo not in prefijos:
            prefijos.append(prefijo)

# Procedemos a convertir el archivo .ts a .mp4
for i in prefijos:
    archivo_video = glob.glob(os.path.join(carpeta_videos_ts, f"{i}-*.ts"))[0]
    nombre_archivo_video = os.path.splitext(os.path.basename(archivo_video))[0]
    # cadena_sin_subcadena = cadena.replace("(720p with 30fps)", "")
    nombre_archivo_video = nombre_archivo_video.replace(sub_cadena, "")
    archivo_salida = os.path.join(carpeta_salida_conversion, f"{nombre_archivo_video}.mp4")
    # invocamos a ffmpeg para la conversión
    print("\033[37m" + f"Convirtiendo... \033[32m{archivo_video}\033[37m --> \033[33m{archivo_salida}" + "\033[0m")

    subprocess.run(f"{ruta_ffmpeg} -hide_banner -nostats -loglevel error -i \"{archivo_video}\" -c:v libx264 \"{archivo_salida}\"")
