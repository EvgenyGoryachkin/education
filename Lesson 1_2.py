clock = int(input("Введите необходимое время в секундах "))
hour = clock // 3600
minute = (clock - hour * 3600) // 60
second = clock - (hour * 3600 + minute * 60)
print(f"Конвертированное время в нужном формате {hour} {minute} {second}")
