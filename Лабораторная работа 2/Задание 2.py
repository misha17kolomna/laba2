salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
i = 0
x = 0
for i in range(months):
    x = x + salary - spend
    spend = spend * (increase + 1)
x *= -1
y = round(x,2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", y)
