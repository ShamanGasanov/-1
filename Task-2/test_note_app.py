import unittest
from unittest.mock import patch
import tkinter as tk
from note_app import NoteApp  
import _tkinter  

class TestNoteApp(unittest.TestCase):

    @patch('tkinter.filedialog.asksaveasfilename')
    @patch('tkinter.messagebox.showinfo')
    def test_save_note(self, mock_showinfo, mock_asksaveasfilename):
        mock_asksaveasfilename.return_value = 'test_note.txt'
        app = NoteApp(tk.Tk())
        app.text_area.insert(tk.END, "Тестовая заметка")
        app.save_note()
        
        # Проверка, что информация о сохранении была показана
        mock_showinfo.assert_called_with("Сохранение", "Заметка сохранена!")

    @patch('tkinter.filedialog.askopenfilename')
    def test_open_note(self, mock_askopenfilename):
        mock_askopenfilename.return_value = 'test_note.txt'
        app = NoteApp(tk.Tk())
        app.text_area.insert(tk.END, "Старая заметка")
        
        # Создаем файл для теста
        with open('test_note.txt', 'w', encoding='utf-8') as f:
            f.write("Загруженная заметка")
        
        app.open_note()
        
        # Проверка, что текстовая область содержит загруженный текст
        self.assertEqual(app.text_area.get("1.0", tk.END).strip(), "Загруженная заметка")

    @patch('tkinter.messagebox.askokcancel')
    def test_exit_app(self, mock_askokcancel):
        mock_askokcancel.return_value = True
        app = NoteApp(tk.Tk())

        # Вызываем метод выхода
        app.exit_app()

        # Проверяем, что приложение завершилось без ошибок
        try:
            exists = app.root.winfo_exists()
        except _tkinter.TclError:
            exists = False

        self.assertFalse(exists)  # Проверяем, что окно больше не существует

    @patch('tkinter.messagebox.showinfo')
    def test_clear_note(self, mock_showinfo):
        app = NoteApp(tk.Tk())
        app.text_area.insert(tk.END, "Тестовая заметка")
        
        # Вызываем метод очистки заметки
        app.clear_note()
        
        # Проверяем, что текстовая область пуста
        self.assertEqual(app.text_area.get("1.0", tk.END).strip(), "")
        
        # Проверка, что информация о очистке была показана
        mock_showinfo.assert_called_with("Очистка", "Заметка очищена!")

if __name__ == '__main__':
    unittest.main()















