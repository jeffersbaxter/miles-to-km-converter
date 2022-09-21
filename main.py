from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=340)
window.config(padx=21, pady=21)

KM_CONVERSION = 1.60934


def calculate_to_km():
    miles = float(miles_entry.get())
    km_display.config(text=f"{round((miles * KM_CONVERSION), 2)}")


miles_entry = Entry()
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 21, "bold"))
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to", font=("Arial", 21, "bold"))
equal_to_label.grid(row=1, column=0)

km_display = Label(text="0", font=("Arial", 21, "bold"))
km_display.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 21, "bold"))
km_label.grid(row=1, column=2)

calculate_btn = Button(text="Calculate", command=calculate_to_km)
calculate_btn.grid(row=2, column=1)

window.mainloop()