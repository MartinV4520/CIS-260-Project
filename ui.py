import tkinter as tk
from tkinter import messagebox
from classify_url import classify

root = tk.Tk()
root.title("Phishing URL Detector")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

def on_classify():
    url = url_entry.get()
    prediction, confidence, model_name = classify(url)
    label = "Phishing" if prediction == 1 else "Legitimate"
    messagebox.showinfo("Result", f"Prediction: {label}\nConfidence: {confidence:.2f}\nModel: {model_name}")

classify_button = tk.Button(root, text="Check URL", command=on_classify)
classify_button.pack()

root.mainloop()
