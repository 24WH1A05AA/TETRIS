from tkinter import *
from textblob import TextBlob
import pandas as pd

# ---------- THEME COLORS ----------
BG_COLOR = "#222831"       # dark gray background
TEXT_BG = "#393E46"        # text box background
BTN_COLOR = "#00ADB5"      # teal button
BTN_HOVER = "#04C2C9"      # lighter teal
POS_COLOR = "#03C988"      # green
NEG_COLOR = "#F45050"      # red
NEU_COLOR = "#EEEEEE"      # light gray

# ---------- MAIN WINDOW ----------
root = Tk()
root.title("Sentiment Analyzer 🧠")
root.geometry("500x500")
root.config(bg=BG_COLOR)

# ---------- TITLE ----------
title = Label(root, text="Sentiment Analyzer", font=("Segoe UI", 20, "bold"),
              bg=BG_COLOR, fg="#EEEEEE")
title.pack(pady=15)

# ---------- TEXT INPUT ----------
Label(root, text="Enter your text or review below:", font=("Segoe UI", 12),
      bg=BG_COLOR, fg="#EEEEEE").pack(pady=5)

input_text = Text(root, height=8, width=50, wrap=WORD, font=("Segoe UI", 11),
                  bg=TEXT_BG, fg="#FFFFFF", insertbackground="white", relief=FLAT, padx=10, pady=10)
input_text.pack(pady=10)

# ---------- RESULT LABEL ----------
result_label = Label(root, text="", font=("Segoe UI", 14, "bold"), bg=BG_COLOR)
result_label.pack(pady=20)

# ---------- FUNCTIONS ----------
def analyze_sentiment():
    text = input_text.get("1.0", END).strip()
    if not text:
        result_label.config(text="⚠️ Please enter text!", fg="orange")
        return

    blob = TextBlob(text)
    score = blob.sentiment.polarity

    if score > 0.1:
        sentiment = "😊 Positive"
        color = POS_COLOR
    elif score < -0.1:
        sentiment = "☹️ Negative"
        color = NEG_COLOR
    else:
        sentiment = "😐 Neutral"
        color = NEU_COLOR

    result_label.config(text=f"{sentiment}\n(Score: {score:.2f})", fg=color)

    # simple animation effect
    for i in range(3):
        result_label.after(100, lambda: result_label.config(font=("Segoe UI", 15, "bold")))
        result_label.after(200, lambda: result_label.config(font=("Segoe UI", 14, "bold")))

def clear_text():
    input_text.delete("1.0", END)
    result_label.config(text="")

# ---------- BUTTONS ----------
def on_enter(e):
    e.widget.config(bg=BTN_HOVER)
def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

analyze_btn = Button(root, text="Analyze Sentiment", command=analyze_sentiment,
                     bg=BTN_COLOR, fg="white", font=("Segoe UI", 12, "bold"),
                     activebackground=BTN_HOVER, relief=FLAT, padx=15, pady=5, cursor="hand2")
analyze_btn.pack(pady=5)
analyze_btn.bind("<Enter>", on_enter)
analyze_btn.bind("<Leave>", on_leave)

clear_btn = Button(root, text="Clear", command=clear_text,
                   bg="#FFB703", fg="black", font=("Segoe UI", 11, "bold"),
                   activebackground="#FFD166", relief=FLAT, padx=10, pady=5, cursor="hand2")
clear_btn.pack(pady=5)

# ---------- FOOTER ----------
Label(root, text="Made with ❤️ in Python", font=("Segoe UI", 9),
      bg=BG_COLOR, fg="#888888").pack(side=BOTTOM, pady=10)

root.mainloop()

