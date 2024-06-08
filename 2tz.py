def calculate_total_hours(c1, b1):
    total_hours = 0
    total_fireworks = c1
    burned_out_fireworks = 0
    
    while total_fireworks > 0:
        # Используем все имеющиеся огоньки
        total_hours += total_fireworks * 2
        burned_out_fireworks += total_fireworks
        total_fireworks = 0
        
        # Перерабатываем потухшие огоньки в новые
        total_fireworks += burned_out_fireworks // b1 * 2
        burned_out_fireworks = burned_out_fireworks % b1
    
    return total_hours

# Примеры использования
c1 = 5
b1 = 3
result = calculate_total_hours(c1, b1)
print(f"{result} часа")  # Ожидаемый результат: "22 часа"
