import tkinter as tk
from tkinter import ttk, messagebox
from transport.client import Client
from transport.airplane import Airplane
from transport.van import Van
from transport.transport_company import TransportCompany
import re

class TransportApp:
    def __init__(self, root):
        self.company = TransportCompany("My Transport Company")
        self.root = root
        self.root.title("Transport Company")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        self.menu_label = tk.Label(self.main_frame, text="Меню:")
        self.menu_label.pack()

        self.add_client_button = tk.Button(self.main_frame, text="Добавить клиента", command=self.add_client)
        self.add_client_button.pack(pady=5)

        self.add_vehicle_button = tk.Button(self.main_frame, text="Добавить транспортное средство", command=self.add_vehicle)
        self.add_vehicle_button.pack(pady=5)

        self.view_data_button = tk.Button(self.main_frame, text="Просмотреть данные", command=self.view_data)
        self.view_data_button.pack(pady=5)

        self.distribute_cargo_button = tk.Button(self.main_frame, text="Распределить грузы", command=self.distribute_cargo)
        self.distribute_cargo_button.pack(pady=5)

        self.exit_button = tk.Button(self.main_frame, text="Выход", command=root.quit)
        self.exit_button.pack(pady=5)

    def add_client(self):
        add_client_window = tk.Toplevel(self.root)
        add_client_window.title("Добавить клиента")

        tk.Label(add_client_window, text="Имя клиента:").pack()
        name_entry = tk.Entry(add_client_window)
        name_entry.pack()

        tk.Label(add_client_window, text="Вес груза (в тоннах):").pack()
        cargo_weight_entry = tk.Entry(add_client_window)
        cargo_weight_entry.pack()

        tk.Label(add_client_window, text="VIP клиент? (y/n):").pack()
        is_vip_entry = tk.Entry(add_client_window)
        is_vip_entry.pack()

        def save_client():
            name = name_entry.get().strip()
            if not name:
                messagebox.showerror("Ошибка", "Имя клиента не может быть пустым.")
            elif re.search(r'\d', name):
                messagebox.showerror("Ошибка", "Имя клиента не может содержать цифры.")
            else:
                try:
                    cargo_weight = float(cargo_weight_entry.get())
                    if cargo_weight <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Ошибка", "Вес груза должен быть положительным числом.")
                    return

                is_vip_input = is_vip_entry.get().lower()
                if is_vip_input not in ['y', 'n']:
                    messagebox.showerror("Ошибка", "Ответ должен быть 'y' или 'n'.")
                    return

                is_vip = is_vip_input == 'y'

                client = Client(name, cargo_weight, is_vip)
                self.company.add_client(client)
                messagebox.showinfo("Успех", "Клиент добавлен.")
                add_client_window.destroy()

        tk.Button(add_client_window, text="Сохранить", command=save_client).pack(pady=5)

    def add_vehicle(self):
        add_vehicle_window = tk.Toplevel(self.root)
        add_vehicle_window.title("Добавить транспортное средство")

        tk.Label(add_vehicle_window, text="Тип транспорта (airplane/van):").pack()
        vehicle_type_entry = tk.Entry(add_vehicle_window)
        vehicle_type_entry.pack()

        tk.Label(add_vehicle_window, text="Грузоподъемность (в тоннах):").pack()
        capacity_entry = tk.Entry(add_vehicle_window)
        capacity_entry.pack()

        def save_vehicle():
            vehicle_type = vehicle_type_entry.get().lower()
            if vehicle_type not in ['airplane', 'van']:
                messagebox.showerror("Ошибка", "Тип транспорта должен быть 'airplane' или 'van'.")
                return

            try:
                capacity = float(capacity_entry.get())
                if capacity <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Ошибка", "Грузоподъемность должна быть положительным числом.")
                return

            if vehicle_type == "airplane":
                tk.Label(add_vehicle_window, text="Максимальная высота полета (в метрах):").pack()
                max_altitude_entry = tk.Entry(add_vehicle_window)
                max_altitude_entry.pack()

                def save_airplane():
                    try:
                        max_altitude = int(max_altitude_entry.get())
                        if max_altitude <= 0:
                            raise ValueError
                    except ValueError:
                        messagebox.showerror("Ошибка", "Высота полета должна быть положительным числом.")
                        return

                    vehicle = Airplane(capacity, max_altitude)
                    self.company.add_vehicle(vehicle)
                    messagebox.showinfo("Успех", "Самолет добавлен.")
                    add_vehicle_window.destroy()

                tk.Button(add_vehicle_window, text="Сохранить самолет", command=save_airplane).pack(pady=5)

            elif vehicle_type == "van":
                tk.Label(add_vehicle_window, text="Холодильник? (y/n):").pack()
                is_refrigerated_entry = tk.Entry(add_vehicle_window)
                is_refrigerated_entry.pack()

                def save_van():
                    is_refrigerated_input = is_refrigerated_entry.get().lower()
                    if is_refrigerated_input not in ['y', 'n']:
                        messagebox.showerror("Ошибка", "Ответ должен быть 'y' или 'n'.")
                        return

                    is_refrigerated = is_refrigerated_input == 'y'

                    vehicle = Van(capacity, is_refrigerated)
                    self.company.add_vehicle(vehicle)
                    messagebox.showinfo("Успех", "Фургон добавлен.")
                    add_vehicle_window.destroy()

                tk.Button(add_vehicle_window, text="Сохранить фургон", command=save_van).pack(pady=5)

        tk.Button(add_vehicle_window, text="Далее", command=save_vehicle).pack(pady=5)

    def view_data(self):
        data_window = tk.Toplevel(self.root)
        data_window.title("Данные клиентов и транспортных средств")

        client_frame = tk.LabelFrame(data_window, text="Клиенты")
        client_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        client_tree = ttk.Treeview(client_frame, columns=("Name", "Cargo Weight", "VIP Status"), show="headings")
        client_tree.heading("Name", text="Имя")
        client_tree.heading("Cargo Weight", text="Вес груза")
        client_tree.heading("VIP Status", text="VIP")

        for client in self.company.clients:
            client_tree.insert("", "end", values=(client.name, client.cargo_weight, "Да" if client.is_vip else "Нет"))

        client_tree.pack(fill="both", expand="yes")
        client_tree.bind("<Double-1>", self.edit_client)

        vehicle_frame = tk.LabelFrame(data_window, text="Транспортные средства")
        vehicle_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        vehicle_tree = ttk.Treeview(vehicle_frame, columns=("Type", "Capacity", "Specific"), show="headings")
        vehicle_tree.heading("Type", text="Тип")
        vehicle_tree.heading("Capacity", text="Грузоподъемность")
        vehicle_tree.heading("Specific", text="Спецификация")

        for vehicle in self.company.vehicles:
            specific = f"{vehicle.max_altitude} м" if isinstance(vehicle, Airplane) else ("Да" if vehicle.is_refrigerated else "Нет")
            vehicle_tree.insert("", "end", values=(type(vehicle).__name__, vehicle.capacity, specific))

        vehicle_tree.pack(fill="both", expand="yes")
        vehicle_tree.bind("<Double-1>", self.edit_vehicle)

    def edit_client(self, event):
        selected_item = event.widget.selection()[0]
        values = event.widget.item(selected_item, "values")

        edit_client_window = tk.Toplevel(self.root)
        edit_client_window.title("Редактировать клиента")

        tk.Label(edit_client_window, text="Имя клиента:").pack()
        name_entry = tk.Entry(edit_client_window)
        name_entry.insert(0, values[0])
        name_entry.pack()

        tk.Label(edit_client_window, text="Вес груза (в тоннах):").pack()
        cargo_weight_entry = tk.Entry(edit_client_window)
        cargo_weight_entry.insert(0, values[1])
        cargo_weight_entry.pack()

        tk.Label(edit_client_window, text="VIP клиент? (y/n):").pack()
        is_vip_entry = tk.Entry(edit_client_window)
        is_vip_entry.insert(0, "y" if values[2] == "Да" else "n")
        is_vip_entry.pack()

        def save_edited_client():
            name = name_entry.get().strip()
            if not name:
                messagebox.showerror("Ошибка", "Имя клиента не может быть пустым.")
            elif re.search(r'\d', name):
                messagebox.showerror("Ошибка", "Имя клиента не может содержать цифры.")
            else:
                try:
                    cargo_weight = float(cargo_weight_entry.get())
                    if cargo_weight <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Ошибка", "Вес груза должен быть положительным числом.")
                    return

                is_vip_input = is_vip_entry.get().lower()
                if is_vip_input not in ['y', 'n']:
                    messagebox.showerror("Ошибка", "Ответ должен быть 'y' или 'n'.")
                    return

                is_vip = is_vip_input == 'y'

                # Обновление данных клиента в таблице
                event.widget.item(selected_item, values=(name, cargo_weight, "Да" if is_vip else "Нет"))

                # Обновление данных клиента в списке клиентов компании
                for client in self.company.clients:
                    if client.name == values[0] and client.cargo_weight == float(values[1]) and ("Да" if client.is_vip else "Нет") == values[2]:
                        client.name = name
                        client.cargo_weight = cargo_weight
                        client.is_vip = is_vip
                        break

                messagebox.showinfo("Успех", "Данные клиента обновлены.")
                edit_client_window.destroy()

        tk.Button(edit_client_window, text="Сохранить изменения", command=save_edited_client).pack(pady=5)

    def edit_vehicle(self, event):
        selected_item = event.widget.selection()[0]
        values = event.widget.item(selected_item, "values")

        edit_vehicle_window = tk.Toplevel(self.root)
        edit_vehicle_window.title("Редактировать транспортное средство")

        tk.Label(edit_vehicle_window, text="Грузоподъемность (в тоннах):").pack()
        capacity_entry = tk.Entry(edit_vehicle_window)
        capacity_entry.insert(0, values[1])
        capacity_entry.pack()

        specific_label = tk.Label(edit_vehicle_window)
        specific_label.pack()

        specific_entry = tk.Entry(edit_vehicle_window)
        specific_entry.pack()

        if values[0] == "Airplane":
            specific_label.config(text="Максимальная высота полета (в метрах):")
            specific_entry.insert(0, values[2][:-2])  # Убираем ' м' из значения
        else:
            specific_label.config(text="Холодильник? (y/n):")
            specific_entry.insert(0, "y" if values[2] == "Да" else "n")

        def save_edited_vehicle():
            try:
                capacity = float(capacity_entry.get())
                if capacity <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Ошибка", "Грузоподъемность должна быть положительным числом.")
                return

            if values[0] == "Airplane":
                try:
                    max_altitude = int(specific_entry.get())
                    if max_altitude <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Ошибка", "Высота полета должна быть положительным числом.")
                    return
                specific_value = f"{max_altitude} м"
            else:
                is_refrigerated_input = specific_entry.get().lower()
                if is_refrigerated_input not in ['y', 'n']:
                    messagebox.showerror("Ошибка", "Ответ должен быть 'y' или 'n'.")
                    return
                specific_value = "Да" if is_refrigerated_input == 'y' else "Нет"

            # Обновление данных транспортного средства в таблице
            event.widget.item(selected_item, values=(values[0], capacity, specific_value))

            # Обновление данных транспортного средства в списке транспортных средств компании
            for vehicle in self.company.vehicles:
                if type(vehicle).__name__ == values[0] and vehicle.capacity == float(values[1]):
                    vehicle.capacity = capacity
                    if isinstance(vehicle, Airplane):
                        vehicle.max_altitude = max_altitude
                    else:
                        vehicle.is_refrigerated = is_refrigerated_input == 'y'
                    break

            messagebox.showinfo("Успех", "Данные транспортного средства обновлены.")
            edit_vehicle_window.destroy()

        tk.Button(edit_vehicle_window, text="Сохранить изменения", command=save_edited_vehicle).pack(pady=5)

    def distribute_cargo(self):
        self.company.optimize_cargo_distribution()
        self.show_load_distribution()

    def show_load_distribution(self):
        distribution_window = tk.Toplevel(self.root)
        distribution_window.title("Загрузка транспортных средств")

        vehicles = self.company.list_vehicles()
        if vehicles:
            for vehicle in vehicles:
                load_info = f"{vehicle} - Загрузка: {vehicle.get_load_percentage():.2f}%"
                tk.Label(distribution_window, text=load_info).pack()
        else:
            tk.Label(distribution_window, text="Транспортных средств нет.").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()

