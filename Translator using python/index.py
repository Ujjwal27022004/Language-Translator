import tkinter as tk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        self.heading_label = tk.Label(self.root, text="Real-Time Language Translator", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.text_label = tk.Label(self.root, text="Enter text:", font=("Helvetica", 12))
        self.text_label.pack()

        self.text_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.text_entry.pack(pady=5)

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text, font=("Helvetica", 12, "bold"), bg="green", fg="white")
        self.translate_button.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), wraplength=300)
        self.result_label.pack(pady=10)

    def translate_text(self):
        text_to_translate = self.text_entry.get()
        if text_to_translate:
            translation = self.translator.translate(text_to_translate, dest="en")  # Translate to English
            self.result_label.config(text=f"Translation: {translation.text}")
        else:
            self.result_label.config(text="Please enter text to translate.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
