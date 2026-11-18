import tkinter as tk



def po_kliknieciu() :
    print("kliknieto guzik!!")









okno = tk.Tk()
okno.title("moje okienko z guzikiem!!")
okno.geometry("300x150")
przycisk = tk.Button(okno, text="kliknij mnie!!", command=po_kliknieciu)
przycisk.pack(pady=30, padx=50,)
















okno.mainloop()
