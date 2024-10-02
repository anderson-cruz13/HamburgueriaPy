from view.telas import cabecalho, opcoes
from typing import Dict


def tela_almoxarifado() -> None:
    cabecalho("almoxarifado")
    opcoes(
        "adicionar compra",
        "visualizar almoxarifado",
        "buscar item",
        "excluir item",
        "editar item",
        "menu principal")
    print(">> Escolha uma opção\n")


def cabecalho_status(
        label: str | None = "",
        dict_file: dict | None = None,
        ids: int | None = None):

    if not label:
        return

    row = 110
    text = label.upper()
    if not dict_file:
        items = ids
    else:
        items = len(dict_file)
    text_width = len(text)
    space = row - text_width - 2
    print(f"\033[1m {'.' * row} ")
    print(f"  {text} {items:<{space}} ")
    print(f" {'.' * row}\033[m")


def cabecalho_infor(infor: Dict, text: str | None = ""):
    if text:
        cabecalho_status(text, infor)

    ids = 5
    name = 90
    quantity = 10
    print(f"\033[1;31m-|-----|{"-" * name}|-------------|-")
    print(f" |{'ID':^{ids}}|{'NOME':^{name}}| {'QUANTIDADE':^{quantity}}  |")
    print(f"-|-----|{"-" * 90}|-------------|-\033[m")

    for key, value in infor.items():
        print(f" |{key:^{ids}}|{value[0].title():^{name}}| \
{value[1]:^{quantity}}  |")
        print(f"-|-----|{"-" * 90}|-------------|-")