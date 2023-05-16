import PySimpleGUI as sg



class BookshopGUI():

    def get_data(self):
        self.book_list = session.query(Books).all()
        data = [[item.id, item.book_title, item.author, item.year, item.price, item.quantity]
            for item in self.book_list]
        return data


    def __init__(self):
            headers = ['ID', 'Book Title', "Author", 'Year of Release', 'Price', 'Quantity']
            self.table = sg.Table(values=, headings=headers, auto_size_columns=True, key="-TABLE-", enable_events=True)
            self.layout = [
                [self.table],
                [sg.Button ("ADD TO CART",), sg.Button("VIEW CART"), sg.Button("FILTER BOOKS BY AUTHOR"), sg.Button("FILTER BOOKS BY THE YEAR"), sg.Button("EXIT"), sg.Button("VIEW PURCHASE HISTORY")]]
            self.window = sg.Window("BOOK_SHOP", layout=self.layout)



    def run(self):
            while True:
                event, value = self.window.read
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
