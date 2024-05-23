import pyperclip
from docx import Document
from time import sleep
while True:
    def transfer_to_word():
        # Crear un nuevo documento de Word
        doc = Document()

        # Obtener el texto del portapapeles
        text = pyperclip.paste()

        # Añadir el texto al documento
        doc.add_paragraph(text)

        # Guardar el documento
        doc.save('Programas propios\output.docx')

    # Activar/desactivar la función
    activate = True

    if activate:
        transfer_to_word()
    sleep(10)