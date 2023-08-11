from typing import List


class Customer:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Order:

    def __init__(self, item: str, customer_id: int):
        self.item = item
        self.customer_id = customer_id


def print_ordered_items(orders: List[Order], customers: List[Customer]):
    # what is wrong with this implementation
    for order in orders:
        for customer in customers:
            if order.customer_id == customer.id:
                print(f"Customer {customer.name} ordered {order.item}")
                continue


if __name__ == '__main__':
    # task: given a list of customer and orders, print the name of the customer for each ordered item

    # get a list of all customers
    customers = [Customer(123, "Juanita"), Customer(444, "Pablo"), Customer(2, "Sanchez")]

    # get list of recent orders
    orders = [Order("bread", 123), Order("eggs", 444), Order("juice", 444)]

    # print each customer id and the items they purchased
    print_ordered_items(orders, customers)
