class Store:
    def __init__(self, name, store_type, capacity):
        self.name = name
        self.type = store_type
        self.capacity = capacity
        self.items = {}

    
    def from_size(cls, name, store_type, size):
        return cls(name, store_type, size // 2)

    def add_item(self, item_name):
        if sum(self.items.values()) + 1 > self.capacity:
            return "Not enough capacity in the store"
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# Example Usage:
first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
