from classes.classes import Product, Order, Customer, Discount


# Товары
p1 = Product("Носочки", 800)
p2 = Product("Шляпка", 1200)
p3 = Product("Маечка", 1500)
p4 = Product("Юбочка", 2000)
p5 = Product("Брючки", 2500)

# Клиенты
c1 = Customer("Анна")
c2 = Customer("Иван")
c3 = Customer("Петруша")
c4 = Customer("Натуська")

# Заказы
order1 = Order([p1, p3])           # для Анны
order2 = Order([p2])               # для Анны
order3 = Order([p2, p3])           # для Ивана
order4 = Order([p1, p2, p4])       # для Петруши
order5 = Order([p3, p3, p1, p5])   # для Натуськи

# Добавляем заказы клиентам
c1.add_order(order1)
c1.add_order(order2)
c2.add_order(order3)
c3.add_order(order4)
c4.add_order(order5)

# Применяем скидки
discount1 = Discount("Сезонная скидка", 15)
discount2 = Discount("Промокод", 25)

print(f"\nСумма заказа с сезонной скидкой (Анна): {order1.apply_discount(discount1.discount_percent):.2f}₽")
print(f"Сумма заказа с промокодом (Анна): {order2.apply_discount(discount2.discount_percent):.2f}₽")

# Вывод информации о клиентах
print("\n--- Информация о клиентах и заказах ---")
print(c1)
print()
print(c2)
print()
print(c3)
print()
print(c4)

# Общая статистика
print("\n--- Общая статистика ---")
print(f"Всего заказов: {Order.total_order_count()}")
print(f"Общая сумма всех заказов: {Order.total_revenue():.2f}₽")