import threading
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from deep_translator import GoogleTranslator


class Transpad:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Translate Pad")
        self.root.geometry("800x400")

        # Input text box
        tk.Label(self.root, text="Live Speech Input").pack()
        self.input_box = tk.Text(self.root, height=8)
        self.input_box.pack(fill=tk.BOTH, expand=True)

        # Output text box
        tk.Label(self.root, text="Live Translated Output").pack()
        self.output_box = tk.Text(self.root, height=8, fg="green")
        self.output_box.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.root, text="Start Live Translation", command=self.start_live).pack()

        self.running = False
        self.recognizer = sr.Recognizer()
        self.translator = GoogleTranslator(source='auto', target='hi')  # Hindi output

    # ---------------- PARALLEL PROCESS ---------------- #

    def start_live(self):
        if self.running:
            return

        self.running = True
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)

                while self.running:
                    audio = self.recognizer.listen(source, phrase_time_limit=3)

                    try:
                        text = self.recognizer.recognize_google(audio)
                        self.update_input(text)
                        self.translate_parallel(text)

                    except sr.UnknownValueError:
                        pass
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def translate_parallel(self, text):
        threading.Thread(
            target=self.translate_text,
            args=(text,),
            daemon=True
        ).start()

    def translate_text(self, text):
        try:
            translated = self.translator.translate(text)
            self.update_output(translated)
        except:
            pass

    # ---------------- SAFE GUI UPDATE ---------------- #

    def update_input(self, text):
        self.root.after(
            0, lambda: self.input_box.insert(tk.END, text + " ")
        )

    def update_output(self, text):
        self.root.after(
            0, lambda: self.output_box.insert(tk.END, text + " ")
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Transpad()
    app.run()
