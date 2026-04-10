# Autor: Gabriela Souza
# Projeto Padrão - Visual

# instalar o pacote do customtkinter
# pip install customtkinter

# importação da biblioteca
import customtkinter as ctk

# configurações visuais
ctk.set_appearance_mode('dark') #Modos 'light' e 'dark'
ctk.set_default_color_theme('dark-blue') #Temas 'blue', 'dark-blue', 'green'

janela = ctk.CTk()
# tamanho da janela
janela.geometry('800x600')
# titulo da janela
janela.title('Calculadora de IMC')



# Função no Python é def
def calcular():
    # o .get() pega o valor digitado dentro do input
    altura = float(entrada_altura.get())
    peso = float(entrada_peso.get())
    imc = peso / (altura ** 2)
    # o .configure() joga o resultado calculado na variável imc dentro da caixa onde aparecerá o resultado

    if imc <= 18.5:
        classificacao = 'Classificação: Abaixo do peso'
    elif imc <= 25:
        classificacao = 'Classificação: Peso normal'
    elif imc <= 30:
        classificacao = 'Classificação: Sobrepeso'
    else:
        classificacao = 'Classificação: Obesidade'
    
    resultado_label.configure (text = f'Seu IMC é de: {imc:.2f} \n {classificacao}')

# Criação de elementos da tela
# Entrada da altura do usuario
entrada_altura = ctk.CTkEntry(janela, 
                              width=360,
                              height=36,
                              font=('Arial', 12),
                              placeholder_text='Digite sua altura em metros: ')
entrada_altura.pack(pady=20)

# Entrada do peso do usuario
entrada_peso = ctk.CTkEntry(janela, 
                            width=360,
                            height=36,
                            font=('Arial', 12),
                            placeholder_text='Digite seu peso em quilos: ')
entrada_peso.pack(pady=20)

# Botão
resultado_botao = ctk.CTkButton(janela, 
                                width=360,
                                height=36,
                                font=('Arial', 12),
                                #arredonda as bordas
                                corner_radius= 16,
                                # chama a função ao clicar no botão
                                command= calcular,
                                text='Calcular')
resultado_botao.pack(pady=20)

# Resultado
resultado_label = ctk.CTkLabel(janela, text='')
resultado_label.pack(pady=20)





janela.mainloop()