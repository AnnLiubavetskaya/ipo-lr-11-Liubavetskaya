from transport.client import Client
from transport.airplane import Airplane
from transport.van import Van
from transport.transport_company import TransportCompany

def menu():
    company = TransportCompany("My Transport Company")

    while True:
        print("\nМеню:")
        print("1. Добавить клиента")
        print("2. Добавить транспортное средство")
        print("3. Просмотреть транспортные средства")
        print("4. Распределить грузы")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            # Ввод имени клиента с валидацией
            while True:
                name = input("Имя клиента: ").strip()
                if not name:
                    print("Имя клиента не может быть пустым. Попробуйте снова.")
                else:
                    break

            # Ввод веса груза с валидацией
            while True:
                try:
                    cargo_weight = float(input("Вес груза (в тоннах): "))
                    if cargo_weight <= 0:
                        print("Вес груза должен быть положительным числом. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Неверный ввод. Вес груза должен быть числом.")

            # Ввод VIP-статуса с валидацией
            while True:
                is_vip_input = input("VIP клиент? (y/n): ").lower()
                if is_vip_input in ['y', 'n']:
                    is_vip = is_vip_input == 'y'
                    break
                else:
                    print("Неверный ввод. Ответ должен быть 'y' или 'n'.")

            client = Client(name, cargo_weight, is_vip)
            company.add_client(client)

        elif choice == "2":
            # Ввод типа транспорта с валидацией
            while True:
                vehicle_type = input("Тип транспорта (airplane/van): ").lower()
                if vehicle_type in ['airplane', 'van']:
                    break
                else:
                    print("Неверный ввод. Тип транспорта должен быть 'airplane' или 'van'.")

            # Ввод грузоподъемности с валидацией
            while True:
                try:
                    capacity = float(input("Грузоподъемность (в тоннах): "))
                    if capacity <= 0:
                        print("Грузоподъемность должна быть положительным числом. Попробуйте снова.")
                    else:
                        break
                except ValueError:
                    print("Неверный ввод. Грузоподъемность должна быть числом.")

            if vehicle_type == "airplane":
                # Ввод максимальной высоты полета с валидацией
                while True:
                    try:
                        max_altitude = int(input("Максимальная высота полета (в метрах): "))
                        if max_altitude <= 0:
                            print("Высота полета должна быть положительным числом. Попробуйте снова.")
                        else:
                            break
                    except ValueError:
                        print("Неверный ввод. Высота полета должна быть целым числом.")

                vehicle = Airplane(capacity, max_altitude)

            elif vehicle_type == "van":
                # Ввод наличия холодильника с валидацией
                while True:
                    is_refrigerated_input = input("Холодильник? (y/n): ").lower()
                    if is_refrigerated_input in ['y', 'n']:
                        is_refrigerated = is_refrigerated_input == 'y'
                        break
                    else:
                        print("Неверный ввод. Ответ должен быть 'y' или 'n'.")

                vehicle = Van(capacity, is_refrigerated)

            company.add_vehicle(vehicle)

        elif choice == "3":
            vehicles = company.list_vehicles()
            if vehicles:
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("Транспортных средств нет.")

        elif choice == "4":
            company.optimize_cargo_distribution()
            print("Грузы распределены!")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
