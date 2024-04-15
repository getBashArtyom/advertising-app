import tkinter as tk
from search import find_nearest_banners

class BannerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Поиск ближайших баннеров")
        self.geometry("600x400")

        # Создаем поля для ввода координат и цены
        self.label_lat = tk.Label(self, text="Широта:")
        self.label_lat.grid(row=0, column=0)
        self.entry_lat = tk.Entry(self)
        self.entry_lat.grid(row=0, column=1)

        self.label_lon = tk.Label(self, text="Долгота:")
        self.label_lon.grid(row=1, column=0)
        self.entry_lon = tk.Entry(self)
        self.entry_lon.grid(row=1, column=1)

        self.label_price = tk.Label(self, text="Максимальная цена:")
        self.label_price.grid(row=2, column=0)
        self.entry_price = tk.Entry(self)
        self.entry_price.grid(row=2, column=1)

        # Создаем кнопку для выполнения поиска
        self.button_search = tk.Button(self, text="Найти ближайшие баннеры", command=self.search_banners)
        self.button_search.grid(row=3, column=0, columnspan=2)

        # Создаем текстовое поле для вывода результатов
        self.text_results = tk.Text(self)
        self.text_results.grid(row=4, column=0, columnspan=2)

    def search_banners(self):
        # Получаем значения из полей ввода
        user_lat = float(self.entry_lat.get())
        user_lon = float(self.entry_lon.get())
        max_price = float(self.entry_price.get())

        # Выполняем поиск ближайших баннеров
        nearest_banners = find_nearest_banners(user_lat, user_lon, max_price)

        # Очищаем текстовое поле
        self.text_results.delete(1.0, tk.END)

        # Выводим результаты в текстовое поле
        for banner in nearest_banners:
            self.text_results.insert(tk.END, f"Баннер: {banner['id']}\nРасстояние: {banner['distance']} км\nСтатус: {banner['status']}\n\n")

if __name__ == "__main__":
    app = BannerApp()
    app.mainloop()
