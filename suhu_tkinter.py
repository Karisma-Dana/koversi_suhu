# from tkinter import * 
import tkinter as tk 

def eksekusi(): 
    user_input = Entry_tinggi.get()
    
    try:
        user_info = float(user_input)
        user_choice = int(choice.get())

        if user_choice == 1:
            reamur1 = 4/5 * user_info
            fahrenheit1 = (9/5 * user_info) + 32
            kelvin1 = user_info + 273
            hasil = f"Reamur: {reamur1:.2f}\nFahrenheit: {fahrenheit1:.2f}\nKelvin: {kelvin1:.2f}"
        elif user_choice == 2:
            celcius1 = 5/4 * user_info
            fahrenheit1 = (9/4 * user_info) + 32
            kelvin1 = (5/4 * user_info) + 273
            hasil = f"Celcius: {celcius1:.2f}\nFahrenheit: {fahrenheit1:.2f}\nKelvin: {kelvin1:.2f}"
        elif user_choice == 3:
            celcius1 = 5/9 * (user_info-32)
            reamur1 = 4/9 * (user_info-32)
            kelvin1 = 5/9 * (user_info-32) + 273
            hasil = f"Celcius: {celcius1:.2f}\nReamur: {reamur1:.2f}\nKelvin: {kelvin1:.2f}"
        elif user_choice == 4 :
            celcius1 = user_info-273
            reamur1 = 4/5 *(user_info-273)
            fahrenheit1 = 9/5 * (user_info-273) + 32
            hasil = f"Celcius: {celcius1:.2f}\nReamur: {reamur1:.2f}\nFahrenheit: {fahrenheit1:.2f}"
        else :
            hasil = "anda belum memilih opsi suhu awal"

        hasil_akhir.config(text=hasil)

    except ValueError:
        hasil_akhir.config(text="Masukkan angka yang valid.")


root = tk.Tk()
root.title("konversi satuan suhu")
root.geometry("250x260")
user_pilihan = tk.Label(root,text="masukan opsi satuan awal\n")
user_pilihan.pack()
#user pilihan awal 

choice = tk.IntVar()
celcius = tk.Radiobutton(root,text="Celcius",variable=choice,value=1,)
celcius.pack(anchor="w")
Reamur = tk.Radiobutton(root,text="reamur",variable=choice,value=2)
Reamur.pack(anchor="w")
Fahrenheit = tk.Radiobutton(root,text="Fahrenheit",variable=choice,value=3)
Fahrenheit.pack(anchor="w")
Kelvin = tk.Radiobutton(root,text="Kelvin",variable=choice,value=4,)
Kelvin.pack(anchor="w")

#------------------------------------------------------------------------------------------

label_tinggi = tk.Label (root, text = "suhu sesuai pilihan : ")
label_tinggi.pack()
Entry_tinggi = tk.Entry(root)
Entry_tinggi.pack()


tombol = tk.Button(root,text="Hitung",command=eksekusi)
tombol.pack()

hasil_akhir = tk.Label(root,text="")
hasil_akhir.pack()


root.mainloop()







0