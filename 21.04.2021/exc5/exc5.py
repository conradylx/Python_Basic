# Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można produkt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    shop_items = ['Sweater', 'Hoodie', 'Shorts', 'T-shirt', 'Kardigan', 'Shirt', 'Hat']
    shop_sold_items = []

    def check_assortment(self):
        formatted_items = ", ".join(self.shop_items)
        print(f'Actual shop assortment is: {formatted_items}.')

    def buy_item(self, name):
        if name in self.shop_items:
            print(f'You bought an {name}')
            self.shop_sold_items.append(name)
            return self.shop_items.remove(name)
        else:
            print(f"There is no {name.lower()} in the shop assortment")

    def try_on_cloth(self, item):
        print(f'{item} looks great on you')

    def return_to_shop(self, item):
        if item in self.shop_sold_items:
            print(f'Returned {item} successfully')
            self.shop_items.append(item)
        else:
            print(f'{item} was not in the shop assortment')


if __name__ == '__main__':
    shop1 = Shop()
    shop1.check_assortment()
    shop1.buy_item('Kardigan')
    shop1.check_assortment()
    shop1.return_to_shop('ItemX')
    shop1.buy_item('Shoes')
    shop1.return_to_shop('Kardigan')
    shop1.check_assortment()
    shop1.try_on_cloth('Kardigan')
