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