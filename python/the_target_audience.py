# Напишите скрипт на Python, который анализирует данные пользователей,
# хранящиеся в текстовом файле. Скрипт считывает данные о пользователях
# из файла, обрабатывает их и вычисляет статистику по полу и возрасту пользователей.
male_count = 0
female_count = 0
age_7_15_count = 0
age_16_20_count = 0
age_21_35_count = 0

file_name = 'C:\\Users\\lawrence\\Education_python\\python\\data\\user_data.txt'
with open(file_name, "r",encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 3:
            _, age, gender = parts  # Нас не интересует id пользователя, поэтому используем _ для игнорирования
            age = int(age)
            print(gender)
            
            if gender == "м":
                 male_count += 1
            elif gender == "ж":
                female_count += 1
            if 7 <= age <= 15:
                age_7_15_count += 1
            elif 16 <= age <= 20:
                age_16_20_count += 1
            elif 21 <= age <= 35:
                age_21_35_count += 1

total_users = male_count + female_count
total_age = age_7_15_count + age_16_20_count + age_21_35_count

male_percentage = (male_count / total_users) * 100
female_percentage = (female_count / total_users) * 100

age_7_15_percentage = (age_7_15_count / total_age) * 100
age_16_20_percentage = (age_16_20_count / total_age) * 100
age_21_35_percentage = (age_21_35_count / total_age) * 100

print(f"Разница между полами: Мужчины - {male_percentage:.2f}%, Женщины - {female_percentage:.2f}%")
print(f"Преобладающий возрастной диапазон: 7-15 лет - {age_7_15_percentage:.2f}%, 16-20 лет - {age_16_20_percentage:.2f}%, 21-35 лет - {age_21_35_percentage:.2f}%")