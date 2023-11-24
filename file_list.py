#---------------------------------------------------------------------------------------
# Libreria file_list
#Proyecto: folderFree
#Version: 0.1
#Dev: Ing. Hector Rafael Gonzalez Vega
#Date: 10/10/2023
#update: 07/11/2023
#This code is under Creative Commons CC-BY "Atribución 3.0 No portada" License:
#https://creativecommons.org/licenses/by/3.0/deed.es
#---------------------------------------------------------------------------------------
import os
import shutil

FOLDERS_DIR = {'downloads':"~/Downloads",'documents':"~/Documents",'pictures':"~/Pictures",'music':"~/Music",'videos':"~/Videos",}
FOLDERS_NME = {'downloads':"Descargas",'documents':"Documentos",'pictures':"Imagenes",'music':"Musica",'videos':"Videos",}

def text_cut(txt):
    '''
        Cortador de texto, comprueba el tamaño del string y si sobrepasa los 30 caracteres
        este sera recortado y se agregaran '...' al final.

        Args:
            txt (string): Texto a cortar.
        
        Returns:
            string: Texto corregido.
    '''

    if len(txt) > 30:
        txt = f"{txt[:30]}..."
    
    return txt

def list_files(folder_list):
    '''
       Enlistador de archivos (y carpetas). Segun una lista con los nombres de las carpetas,
       hara un listado del contenido de las mismas y lo devolvera.

        Args:
            folder_list (list): Lista con los nombres de carpetas a analisar.
        
        Returns:
            list[list]: Devolvera una lista dentro de otra, donde el contenido seran los
            archivos contenidos de las carpetas, el contenido de la sublista es:
                - 0: Nombre legible de carpeta
                - 1: Nombre del archivo
                - 2: Tamaño del archivo
                - 3: Ruta del archivo
    '''
    data = []

    for folder in folder_list:
        dir_path = os.path.expanduser(FOLDERS_DIR[folder])
        
        try:
            files =  os.listdir(dir_path)
            for file in files:
                file_path = os.path.join(dir_path, file)
                #print(file_path)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    if file_size < 1024:
                        size = f"{file_size} bytes"
                    elif file_size < 1024 * 1024:
                        size = f"{file_size / 1024:.2f} KB"
                    elif file_size < 1024 * 1024 * 1024:
                        size = f"{file_size / (1024 * 1024):.2f} MB"
                    else:
                        size = f"{file_size / (1024 * 1024):.2f} GB"

                    data.append([FOLDERS_NME[folder],text_cut(file),size,file_path])
                elif os.path.isdir(file_path):
                    data.append([FOLDERS_NME[folder],text_cut(file),'NA',file_path])
        
        except FileNotFoundError:
            pass
        
    return data

def del_files(_path):
    '''
        Segun la ruta dada, eliminara el archivo o carpeta.

        Args:
            _path (string): Ruta de archivo o carpeta a eliminar.
        
        Returns:
            None
    '''
    try:
        if os.path.isfile(_path):
            os.remove(_path)
        elif os.path.isdir(_path):
            shutil.rmtree(_path)
    except:
        pass
