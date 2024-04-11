import xlwings as xw
from listener import MsgBoxListener

file_path = r"\Acompanhamento\BASE_atualizavel.xlsm"
modulo = "mdlUpdate"
macro = "start_macro"
title_msgbox = "Relatório"
find_msgbox = True

# start child thread
if find_msgbox:
    listener = MsgBoxListener(title_msgbox, 3)
    listener.start()

app = xw.App(visible=True, add_book=False)
wb = app.books.open(file_path)

run_macro = wb.app.macro(modulo + "." + macro)
run_macro()
#wb.save(file_path)

wb.close()

# stop listener thread
if find_msgbox:
    listener.stop()

