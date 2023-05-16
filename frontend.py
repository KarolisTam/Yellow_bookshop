import PySimpleGUI as sg


def shopping_cart():
    sg.theme("LightGreen5")
    headers =["Book name", "Author", "Release year", "Price"]
    layout =[
        [sg.Table(values="", headings=headers, auto_size_columns=True, key="cart_table", enable_events=True)],
        [sg.Button("Remove", key="remove"), sg.Button("Purchase", key="purchase"), sg.Button("Close Shopping Cart", key="close")]
    ]
    shopcart = sg.Window("Shoping Cart", layout)
    while True:
        event, values = shopcart.read()
        if event in (sg.WIN_CLOSED, 'close'):
            break
        elif event == "remove":
            selected_rows = values["cart_table"][0]
            print(selected_rows)

   
    shopcart.close()

import PySimpleGUI as sg


def purchase_history():
    sg.theme("LightGreen5")
    headers =["Book name", "Author", "Release year", "Price", "Purchase Date"]
    layout =[
        [sg.Table(values="", headings=headers, auto_size_columns=True, key="history_table")],
        [sg.Button("Close Purchase History", key="close")]
    ]
    history = sg.Window("Shoping History", layout)
    while True:
        event, values = history.read()
        if event in (sg.WIN_CLOSED, 'close'):
            break
   
    history.close()

shopping_cart()