from data.saveJson import SaveJson


class Employee:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.cpf = ""
        self.adress = ""
        self.phone = ""
        self.employee = SaveJson("funcionarios.json")
        self.load_employee = self.employee.load_json()

    def add_employee(
            self, name: str, cpf: str,
            age: int, adress: str, phone: str) -> bool:

        if not self._verify_cpf(cpf):
            new_employee = {
                cpf: [
                    name,
                    age,
                    adress,
                    phone,
                    True
                ]
            }
            self.employee.modify_json(data=new_employee)
            return True
        return False

    def remove_employee(self, cpf: str) -> bool:
        if self._verify_cpf(cpf):
            for keys in self.load_employee:
                if cpf == keys:
                    for details in self.load_employee[keys]:
                        self.load_employee[cpf][-1] = False
                        self.employee.update_json(self.load_employee)
                        return True
        return False

    def edit_employee(self, cpf: str) -> None:
        ...

    def search_employee(self, cpf: str) -> None:
        ...

    def _verify_cpf(self, cpf: str) -> bool:
        if cpf in self.load_employee:
            return True
        return False
