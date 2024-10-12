from view.screens import clear, _basic
from employee.view import screen_employee
from controller.inputs import inputInt, inputStr, inputAdrs
from employee.model import Employee
from view.styles import printS, printW
from employee.view import view_employee


def edit() -> None:
    """
    Edits an existing employee.

    Asks the user for the employee's CPF and, if it exists,
    allows the user to edit their information. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    cpf = input(" | CPF:\t")

    employee = Employee()
    employee_data = employee.visualize_employee(cpf)
    if employee_data is None:
        printW("> CPF não alcançado! <Enter> para continuar")
        input()
        return

    view_employee(employee_data)

    name = input(" | Nome:\t")
    address = input(" | Endereço:\t")
    age = input(" | Idade:\t")
    phone = input(" | Telefone:\t")

    employee_edit = {
        cpf: [
            name if name != "" else employee_data[cpf][0],
            address if address != "" else employee_data[cpf][1],
            age if age != "" else employee_data[cpf][2],
            phone if phone != "" else employee_data[cpf][3],
        ]
    }
    employee.edit_employee(employee_edit, cpf)

    input()


def search() -> None:
    """
    Searches for a previously registered employee.

    Asks the user for the employee's CPF and, if it exists,
    allows the user to view their information. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    cpf = input(" | CPF:\t")

    employee = Employee()
    employee_data = employee.visualize_employee(cpf)
    if employee_data is None:
        printW("> CPF não alcançado! <Enter> para continuar")
        input()
        return

    view_employee(employee_data)
    printS("> Enter para continuar")
    print(employee_data)

    input()
    return


def visualize_all_employees() -> None:
    """
    Visualize all previously registered employees.

    :return: None
    """

    _basic("Todos os funcionários")
    employee = Employee()
    employee_data = employee.visualize_all_employee()
    view_employee(employee_data)
    printW("> Enter para continuar")
    input()


def delete() -> None:
    """
    Deletes a previously registered employee.

    Asks the user for the employee's CPF and, if it exists,
    removes the employee from the system. If not, prints an
    error message and goes back to the main menu.

    :return: None
    """

    _basic("Deletando funcionário")

    cpf = input("CPF:\t")

    contract = Employee()
    if not contract.update_employee(cpf):
        printW(f"{cpf} não alcançado!")
        input()
        return

    printS(f"{cpf} desligado do sistema!")
    input()


def new_employee() -> None:
    """
    Adds a new employee to the system.

    Asks the user for the employee's name, age, CPF, address and phone.
    If the CPF is unique, the employee is added to the system.
    If not, an error message is printed and the user is returned to
    the main menu.

    :return: None
    """

    _basic("Adicionando novo funcionário")

    name = inputStr("Nome:\t")
    age = inputInt("Idade:\t")
    cpf = input("CPF:\t")
    address = inputAdrs("Endereço:\t")
    phone = input("Telefone:\t")

    contract = Employee()
    if not contract.insert_data(
                            name=name,
                            age=age,
                            cpf=cpf,
                            address=address,
                            phone=phone
                    ):
        printW(f"{cpf} já foi registrado! Deseja ativa-lo ?")
        option = inputStr("Sim/Não:\t").lower()
        if option.startswith("s"):
            printS(f"{cpf} ativado!")
            contract.update_employee(cpf)
        else:
            printW("Operação cancelada!\n")
        input()
        return

    printS(f"{name} foi adicionado ao sistema com sucesso!")
    input()


def main_employee() -> None:
    """
    Main function of the employee module.

    Runs an infinite loop that calls the employee screen
    reads the user's option and executes the corresponding action,
    which can be:

    1. Add a new employee to the system
    2. View all employees
    3. Search for an employee
    4. Remove an employee from the system
    5. Edit an existing employee
    0. Go back to the main menu

    :return: None
    """
    while True:
        clear()
        screen_employee()
        option = input("")

        match option:
            case '1':
                new_employee()
            case '2':
                visualize_all_employees()
            case '3':
                search()
            case '4':
                delete()
            case '5':
                edit()
            case '0':
                clear()
                return


if __name__ == "__main__":
    edit()
