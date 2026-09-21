import json

def criar(conta):
    criar_conta = {
        nome_input : input("Qual é o seu nome? "),
        cpf : input("Qual é o seu CPF? "),
        celular : input("Qual é o seu número? "),
        email : input("Qual é o seu e-mail? "),
        idade : input("Qual é a sua idade? "),
        estado_civil : input("És casado(a) ou solteiro(a)?"),
        agencia : input("Qual agencia fornece sua conta?"),
        endereco: {
            endereço : input("Qual é o seu endereço?"),
            CEP : int(input("Qual é o seu CEP?")),
            Rua : input("Qual é a sua rua?"),
        }
    }
def carregar_conta():

    try:
        with open("conta.json", "r", encoding="utf-8") as f:
            return 
    except FileNotFoundError:
        return None

def salvar_conta(conta):
    try:
        with open("conta.json", "w", encoding="utf-8") as f:
            json.dump(conta, f, ensure_ascii=False, indent=2)
        print("Conta salva com sucesso!")
    except Exception as e:
        print(f"Erro ao guardar: {e}")
# Fase 2:
def depositar(conta, valor):
    if valor <= 0:
        print("O valor do depósito deve ser positivo.")
        return
    conta["saldo"] += valor
    conta["historico"].append(f"Depósito de R$ {valor:.2f}")
    print(f"Depósito realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def sacar(conta, valor):
    if valor <= 0:
        print("O valor do levantamento deve ser positivo.")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente para esse levantamento.")
        return
    conta["saldo"] -= valor
    conta["historico"].append(f"Levantamento de R$ {valor:.2f}")
    print(f"Levantamento realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def extrato(conta):
    print(f"\n--- EXTRATO DE {conta['titular'].upper()}---")
    if not conta["historico"]:
        print("Nenhuma movimentação ainda.")
    else:
        for movimento in conta["historico"]:
            print(f" {movimento}")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

print("--- BEM VINDO AO PYBANK ---")
conta = carregar_conta()

if conta is None:
    nome_input = input("Não encontramos nenhuma conta. Digite [1] para criar uma conta: ")
    nome_input : input("Qual é o seu nome? ")
    cpf : int(input("Qual é o seu CPF? "))
    celular : int(input("Qual é o seu número? "))
    email : (input("Qual é o seu e-mail? "))
    idade : int(input("Qual é a sua idade? "))
    estado_civil : input("És casado(a) ou solteiro(a)?")
    agencia : input("Qual agencia fornece sua conta?")
    endereço : int(input("Qual é o seu endereço?"))
    CEP : int(input("Qual é o seu CEP?"))
    rua : input("Qual é a sua rua?")
    if nome_input == "1":
        criar(conta)

    conta = {
        "titular" : nome_input,
        "saldo" : 0.0,
        "historico": []
    }
else:
    print(f"Bem vindo de volta, {conta['titular']}!")

while True:
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    opcao = input("[1] Depositar | [2] Levantar | [3] Extrato | [4] Guardar e Sair: ")

    if opcao == "1" or opcao == "2":
        try:
            valor = float(input("Valor: R$"))
        except ValueError:
            print("Digite um número válido.")
            continue
        if opcao == "1":
            depositar(conta, valor)
        else:
            sacar(conta, valor)

    elif opcao == "3":
        extrato(conta)

    elif opcao == "4":
        salvar_conta(conta)
        break

    else:
        print("Opção inválida.")