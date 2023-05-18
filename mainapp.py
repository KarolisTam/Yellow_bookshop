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
        sg.Button("FILTER BOOKS BY AUTHOR")], 
    [sg.Button("FILTER BOOKS BY THE YEAR"), 
        sg.Button("EXIT"), 
        sg.Button("VIEW PURCHASE HISTORY")]
    ]    

window = sg.Window("BOOK_SHOP", layout)

customer_id = Login().login_page()

while customer_id:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'EXIT':
        break
    elif event == 'ADD TO CART':
        obijektas.add_to_oder_cart(table, values)
    elif event == 'VIEW CART':
        obijektas.shopping_oder(customer_id)
        window["-TABLE-"].update(values=obijektas.get_product_list())
    elif event == 'FILTER BOOKS BY AUTHOR':
        window["-TABLE-"].update(values=obijektas.filter_by_author())
    elif event == 'FILTER BOOKS BY THE YEAR':
        window["-TABLE-"].update(values=obijektas.filter_by_year())
    elif event == 'VIEW PURCHASE HISTORY':
        obijektas.purchase_history(customer_id)
window.close()