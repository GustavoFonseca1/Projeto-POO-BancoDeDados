import random

class ContaCorrente:
    def __init__(self, titular, senha):
        self.titular = titular
        self.conta = random.randint(100, 999)
        self.senha = senha
        self.saldoC = 0.0

    def sacar(self, valor):
        if valor <= self.saldoC:
            self.saldoC -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        if valor > 0:
            self.saldoC += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def aplicar(self, valor, conta_poupanca):
        if valor <= self.saldoC:
            self.saldoC -= valor
            conta_poupanca.saldoP += valor
            print(f"Aplicação de R${valor:.2f} realizada com sucesso!")
        else:
            print("Saldo insuficiente para aplicar.")


class ContaPoupanca:
    def __init__(self):
        self.saldoP = 0.0

    def resgatar(self, valor, conta_corrente):
        if valor <= self.saldoP:
            self.saldoP -= valor
            conta_corrente.saldoC += valor
            print(f"Resgate de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente na poupança.")

    def extrato(self, conta_corrente):
        print("\n=== Extrato ===")
        print(f"Saldo da Conta Corrente: R${conta_corrente.saldoC:.2f}")
        print(f"Saldo da Poupança: R${self.saldoP:.2f}\n")

def cadastrar_senha():
    while True:
        senha = input("Digite uma senha de 4 dígitos: ")
        if senha.isdigit() and len(senha) == 4:
            return senha
        else:
            print("Senha inválida! Digite uma senha de 4 dígitos.")

def verificacao_de_senha(senha_cadastrada):
    for i in range(3):
        senha_informada = input("Digite sua senha: ")
        if senha_informada == senha_cadastrada:
            return True
        else:
            tentativas_restantes = 2 - i
            if tentativas_restantes > 0:
                print(f"Senha incorreta! Você tem mais {tentativas_restantes} tentativa(s).")
            else:
                print("Conta bloqueada.")
                return False

def main():
    print("=== Bem-vindo ao Banco ===")
    titular = input("Digite o nome do titular: ")
    senha = cadastrar_senha()
    conta_corrente = ContaCorrente(titular, senha)
    conta_poupanca = ContaPoupanca()

    while True:
        print("\n=== Menu ===")
        print("1. Extrato")
        print("2. Depositar na Conta Corrente")
        print("3. Sacar da Conta Corrente")
        print("4. Aplicar na Poupança")
        print("5. Resgatar da Poupança")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if verificacao_de_senha(conta_corrente.senha):
                conta_poupanca.extrato(conta_corrente)
        elif opcao == "2":
            if verificacao_de_senha(conta_corrente.senha):
                valor = float(input("Valor para depósito: "))
                conta_corrente.depositar(valor)
        elif opcao == "3":
            if verificacao_de_senha(conta_corrente.senha):
                valor = float(input("Valor para saque: "))
                conta_corrente.sacar(valor)
        elif opcao == "4":
            if verificacao_de_senha(conta_corrente.senha):
                valor = float(input("Valor para aplicar na poupança: "))
                conta_corrente.aplicar(valor, conta_poupanca)
        elif opcao == "5":
            if verificacao_de_senha(conta_corrente.senha):
                valor = float(input("Valor para resgatar da poupança: "))
                conta_poupanca.resgatar(valor, conta_corrente)
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
