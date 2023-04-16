# -*- coding: cp1251 -*-
import yaml

data = {
    "items": ["computer", "printer", "keyboard", "mouse"],
    "items_price": {
        "computer": "200€-1000€",
        "keyboard": "5€-50€",
        "mouse": "4€-7€",
        "printer": "100€-300€"
    },
    "items_quantity": 4
}

# Сохраняем данные в файл в формате YAML
with open('file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

# Считываем данные из файла и проверяем, совпадают ли они с исходными
with open('file.yaml', 'r', encoding='utf-8') as file:
    loaded_data = yaml.safe_load(file)

print(data == loaded_data)  # должно вывести True



