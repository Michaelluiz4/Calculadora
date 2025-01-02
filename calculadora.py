from tkinter import *

class Calculadora:
    def __init__(self, primeiro_numero=0, segundo_numero=0):
        self.primeiro_numero = primeiro_numero
        self.segundo_numero = segundo_numero

    
    def entrada(self):
        try:
            self.primeiro_numero = float(input('Primeiro número: '))
            self.segundo_numero = float(input('Segundo número: '))
        except ValueError:
            print('Erro. Digite apenas números.')
            self.entrada()


    def opcoes(self):
        print('1 - Soma')
        print('2 - Subtração') 
        print('3 - Multiplicação') 
        print('4 - divisão')

        #self.opcao = int(input('Escolha a opção desejada: '))


    def soma(self):
        return self.primeiro_numero + self.segundo_numero


    def subtracao(self):
        return self.primeiro_numero - self.segundo_numero


    def multiplicacao(self):
        return self.primeiro_numero * self.segundo_numero


    def divisao(self):
        try:
            return self.primeiro_numero / self.segundo_numero
        except ZeroDivisionError:
            return 'Erro. Não é possível fazer divisão por zero.'


    def resultado(self):
        self.opcoes()

        if self.opcao == 1:
            return self.soma()
        elif self.opcao == 2:
            return self.subtracao()
        elif self.opcao == 3:
            return self.multiplicacao()
        elif self.opcao == 4:
            return self.divisao()
        else:
            return 'Erro. Escolha uma opção válida.'



windows = Tk()
windows.title('Calculadora')
windows.geometry('600x700')

text = Label(windows, text='', width=10, height=10)
text.grid(row=0, column=0)

botao7 = Button(windows, text='7', width=10, height=7)
botao7.grid(row=1, column=0)

botao8 = Button(windows, text='8', width=10, height=7)
botao8.grid(row=1, column=1)

botao9 = Button(windows, text='9', width=10, height=7)
botao9.grid(row=1, column=2)

botao4 = Button(windows, text='4', width=10, height=7)
botao4.grid(row=2, column=0)

botao5 = Button(windows, text='5', width=10, height=7)
botao5.grid(row=2, column=1)

botao6 = Button(windows, text='6', width=10, height=7)
botao6.grid(row=2, column=2)

botao1 = Button(windows, text='1', width=10, height=7)
botao1.grid(row=3, column=0)

botao2 = Button(windows, text='2', width=10, height=7)
botao2.grid(row=3, column=1)

botao3 = Button(windows, text='3', width=10, height=7)
botao3.grid(row=3, column=2)

botao0 = Button(windows, text='0', width=10, height=7)
botao0.grid(row=4, column=0)


windows.mainloop()