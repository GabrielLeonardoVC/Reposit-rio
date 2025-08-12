import re
import os
def limpar():
    os.system("cls")
input(" ______________________\n |                    |\n |                    |\n |      Cadastro      |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir.\nClique em qualquer tecla para continuar... ")
os.system("cls")
while True:
    while True:
        nome = input("Digite seu nome (apenas letras)\n-->")
        if nome.replace(" ", "").isalpha():
            nome = nome.title()
            break
        else:
            print("Erro! Digite apenas letras (sem espaços ou símbolos).")
    os.system("cls")

    while True:
        idade = input("Digite sua idade (apenas números)\n-->")
        if idade.isdigit() and 0 < int(idade) <= 999:
            break
        else:
            print("Erro! Digite uma idade válida (número positivo até 3 dígitos).")
    os.system("cls")

    while True:
        cpf = input("Digite seu CPF (11 Digitos, apenas números)\n-->")
        if cpf.isdigit()and len(cpf) ==11:
            print("CPF validado")
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break
        else:
            print("Erro! Digite apenas 11 digitos e somente números.")
    os.system("cls")

    while True:
        rg = input("Digite seu RG (7 a 9 dígitos, somente números)\n-->").strip()
        if rg.isdigit() and 7 <= len(rg) <= 9:
            rg = rg.zfill(9)  # Preenche com zeros à esquerda até ter 9 dígitos
            rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8]}"
            break
        else:
            print("Erro! Digite de 7 a 9 dígitos, apenas números.")
    os.system("cls")
            
    while True:
            email = input("Digite seu e-mail.\n-->").strip()
            padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(padrao_email, email):
                break
            else:
                print("Erro! Digite um e-mail válido (exemplo:usuario@usuario.com)")
    os.system("cls")

    while True:
        senha = input("Digite sua senha.(Máximo 8 Caracteres)\n-->")
        if len(senha) <=8:
            break
        else:
            print("Erro. Digite no máxímo 8 caracteres")
    os.system("cls")

    print("Iremos configurar uma pergunta secreta para recuperação de senha.")
    while True:
        pergunta = input("Digite sua pergunta\n-->")
        if pergunta:
            break
    while True:
        resposta = input("Digite sua resposta\n-->")
        if resposta.replace(" ", ""):
            resposta = resposta.strip().lower()
            break
        else:
            print("Erro! Digite novamente.")
    os.system("cls")
    
    print("Veja se seus dados estão corretos a seguir...")
    os.system("cls")
    print(f"Nome:{nome}")
    print(f"Idade:{idade} anos")
    print(f"CPF:{cpf_formatado}")
    print(f"RG:{rg_formatado}")
    print(f"E-mail:{email}")
    print(f"Senha:{senha}")
    print(f"Pergunta secreta:{pergunta}")
    print(f"Resposta secreta:{resposta}")

    simounao = input("\nSeus dados estão corretos? Digite 'Sim' para continuar ou 'Não' para corrigirmos seu erro.\n--> ").strip().lower()
    if simounao in ['sim','s','si','sm','ss','SIM','S','SI','SM','SS']:
        print("\nCadastro concluído com sucesso!")
        break
    else:
        print("\nVamos refazer o seu cadastro.\n")
        input("Pressione Enter para continuar...")
        os.system("cls")
limpar()
print("______________________\n |                    |\n |                    |\n |        Login       |\n |                    |\n |____________________|\n\nRealize seu Login a seguir.\nClique em qualquer tecla para continuar... ")
os.system("cls")

while True:
    print("Vamos realizar seu Login a seguir. Siga os passos a seguir digitando apenas 1 ou 2.")
    print("1 - Fazer login")
    print("2 - Esqueci minha senha")
    opcao = input("Escolha uma opção (1 ou 2)\n-->").strip()

    if opcao not in ["1", "2"]:
        print("Opção inválida! Digite apenas 1 ou 2")
        continue
    limpar()
        
    if opcao == "1":
        nomelogin = input("Digite seu nome de usuário\n-->").strip().title()
        limpar()
        senhalogin = input("Digite sua senha\n-->").strip()
        limpar()

        if nomelogin==nome and senhalogin == senha:
            print(f"Bem-vindo, {nome}!")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.\n")
    
    elif opcao == "2":
        print(" _____________________________________\n |                                   |\n |                                   |\n |        Recuperação de Senha       |\n |                                   |\n |___________________________________|")
        print(f"Pergunta:\n-->{pergunta}")
        tentativa = input("Resposta:\n-->").strip().lower()
        limpar()
        
        if tentativa == resposta:
                while True:
                    nova_senha = input("Digite sua NOVA senha (Máximo 8 caracteres)\n-->")
                    if len(nova_senha) <=8:
                        senha=nova_senha
                    print("Sua senha foi redefinida com sucesso!")
                    input("Preciose qualquer tecla para retornar ao login...")
                    limpar()
                    break
        else:
                    print("Erro!Sua senha deve conter no máximo 8 caracteres.")
    else:
            print("Resposta incorreta.Não foi possivel redefinir sua senha!")