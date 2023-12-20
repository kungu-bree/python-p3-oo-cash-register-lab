#!/usr/bin/env python3

#!/usr/bin/env python3


class CashRegister:
    def __init__(self):
        self.items = []
        self.last_transaction = None
        self.discount = 0
        self.total = 0

    def add_item(self, item, price, quantity=1):
        self.items.append({'item': item, 'price': price, 'quantity': quantity})
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After applying a {self.discount}% discount, the total is ${self.total:.2f}"
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.last_transaction is not None:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = None
        else:
            return "No transaction to void."

    def show_items(self):
        for item in self.items:
            print(f"{item['quantity']} {item['item']}(s) at ${item['price']} each")

    def get_total(self):
        return f"The total amount is ${self.total:.2f}"
  
