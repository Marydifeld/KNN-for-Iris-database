import tkinter as tk
from KNN import *
window = tk.Tk()
window.geometry("400x300")


def main():
    
    

    label = tk.Label(text = "KNN for iris database")
    label.pack()

    label1 = tk.Label(window, text="Sepal length")
    label1.pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    label2 = tk.Label(window, text="Sepal width")
    label2.pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    label3 = tk.Label(window, text="Petal length")
    label3.pack()
    entry3 = tk.Entry(window)
    entry3.pack()

    label4 = tk.Label(window, text="Petal width")
    label4.pack()
    entry4 = tk.Entry(window)
    entry4.pack()

    label5 = tk.Label(window, text="k")
    label5.pack()
    entry5 = tk.Entry(window)
    entry5.pack()

    #Button
    execute_button = tk.Button(window, text="Execute", command=lambda: execute(entry1, entry2, entry3, entry4, entry5))
    execute_button.pack()

 
def execute(entry1, entry2, entry3, entry4, entry5):
    try:
        s_length = float(entry1.get())
        s_width = float(entry2.get())
        p_length = float(entry3.get())
        p_width = float(entry4.get())
        k = int(entry5.get())   
    except:
        print("Not suported format")
    result = (run_knn(s_length, s_width,p_length,p_width,k ))
    for i in window.winfo_children():
        i.destroy()
    label_result = tk.Label(window, text= result, wraplength=350, justify="left")
    label_result.pack(pady=50)
    again = tk.Button(window, text="Again", command= reset)
    again.pack()

def reset():
    for i in window.winfo_children():
        i.destroy()
    main()



main()
window.mainloop()

 


