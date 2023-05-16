import PySimpleGUI as sg
from backend import Product, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()


class BookshopGUI():

    def get_product_list(self):
        self.products = session.query(Product).all()
        product_list = []
        for item in self.products:           
            product_list.append([item.id, item.book_title, item.author, item.year, item.price, item.quantity])
        return product_list

    def __init__(self):
        headers = ['ID', 'Book Title', "Author", 'Year of Release', 'Price', 'Quantity']
        self.table = sg.Table(values=self.get_product_list(), headings=headers, 
                              auto_size_columns=True, key="-TABLE-", enable_events=True)
        self.layout = [
            [self.table],
            [sg.Button("ADD TO CART"), 
             sg.Button("VIEW CART"), 
             sg.Button("FILTER BOOKS BY AUTHOR"), 
             sg.Button("FILTER BOOKS BY THE YEAR"), 
             sg.Button("EXIT"), 
             sg.Button("VIEW PURCHASE HISTORY")]]
        self.window = sg.Window("BOOK_SHOP", layout=self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'EXIT':
                break
            elif event == 'ADD TO CART':
                pass
            elif event == 'VIEW CART':
                pass
            elif event == 'FILTER BOOKS BY AUTHOR':
                pass
            elif event == 'FILTER BOOKS BY YEAR':
                pass
            elif event == 'VIEW PURCHASE HISTORY':
                pass


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


