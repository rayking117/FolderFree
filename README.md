# FolderFree
Aplicacion limpiadora de las carpetas Descargas, Documentos, Imagenes, Musica y Videos de Windows

Name: folderFree

Version: 0.1

Dev: Ing. Hector Rafael Gonzalez Vega

Date: 10/10/2023

Update: 07/11/2023

## Indice

* [Descripcion del proyecto](#descripcion-del-proyecto)
* [Estado del Proyecto](#estado-del-proyecto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Libreria Interna](#-libreria-interna)
* [Licecia](#-licencia)
* [Versiones](#Versiones)

## Descripcion del proyecto
FolderFree (FF) nace para poder eliminar archivos de carpetas especificas sin tener que entrar a cada una y hacerlo manualmente. Solo funciona en Windows (de momento)

(:sweat_smile: *imagenes pendientes de subir* :sweat_smile:)

Para ejecutar el script es necesario tener instalado Python3 con la libreria **Flet**. Se debera ejecutar el Script **main.py**.

Al iniciar FF se podra ver una ventana con 5 Checkbox de cada carpeta (Musica por defecto):
* Segun la seleccionada es la que se examinara para eliminar el contenido.

Una tabla con Carpeta, Archivo y Tamaño:
* Carpeta: Indica la carpeta donde se encuentra el archivo.
* Archivo: Nombre del archivo (en ocaciones se puede mostrar reducido si es muy largo).
* Tamaño: Tamaño del archivo

Y 2 botones Examinar y Eliminar (desactivado por defecto):
* Examinar: Al dar clic, segun la carpeta seleccionada, se examinara y mostrara el conetenido dentro de la tabla y el boton Eliminar se activara
* Eliminar: Al dar clic se mostrara un aviso de confirmacion: No-> no elimina; Si-> Elimina el contenido de las carpetas seleccionadas.

## Estado del Proyecto
A fecha de **Noviembre 2023** el proyecto se encuentra en **version 0.1**.

Debido a otros proyectos, este se encuentra en **pausa**, pero no quiere decir que ya no se actualizara.

## Tecnologias Utilizadas
* Python 3.11.5
* Flet 0.10.3
* os
* shutil

## Licecia
Este Proyecto esta bajo Creative Commons CC-BY "Atribución 3.0 No portada" License:
https://creativecommons.org/licenses/by/3.0/deed.es

## Versiones

v0.1
--
Elimina contenido de las carpetas:
* Descargas
* Documentos
* Imagenes
* Musica
* Videos