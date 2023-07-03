import tkinter as tk
from tkinter import filedialog
import csv
import codecs

def select_file():
    file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=(("CSV Files", "*.csv"),))
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def convert_csv():
    file_path = file_entry.get()

    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)

                data = [row for row in reader]

            output_file_path = filedialog.asksaveasfilename(title="Save Converted CSV File", defaultextension=".csv")

            if output_file_path:
                with codecs.open(output_file_path, 'w', 'utf-8-sig') as csv_file:
                    writer = csv.writer(csv_file)


                    writer.writerows(data)

                result_label.config(text="CSV file converted successfully!", fg="green")
            else:
                result_label.config(text="Output file not selected.", fg="red")
        except :
            with open(file_path, 'r', encoding='latin-1') as csv_file:
                reader = csv.reader(csv_file)

                data = [row for row in reader]

            output_file_path = filedialog.asksaveasfilename(title="Save Converted CSV File", defaultextension=".csv")

            if output_file_path:
                with codecs.open(output_file_path, 'w', 'utf-8-sig') as csv_file:
                    writer = csv.writer(csv_file)


                    writer.writerows(data)

                result_label.config(text="CSV file converted successfully!", fg="green")
            else:
                result_label.config(text="Output file not selected.", fg="red")
    
    else:
        result_label.config(text="Input file not selected.", fg="red")

window = tk.Tk()
window.title("CSV Converter")
window.geometry("400x150")

file_label = tk.Label(window, text="Select CSV File:")
file_label.pack()

file_entry = tk.Entry(window, width=40)
file_entry.pack(pady=10)

select_button = tk.Button(window, text="Select", command=select_file)
select_button.pack()

convert_button = tk.Button(window, text="Convert CSV", command=convert_csv)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
