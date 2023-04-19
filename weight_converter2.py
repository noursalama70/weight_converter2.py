# Программа для конвертации веса из земных условий в условия космоса

# Константы
GRAVITY_MOON = 1.62  # Ускорение свободного падения на Луне, м/с^2
GRAVITY_MARS = 3.71  # Ускорение свободного падения на Марсе, м/с^2
GRAVITY_JUPITER = 24.79  # Ускорение свободного падения на Юпитере, м/с^2

# Функции
def convert_weight_on_moon(weight):
    return weight / 9.81 * GRAVITY_MOON

def convert_weight_on_mars(weight):
    return weight / 9.81 * GRAVITY_MARS

def convert_weight_on_jupiter(weight):
    return weight / 9.81 * GRAVITY_JUPITER

# Пример использования
weight_on_earth = float(input("Введите ваш вес в кг: "))
print(f"Вес на Луне: {convert_weight_on_moon(weight_on_earth)} кг")
print(f"Вес на Марсе: {convert_weight_on_mars(weight_on_earth)} кг")
print(f"Вес на Юпитере: {convert_weight_on_jupiter(weight_on_earth)} кг")
