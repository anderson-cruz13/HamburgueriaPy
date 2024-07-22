# Importações necessárias para o pacote.
from ferramentas_pct import (
    limpar_tela, 
    leia_item, 
    leia_int, 
    leia_float, 
)
from dados_pct import (
    save_data, cardapio
)
from estilização_pct import (
    subtitulo, 
    titulo)


ID_MENU = 1 if len(cardapio) == 0 else max(cardapio.keys()) + 1

def exibir_cardapio():
    """
    Exibe o cardápio da hamburgueria, mostrando os hambúrgueres disponíveis e seus ingredientes por porção.
    """
    limpar_tela()
    titulo("CARDÁPIO")
    for codigo, detalhes in cardapio.items():
        for nome_hamburguer, ingredientes in detalhes.items():
            if nome_hamburguer != 'PRECO':
                print()
                subtitulo(nome_hamburguer)  # Nome do hambúrguer 
                print('\033[1;37m')
                for ingrediente, quantidade in ingredientes.items():
                    print(f"{ingrediente} {'-' * (122 - len(ingrediente))} {quantidade}")
                print(f"PREÇO {'-' * (116 - len('PREÇO'))} R$ {detalhes['PRECO']:.2f}")
    print()
    print('\033[m') 
    input(">> Enter")


def verificar_hamburguer_existente():
    """
    Verifica a existência de um hambúrguer no cardápio.

    Returns:
        Nome do hambúrguer se encontrado, caso contrário None.
    """
    hamburguer = leia_item("Hambúrguer: ").upper().replace(" ", "")
    
    for codigo, detalhes in cardapio.items():
        hamburguer_menu = list(detalhes.keys())[0].replace(" ", "").upper()

        if hamburguer == hamburguer_menu:
            return True, hamburguer
        
    return False, hamburguer


def atualizar_hamburguer(hamburguer):
    """
    Atualiza os ingredientes de um hambúrguer existente no cardápio.
    """
    limpar_tela()
    titulo("ATUALIZAÇÃO DE HAMBÚRGUER")
    for codigo, detalhes in cardapio.items():
        hamburguer_menu = list(detalhes.keys())[0].upper()

        if hamburguer.replace(" ", "") == hamburguer_menu.replace(" ", ""):
            print(f"Atualizando o hambúrguer {hamburguer_menu}")
            ingredientes = adicionar_ingredientes()
            detalhes[hamburguer_menu] = ingredientes
            detalhes['PRECO'] = ingredientes.pop("PRECO")

            save_data("arquivo_cardapio.dat", cardapio)


def adicionar_ingredientes():
    """
    Adiciona ingredientes ao hambúrguer.
    """
    ingredientes = {}
    
    while True:
        ingrediente = input("(SAIR) - Ingrediente:  ").strip().upper()

        if ingrediente == "SAIR":
            break

        quantidade = leia_int("Quantidade:  ")
        ingredientes[ingrediente] = quantidade        

    preco = leia_float("Preço:  ")
    ingredientes["PRECO"] = preco

    return ingredientes


def criar_hamburguer():
    """
    Cria um novo hambúrguer e adiciona ao cardápio.
    """
    limpar_tela()
    titulo("CRIAÇÃO DE HAMBÚRGUER")
    global ID_MENU

    nome_hamburguer = leia_item("Novo Hambúrguer: ").strip().upper()
    ingredientes = adicionar_ingredientes()
    
    cardapio[ID_MENU] = {
        nome_hamburguer: ingredientes,
        'PRECO': ingredientes.pop("PRECO")
    }
    ID_MENU += 1
    save_data("arquivo_cardapio.dat", cardapio)
    return True


def excluir_hamburguer():
    """
    Exclui um hambúrguer do cardápio.
    """
    limpar_tela()
    titulo("EXCLUSÃO DE HAMBÚRGUER")
    hamburguer = leia_int("Código do Hambúrguer: ")
    
    del cardapio[hamburguer]
    save_data("arquivo_cardapio.dat", cardapio)
    return True
        