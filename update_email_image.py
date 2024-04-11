import win32com.client as win32
import os
from PIL import Image, ImageGrab
from openpyxl import load_workbook


def update_image():
    try:
        os.remove(
            r'\Acompanhamento\imagem.png')
    except(Exception):
        print('Nao tem imagem')

    
    # Necessita de ajustes
    """ workbook = load_workbook(
      r"\Acompanhamento\Relatorio_atualizavel_v7.xlsm",
      read_only=True,
      keep_vba=True
    )
    sheet = workbook['Responsável']

    start_cell = 'A1'
    end_cell = 'L36'
    range_cells = sheet[start_cell:end_cell]

    num_columns = len(range_cells[0])
    num_rows = len(range_cells)

    cell_width_in_pixels = 100
    cell_height_in_pixels = 50
    image_width = num_columns * cell_width_in_pixels
    image_height = num_rows * cell_height_in_pixels
    image = Image.new('RGB', (image_width, image_height), 'white')
    pixels = image.load()

    # Iterate over the cells and copy their values to the image
    for row_idx, row in enumerate(range_cells):
      for col_idx, cell in enumerate(row):
        value = cell.value

        x = col_idx * cell_width_in_pixels
        y = row_idx * cell_height_in_pixels

        # Set the pixel color based on the cell value
        color = (0, 0, 0)  # Black color for text
        if value is None:
          color = (255, 255, 255)  # White color for empty cells
        for i in range(cell_width_in_pixels):
          for j in range(cell_height_in_pixels):
            pixels[x + i, y + j] = color

    # Save the image
    image.save(r'\Acompanhamento\imgs\imagem.png') """



    xlapp = win32.gencache.EnsureDispatch('Excel.Application')
    xlapp.DisplayAlerts = False
    xlapp.Visible = True

    report = xlapp.Workbooks.Open(
        r"\Acompanhamento\Relatorio_atualizavel.xlsm")

    dinWs = report.Worksheets('Responsável')

    dinWs.Range(dinWs.Cells(1, 1), dinWs.Cells(36, 16)).Copy()
    img = ImageGrab.grabclipboard()
    img.save(
        r'\Acompanhamento\imgs\imagem.png')

    report.Close(True)
    xlapp.Quit()

    del report
    del xlapp


if __name__ == '__main__':
    update_image()
