import PySimpleGUI as sg
from backend import Product, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()


def get_product_list():
    products = session.query(Product).all()
    product_list = []
    for item in products:           
        product_list.append([item.id, item.book_name, item.author, item.realease_date, item.price, item.quantity])
    return product_list

def shopping_oder():

    sg.theme("LightGreen5")
    headers =["Book name", "Author", "Release year", "Price"]
    layout =[
        [sg.Table(values="", headings=headers, auto_size_columns=True, key="order_table", enable_events=True)],
        [sg.Button("Remove", key="remove"), sg.Button("Purchase", key="purchase"), sg.Button("Close Shopping Order", key="close")]
    ]
    shopcart = sg.Window("Shoping Order", layout)
    while True:
        event, values = shopcart.read()
        if event in (sg.WIN_CLOSED, 'close'):
            break
        elif event == "remove":
            selected_rows = values["order_table"][0]
            print(selected_rows)


    shopcart.close()

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


