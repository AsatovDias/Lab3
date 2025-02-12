import json

# Шаг 1: Открываем и загружаем JSON-файл
with open("sample-data") as f:
    data = json.load(f)

# Шаг 2: Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

# Шаг 3: Обработка данных из `imdata`
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    
    # Шаг 4: Печать строки таблицы
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")
