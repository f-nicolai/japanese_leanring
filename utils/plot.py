import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from tkinter.font import Font




def display_kanji_and_wait(kanji:str=None, hiragana:str=None,romanji:str=None,word:str=None):
    def on_key_press(event):
        window.quit()  # This stops the mainloop for the current window
        window.destroy()  # This ensures the window is closed properly

    window = tk.Tk()
    window.title("Kanji Display")

    window.geometry("1000x800+300+100")

    # Bind the Enter key to the on_key_press function
    window.bind('<Return>', on_key_press)
    window.bind('<space>', on_key_press)

    center_frame = tk.Frame(window)
    center_frame.pack(expand=True)

    if kanji:
        kanji_font = tk.font.Font(family="Arial", size=200, weight="bold")
        kanji_label = tk.Label(center_frame, text=kanji, font=kanji_font)
        kanji_label.pack()

    if hiragana:
        hiragana_font = tk.font.Font(family="Arial", size=100, weight="bold")
        hiragana_label = tk.Label(center_frame, text=hiragana, font=hiragana_font)
        hiragana_label.pack()

    if romanji:
        romanji_font = tk.font.Font(family="Arial", size=100, weight="bold")
        romanji_label = tk.Label(center_frame, text=romanji, font=romanji_font)
        romanji_label.pack()

    if word:
        word_font = Font(family="Arial", size=100, weight="bold")
        word_label = tk.Label(center_frame, text=word, font=word_font)
        word_label.pack()


    window.mainloop()
