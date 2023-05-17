from frontend import *
import PySimpleGUI as sg
import time

obijektas = BookshopGUI()

headers = ['ID', 'Book Title', "Author", 'Year of Release', 'Price', 'Quantity']
table = sg.Table(values=BookshopGUI().get_product_list(), headings=headers, 
    auto_size_columns=True, key="-TABLE-", enable_events=True)

layout = [
    [table],
    [sg.Button("ADD TO CART"), 
        sg.Button("VIEW CART"), 
        sg.Button("FILTER BOOKS BY AUTHOR"), 
        sg.Button("FILTER BOOKS BY THE YEAR"), 
        sg.Button("EXIT"), 
        sg.Button("VIEW PURCHASE HISTORY"),
        sg.Button("CONFIRM ORDER")]
    ]    

window = sg.Window("BOOK_SHOP", layout)
condition = False
if Login().login_page():
    condition = True

while condition == True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'EXIT':
        break
    elif event == 'ADD TO CART':
        obijektas.add_to_oder_cart(table, values)
    elif event == 'VIEW CART':
        obijektas.shopping_oder()
    elif event == 'FILTER BOOKS BY AUTHOR':
        window["-TABLE-"].update(values=obijektas.filter_by_author())
    elif event == 'FILTER BOOKS BY YEAR':
        window["-TABLE-"].update(values=obijektas.filter_by_year())
    elif event == 'VIEW PURCHASE HISTORY':
        obijektas.purchase_history()
    elif event == 'CONFIRM ORDER':
        obijektas.loading_window()
        obijektas.purchase_history()
window.close()

