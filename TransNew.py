import os
import uuid
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound


class Transpad:
    def __init__(self, width=600, height=400):
        self.root = tk.Tk()
        self.root.title("Transpad")

        # Window size & centering
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = int((screen_w - width) / 2)
        y = int((screen_h - height) / 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Text Area
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scrollbar.set)

        self.file_path = None
        self.create_menu()

    # ---------------- MENU ---------------- #

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # AI menu
        ai_menu = tk.Menu(menu_bar, tearoff=0)
        ai_menu.add_command(label="Voice → Text", command=self.voice_to_text)
        ai_menu.add_command(label="Text → Voice", command=self.text_to_voice)
        menu_bar.add_cascade(label="AI", menu=ai_menu)

        # Language menu
        lang_menu = tk.Menu(menu_bar, tearoff=0)
        languages = {
            "English": "en",
            "Hindi": "hi",
            "Japanese": "ja",
            "Chinese": "zh-CN",
            "Arabic": "ar",
            "German": "de",
            "Korean": "ko",
            "Marathi": "mr",
            "Bengali": "bn",
            "Urdu": "ur",
        }

        for name, code in languages.items():
            lang_menu.add_command(
                label=name,
                command=lambda c=code: self.translate_text(c)
            )

        menu_bar.add_cascade(label="Translate", menu=lang_menu)

        # Help
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(
            label="About",
            command=lambda: messagebox.showinfo("About", "Transpad\nAI Enabled Notepad")
        )
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    # ---------------- FILE OPS ---------------- #

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Untitled - Transpad")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not path:
            return

        with open(path, "r", encoding="utf-8") as file:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, file.read())

        self.file_path = path
        self.root.title(os.path.basename(path) + " - Transpad")

    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")]
            )
            if not self.file_path:
                return

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(self.text_area.get(1.0, tk.END))

        self.root.title(os.path.basename(self.file_path) + " - Transpad")

    # ---------------- AI FEATURES ---------------- #

    def voice_to_text(self):
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                messagebox.showinfo("Voice Input", "Speak now...")
                audio = recognizer.listen(source, timeout=5)

            text = recognizer.recognize_google(audio)
            self.text_area.insert(tk.END, text + "\n")

        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Network error")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def text_to_voice(self):
        text = self.text_area.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Text area is empty")
            return

        filename = f"{uuid.uuid4()}.mp3"

        try:
            tts = gTTS(text=text, lang="en")
            tts.save(filename)

            threading.Thread(
                target=self.play_audio,
                args=(filename,),
                daemon=True
            ).start()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def play_audio(self, filename):
        playsound(filename)
        os.remove(filename)

    def translate_text(self, lang_code):
        text = self.text_area.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Text area is empty")
            return

        try:
            translated = GoogleTranslator(
                source="auto",
                target=lang_code
            ).translate(text)

            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, translated)

        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    # ---------------- RUN ---------------- #

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Transpad()
    app.run()
