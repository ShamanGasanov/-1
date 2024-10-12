import tkinter as tk
from tkinter import filedialog, messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Заметки")
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        # Создаем меню
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Сохранить", command=self.save_note)
        file_menu.add_command(label="Открыть", command=self.open_note)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_app)

        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Правка", menu=edit_menu)
        edit_menu.add_command(label="Очистить", command=self.clear_note)

    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Сохранение", "Заметка сохранена!")

    def open_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)

    def clear_note(self):
        self.text_area.delete("1.0", tk.END)
        messagebox.showinfo("Очистка", "Заметка очищена!")

    def exit_app(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
