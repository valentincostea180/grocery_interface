from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def list(self):
        print(f"{self.name}, costs {self.price}$")
    def receipt(self):
        return self.name, float(self.price)

add = 0


def main():
    print("\n\nWelcome back to the shop!\n")
    grocery_list = {}
    while(True):
        com = input("LIST - checking the grocery list\n"
                    "ADD - adding to the grocery list\n"
                    "OUT - checking out and paying\n\n"
                    "Command: ")
        if com.upper().strip() == 'LIST':
            check_list(grocery_list)
        elif com.upper().strip() == 'ADD':
            add_list(grocery_list)
        elif com.upper().strip() == 'OUT':
            out_list(grocery_list)
            break
        else:
            print("Missing command...")
        if (add + 1) > 10:
            maximum_out()
            out_list(grocery_list)
            break


def check_list(grocery_list):
    if len(grocery_list) == 0:
        print("\n\nNo added products for now.\n"
              "Maybe meant ADDing?\n")
    else:
        items, price = out(grocery_list)
        generate_list_pdf(items, price)



def add_list(grocery_list):
    global add
    add += 1
    a = input("Name of the product: ")
    b = input(f"Price of the product: ")
    while True:
        try:
            grocery_list[a] = Product(a, float(b))
            print("\n\n")
            break
        except ValueError:
            print("Should be a number.\n")
            b = input(f"Price of the product: ")


def out_list(grocery_list):
    budget = get_budget()
    items, price = out(grocery_list)
    print("Don't forget the receipt!\n"
          "It's on the house!")
    generate_receipt_pdf(items, price, budget)


def out(grocery_list):
    total_price = 0
    items = {}
    for prod in grocery_list.values():
        name, price = prod.receipt()
        total_price += price
        items[name] = price
    return items, total_price


def generate_list_pdf(items, total_price):
    c = canvas.Canvas("list.pdf", pagesize=letter)
    c.setFont("Helvetica", 24)
    page_width = letter[0]
    center_x = page_width / 2
    y = 750
    c.drawCentredString(center_x, y, "List")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(100, y, "----------------------------------------------------------------------------------------------------")
    y -= 20
    for item in items:
        c.drawString(100, y, item)
        y -= 20
    c.drawString(100, y, "----------------------------------------------------------------------------------------------------")
    y -= 20
    c.drawCentredString(center_x, y, f"To pay: {total_price}$")
    c.save()

def generate_receipt_pdf(items, total_price, budget):
    c = canvas.Canvas("receipt.pdf", pagesize=letter)
    c.setFont("Helvetica", 24)
    page_width = letter[0]
    center_x = page_width / 2
    y = 750
    c.drawCentredString(center_x, y, "Receipt")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(100, y, "----------------------------------------------------------------------------------------------------")
    y -= 20
    for item, price in items.items():
        c.drawString(100, y, f"{item}")
        c.drawString(480, y, f"{price}$")
        y -= 20
    c.drawString(100, y, "----------------------------------------------------------------------------------------------------")
    y -= 20
    c.drawCentredString(center_x, y, f"Total: {total_price}$")
    y -= 20
    c.drawCentredString(center_x, y, f"Paid: {budget}$")
    y -= 20
    c.drawCentredString(center_x, y, f"Change: {budget - total_price}$")
    y -= 20
    c.drawCentredString(center_x, y, f"{date.today()}")
    c.save()

def get_budget():
    while True:
        try:
            return float(input("\n\nHow much are you willing to spend today? "))
        except ValueError:
            print("Should be a number.\n")


def maximum_out():
    print("The list has maximum 10 items.\n"
                  "Checking out...\n\n")

if __name__ == "__main__":
    main()
