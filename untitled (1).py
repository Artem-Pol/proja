import tkinter as tk
import random
import json

# Предопределённые цитаты
quotes = [
    {"text": "Будьте тем изменением, которое вы хотите видеть в мире.", "author": "Махатма Ганди", "topic": "Изменение"},
    {"text": "Жизнь — это то, что происходит, пока вы заняты строить другие планы.", "author": "Джон Леннон", "topic": "Жизнь"},
    {"text": "Никогда не сдавайтесь, даже если это кажется невозможным.", "author": "Уинстон Черчилль", "topic": "Настойчивость"},
]

# Инициализация главного окна
root = tk.Tk()
root.title("Random Quote Generator")

quote_text = tk.StringVar()
history = []

# Отображение текущец цитаты
quote_label = tk.Label(root, textvariable=quote_text, wraplength=400)
quote_label.pack(pady=20)

# Список для истории цитат
history_listbox = tk.Listbox(root, width=50, height=10)
history_listbox.pack(pady=10)

# Генерация случайной цитаты
def generate_quote():
    quote = random.choice(quotes)
    quote_display = f"{quote['text']} - {quote['author']} ({quote['topic']})"
    quote_text.set(quote_display)
    add_to_history(quote_display)

# Добавление цитаты в историю
def add_to_history(quote):
    history.append(quote)
    history_listbox.insert(tk.END, quote)

# Сохранение истории в JSON
def save_history():
    with open('history.json', 'w') as f:
        json.dump(history, f)

# Загрузка истории из JSON
def load_history():
    global history
    try:
        with open('history.json', 'r') as f:
            history = json.load(f)
            for item in history:
                history_listbox.insert(tk.END, item)
    except FileNotFoundError:
        history = []

# Проверка на пустые строки
def add_quote(text, author, topic):
    if text and author and topic:
        quotes.append({"text": text, "author": author, "topic": topic})

# Кнопки
generate_button = tk.Button(root, text="Сгенерировать цитату", command=generate_quote)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Сохранить историю", command=save_history)
save_button.pack(pady=10)

# Загрузка истории при запуске
load_history()

# Запуск приложения
root.mainloop()