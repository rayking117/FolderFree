#---------------------------------------------------------------------------------------
# Aplicacion limpiadora de carpetas especificas
#Name: folderFree
#Version: 0.1
#Dev: Ing. Hector Rafael Gonzalez Vega
#Date: 10/10/2023
#update: 07/11/2023
#This code is under Creative Commons CC-BY "Atribución 3.0 No portada" License:
#https://creativecommons.org/licenses/by/3.0/deed.es
#---------------------------------------------------------------------------------------
import flet as ft
from file_list import list_files, del_files



def main(page):
    """
    Funcion principal de la aplicacion.
    """
    #Variables
    rows = []
    fls = []

    #Funciones
    def close_msg_alerta(e):
        """
        Cierra el modal con el mensaje de alerta.
        
        Args:
            e (any): Evento.
        
        Returns:
            NA
        """
        msg_alerta.open = False
        page.update()

    def open_msg_alerta(e):
        """
        Abre el modal con el mensaje de alerta.
        
        Args:
            e (any): Evento.
        
        Returns:
            NA
        """
        page.dialog = msg_alerta
        msg_alerta.open = True
        page.update()

    def del_fls(e):
        """
        Elimina los archivos y carpetas.
        
        Args:
            e (any): Evento.
        
        Returns:
            NA
        """
        msg_alerta.open = False
        fls = search_fls(None)
        if len(fls) > 0:
            for file in fls:
                del_files(file[3])
        search_fls(None)
    
    def search_fls(e):
        """
        Dependiendo de lo seleccionado en los "Checkbox" seran las carpetas a analisar
        para obtener su contenido y mostrarlo en el "Datatable".
        
        Args:
            e (any): Evento.
        
        Returns:
            list: Lista con los archivos analisados segun los "Checbox" seleccionados.
        """
        rows = []
        folders = []

        if download_cb.value:
            folders.append('downloads')
        if documents_cb.value:
            folders.append('documents')
        if pictures_cb.value:
            folders.append('pictures')
        if music_cb.value:
            folders.append('music')
        if videos_cb.value:
            folders.append('videos')
        
        files = list_files(folders)
        for file in files:
            rows.append(ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(file[0])),
                            ft.DataCell(ft.Text(file[1])),
                            ft.DataCell(ft.Text(file[2])),
                        ],
                    ),)
        file_table.rows = rows
        del_button.disabled=False
        page.update()
        return files

    #Configuracion de ventana
    page.title = "folderFree"
    page.window_height = 450
    page.window_width = 800
    page.window_maximizable = False

    #Interfas de usuario
    download_cb = ft.Checkbox(label="Descargas", col={"md":2}, )
    documents_cb = ft.Checkbox(label="Documentos", col={"md":2})
    pictures_cb = ft.Checkbox(label="Imagenes", col={"md":2})
    music_cb = ft.Checkbox(label="Musica", col={"md":2}, value=True)
    videos_cb = ft.Checkbox(label="Videos", col={"md":2})
    del_button = ft.ElevatedButton("Eliminar", disabled=True, on_click=open_msg_alerta, col={"md":6}, bgcolor=ft.colors.ERROR, color=ft.colors.ON_PRIMARY)
    file_table = ft.DataTable( #Datatable
        width=800,
        divider_thickness=0,
        vertical_lines=ft.border.BorderSide(0, "black"),
        heading_row_color=ft.colors.BLACK12,
        column_spacing=10,
        columns=[
            ft.DataColumn(ft.Text("Carpeta")),
            ft.DataColumn(ft.Text("Archivo")),
            ft.DataColumn(ft.Text("Tamaño")),
        ],
        rows=rows
    )

    msg_alerta = ft.AlertDialog( #Modal
        modal=True,
        title=ft.Text("Confirma porfavor"),
        content=ft.Text("¿En verdad deseas eliminar estos archivos?"),
        actions=[
            ft.TextButton("Si", on_click=del_fls),
            ft.TextButton("No", on_click=close_msg_alerta),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    c1 = ft.Column( #Columna de Datatable
        spacing=10,
        height=300,
        
        col={"lg": 12},
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                border = ft.border.all(1, "black"),
                border_radius=10,
                col={"lg": 12},
                alignment=ft.alignment.center,
                content=file_table
            )
        ]
    )
    
    #Integracion de contenido
    page.add(
        ft.ResponsiveRow([download_cb, documents_cb, pictures_cb, music_cb, videos_cb]),
        ft.ResponsiveRow([c1]),
        ft.ResponsiveRow([ft.ElevatedButton("Examinar", on_click=search_fls, col={"md":6}),del_button,]),
        
    )


if __name__== "__main__":
    ft.app(target=main)