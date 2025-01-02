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

        self.opcao = int(input('Escolha a opção desejada: '))


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


