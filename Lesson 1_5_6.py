proceeds = float(input("Укажите сумму выручки фирмы "))
outpay = float(input("Укажите сумму издержки фирмы "))
if proceeds > outpay:
    benefit = proceeds / outpay
    print(f"Фирма работает в прибыль.")
    print(f"Рентабельность выручки составила  {benefit: .2f}")
    employee = float(input("Укажите количество работников  "))
    employee_debt = benefit / employee
    print(f"Рентабельность выручки на одного сотрудника составила  {employee_debt: .2f}")
elif proceeds < outpay:
    print(f"Фирма работает в убыток.")

