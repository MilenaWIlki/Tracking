class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

class OrderTracking:
    def __init__(self):
        self.orders = {}

    def place_order(self, order_id, products):
        self.orders[order_id] = Order(order_id, products)

    def track_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id].products
        else:
            return None

# Example usage:
order_tracking = OrderTracking()
order_tracking.place_order(1, [Product(1, "T-shirt", 20, "Comfortable cotton T-shirt"), Product(2, "Jeans", 40, "Classic denim jeans")])
order_products = order_tracking.track_order(1)
print("Ordered Products:", order_products)
