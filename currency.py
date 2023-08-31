from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

def convert_currency():
    amount = float(input_amount.get())
    from_currency = from_currency_combo.get()
    to_currency = to_currency_combo.get()
    
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    
    converted_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

root = Tk()
root.title("Currency Converter")
root.geometry("400x250")
root.config(bg="lightgray")

Label(root, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="lightgray").pack(pady=10)

input_frame = Frame(root, bg="lightgray")
input_frame.pack(pady=20)

Label(input_frame, text="Amount:", font=("Helvetica", 12), bg="lightgray").grid(row=0, column=0, padx=10)
input_amount = Entry(input_frame, font=("Helvetica", 12))
input_amount.grid(row=0, column=1, padx=10)

Label(input_frame, text="From Currency:", font=("Helvetica", 12), bg="lightgray").grid(row=1, column=0, padx=10)
from_currency_combo = ttk.Combobox(input_frame, values=["USD", "EUR", "GBP", "JPY", "INR"], font=("Helvetica", 12), state="readonly")
from_currency_combo.grid(row=1, column=1, padx=10)
from_currency_combo.set("USD")

Label(input_frame, text="To Currency:", font=("Helvetica", 12), bg="lightgray").grid(row=2, column=0, padx=10)
to_currency_combo = ttk.Combobox(input_frame, values=["USD", "EUR", "GBP", "JPY", "INR"], font=("Helvetica", 12), state="readonly")
to_currency_combo.grid(row=2, column=1, padx=10)
to_currency_combo.set("EUR")

convert_btn = Button(root, text="Convert", font=("Helvetica", 12, "bold"), command=convert_currency, bg="gray", fg="white")
convert_btn.pack(pady=10)

converted_label = Label(root, text="", font=("Helvetica", 14), bg="lightgray")
converted_label.pack()

root.mainloop()
