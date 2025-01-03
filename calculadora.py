from tkinter import *
import re

class Calculadora:
    def __init__(self):
        self.operacao = ""  # String para armazenar a operação atual

    def atualizar_visor(self, valor):
        """Atualiza o visor da calculadora com o valor clicado."""
        self.operacao += str(valor)
        visor.config(text=self.operacao)

    def limpar_visor(self):
        """Limpa o visor."""
        self.operacao = ""
        visor.config(text=self.operacao)

    def calcular(self):
        """Avalia a operação no visor e exibe o resultado."""
        try:
            expressao = re.sub(r'(\d+)%(\d+)', r'(\1/100)*\2', self.operacao)
            resultado = eval(expressao)
            visor.config(text=str(resultado))
            self.operacao = str(resultado)  # Atualiza para continuar o cálculo
        except ZeroDivisionError:
            visor.config(text='Não é possível dividir por zero.')
        except Exception:
            visor.config(text="Erro")
            self.operacao = ""

# Criando a janela principal
windows = Tk()
windows.title("Calculadora")

# Instância da classe Calculadora
calculadora = Calculadora()

# Visor da calculadora
visor = Label(windows, text="", font=("Arial", 24), bg="white", fg="black", height=2, anchor="e")
visor.grid(row=0, column=0, columnspan=4, sticky="ew")

# Função para criar botões dinamicamente
def criar_botao(texto, linha, coluna, largura=1, comando=None):
    botao = Button(
        windows, text=texto, width=10 * largura, height=4, font=("Arial", 16),
        command=comando
    )
    botao.grid(row=linha, column=coluna, columnspan=largura, sticky="ew")
    return botao

# Criando os botões
criar_botao("AC", 1, 0, largura=2, comando=calculadora.limpar_visor)
criar_botao("%", 1, 2, comando=lambda: calculadora.atualizar_visor("%"))
criar_botao("÷", 1, 3, comando=lambda: calculadora.atualizar_visor("/"))

criar_botao("7", 2, 0, comando=lambda: calculadora.atualizar_visor("7"))
criar_botao("8", 2, 1, comando=lambda: calculadora.atualizar_visor("8"))
criar_botao("9", 2, 2, comando=lambda: calculadora.atualizar_visor("9"))
criar_botao("X", 2, 3, comando=lambda: calculadora.atualizar_visor("*"))

criar_botao("4", 3, 0, comando=lambda: calculadora.atualizar_visor("4"))
criar_botao("5", 3, 1, comando=lambda: calculadora.atualizar_visor("5"))
criar_botao("6", 3, 2, comando=lambda: calculadora.atualizar_visor("6"))
criar_botao("-", 3, 3, comando=lambda: calculadora.atualizar_visor("-"))

criar_botao("1", 4, 0, comando=lambda: calculadora.atualizar_visor("1"))
criar_botao("2", 4, 1, comando=lambda: calculadora.atualizar_visor("2"))
criar_botao("3", 4, 2, comando=lambda: calculadora.atualizar_visor("3"))
criar_botao("+", 4, 3, comando=lambda: calculadora.atualizar_visor("+"))

criar_botao("0", 5, 0, largura=2, comando=lambda: calculadora.atualizar_visor("0"))
criar_botao(".", 5, 2, comando=lambda: calculadora.atualizar_visor("."))
criar_botao("=", 5, 3, comando=calculadora.calcular)

# Loop principal
windows.mainloop()
