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
    # iterate once over orders and index by customer id
    indexed_orders = {}
    for order in orders:
        if order.customer_id in indexed_orders.keys():
            indexed_orders[order.customer_id].append(order.item)
        else:
            indexed_orders[order.customer_id] = [order.item]

    # iterate once over customers
    for customer in customers:
        if customer.id in indexed_orders.keys():
            item = indexed_orders[customer.id]
            print(f"Customer {customer.name} ordered {item}")

    # total operations len(orders)+len(customers) instead of len(orders)*len(customers)


if __name__ == '__main__':
    # task: given a list of customer and orders, print the name of the customer for each ordered item

    # get a list of all customers
    customers = [Customer(123, "Juanita"), Customer(444, "Pablo"), Customer(2, "Sanchez")]

    # get list of recent orders
    orders = [Order("bread", 123), Order("eggs", 444), Order("juice", 444)]

    # print each customer id and the items they purchased
    print_ordered_items(orders, customers)
