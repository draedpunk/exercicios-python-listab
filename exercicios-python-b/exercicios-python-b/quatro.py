# QUESTAO 4:
# Desenvolva um programa em Python que simule o controle de empréstimos de livros em
# uma biblioteca. O programa deverá utilizar um dicionário (sem JSON) para armazenar os livros, onde
# as chaves representam os nomes dos livros e os valores indicam o status de
# disponibilidade ("Disponível" ou "Indisponível").
# O programa deve:
# • Exibir inicialmente a lista de livros e seus respectivos status para o usuário.(OK)
# • Permitir que o usuário insira o nome do livro que deseja emprestar.(OK)
# • Verificar no dicionário se o livro solicitado está marcado como "Disponível".
# o Se o livro estiver "Disponível", exibir uma mensagem de confirmação do
# empréstimo e atualizar o status do livro no dicionário para
# "Indisponível". (OK)
# o Se o livro estiver "Indisponível", informar ao usuário que ele já foi
# emprestado.

# • Continuar o processo de empréstimo até que o usuário decida encerrar o
# programa (Ex.: "Deseja continuar? (S/N)"). (OK)

import os

livros = [
    {"nome": "Lapvona", "status": "Disponível"}, 
    {"nome": "Laranja Mecanica", "status": "Disponível"}, 
    {"nome": "The Kiss of Deception", "status": "Disponível"},
    {"nome": "Children of The Storm", "status": "Indisponível"}
]

def limpar_terminal():
    os.system("cls")

def exibir_titulo():
    print("\033[1;35m========== BIBLIOTECA ==========\033[m\n")

def exibir_livros():
    print("NOME DO LIVRO | STATUS DO LIVRO")
    for livro in livros:
        print(livro["nome"] + " | " + livro["status"])

def main():
    while True:
        limpar_terminal()
        exibir_titulo()
        exibir_livros()

        try:
            nome_do_livro = input("\nInforme o NOME do livro que você deseja pegar emprestado: ").lower()
            encontrado = False

            for livro in livros:
                if livro["nome"].lower() == nome_do_livro:
                    encontrado = True
                    if livro["status"] == "Disponível":
                        livro["status"] = "Indisponível"
                        print("\n\033[1;32m✅ Empréstimo realizado com sucesso!\033[m")
                    else:
                        print(f"\033[1;31m❌ O livro '{livro['nome']}' já está indisponível.\033[m")
                    break  # Sai do loop ao encontrar o livro
            if not encontrado:
                print("\033[1;33m⚠️ Livro não encontrado no catálogo.\033[m")

        except ValueError:
            print("Opção inválida!")
        
        op = input("Deseja continuar (S/N)? ").strip().upper()
        if op == 'N':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
