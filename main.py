from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date



# Cores
color1 = "#3b3b3b" # preto/escuro
color2 = "#333333" # preto/claro
color3 = "#FFFFFF" # branco
color4 = "#fcc058" # laranja


# Criando os primeiro componentes
window = Tk()
window.title("Calculadora de idade")
window.geometry("310x410")
window.configure(bg=color1)


style = ttk.Style(window)
style.theme_use("clam")

# Frames 
top_frame = Frame(window, width=310, height=140, pady=0, padx=0, relief="flat", bg=color2)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(window, width=310, height=270, pady=0, padx=0, relief="flat", bg=color1)
bottom_frame.grid(row=1, column=0, sticky=NW)

# Label Frames top_frame
app_calculador = Label(top_frame, text="Calcula Idade", width=25, height=1, padx=3, relief="flat", anchor="center", font=("Ivy 15 bold"), bg=color2, fg=color3)
app_calculador.place(x=0, y=30)

app_of_rage = Label(top_frame, text="Idade", width=11, height=1, padx=0, relief="flat", anchor="center", font=("Arial 35 bold"), bg=color2, fg=color3)
app_of_rage.place(x=0, y=70)


# Label Frames bottom_frame
l_inicial_date = Label(bottom_frame, text="Data Atual", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_inicial_date.place(x=50, y=30)

cal_inicial_date = DateEntry(bottom_frame, width=10, background="darkblue", foreground="white", borderWith=2, data_pattern="mm/dd/y", year=2026)
cal_inicial_date.place(x=170, y=30)

# ======================================================

l_birth_date = Label(bottom_frame, text="Data aniversario", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_birth_date.place(x=50, y=70)


cal_birth_date = DateEntry(bottom_frame, width=10, background="darkblue", foreground="white", borderWith=2, data_pattern="mm/dd/y", year=2026)
cal_birth_date.place(x=170, y=70)

app_years = Label(bottom_frame, text="27", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 25 bold"), bg=color1, fg=color3)
app_years.place(x=60, y=135)

app_years_label = Label(bottom_frame, text="Anos", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_years_label.place(x=50, y=175)

app_months = Label(bottom_frame, text="27", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 25 bold"), bg=color1, fg=color3)
app_months.place(x=140, y=135)

app_months_label = Label(bottom_frame, text="Meses", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_months_label.place(x=130, y=175)


app_days = Label(bottom_frame, text="27", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 25 bold"), bg=color1, fg=color3)
app_days.place(x=220, y=135)

app_days_label = Label(bottom_frame, text="Dias", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_days_label.place(x=210, y=175)


# Funcao calcular idade
def calcular_age():
    initial_date_str = cal_inicial_date.get_date()
    birth_date_str = cal_birth_date.get_date()

    data_mais_recente = max(initial_date_str, birth_date_str)
    data_mais_antiga = min(initial_date_str, birth_date_str)


    diferenca = relativedelta(data_mais_recente, data_mais_antiga)

    app_years["text"] = diferenca.years
    app_months["text"] = diferenca.months
    app_days["text"] = diferenca.days


b_calcular_age = Button(bottom_frame, text="Calcular Idade", width=20, height=1, bg=color1, fg=color3, font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE, command=calcular_age)
b_calcular_age.place(x=60, y=225)

window.mainloop()