# Autor: Gabriela Souza
# Projeto Padrão - Visual

# instalar o pacote do customtkinter
# pip install customtkinter

# importação da biblioteca
import customtkinter as ctk

# configurações visuais
ctk.set_appearance_mode('dark') #Modos 'light' e 'dark'
ctk.set_default_color_theme('blue') #Temas 'blue', 'dark-blue', 'green'

janela = ctk.CTk()
janela.geometry('800x600')
janela.title('Conversor de Temperatura')

# criação de elementos da tela
entrada = ctk.CTkEntry(janela, placeholder_text='Digite a temperatura em °C: ')
entrada.pack(pady=20)

janela.mainloop()