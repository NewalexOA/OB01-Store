class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Северная венеция", "Невский проспект")
store2 = Store("Культурная столица", "площадь Растрелли")
store3 = Store("Город трёх революций", "улица Восстания")

# Добавление товаров
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("вода", 1.0)
store3.add_item("шоколад", 1.5)

# Тестируем методы на примере store1
store1.add_item("хлеб", 1.25)
print(store1.get_price("хлеб"))
store1.update_price("хлеб", 1.5)
print(store1.get_price("хлеб"))
store1.remove_item("хлеб")
print(store1.get_price("хлеб"))