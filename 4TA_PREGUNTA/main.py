class BaseEntity:
    idbase = None
    name = None

    def __init__(self, idbase, name):
        self.idbase = idbase
        self.name = name

    def getId(self):
        return self.idbase
    def getName(self):
        return self.name
    def setId(self,pedido):
        self.listaPedidos.append(pedido)
    def setName(self,pedido):
        self.listaPedidos.append(pedido)
    def equals(self):
        return self.email
    def hashCode(self):
        return self.listaPedidos





class EmployeeEntity(BaseEntity):
    salary =  None
    def __init__(self, idbase, name,salary):
        super().__init__(idbase, name)
        self.salary = salary

    def getSalary(self):
        return self.salary
    def getDepartment(self):
        return self.name
    def setSalary(self,salarx):
        self.listaPedidos =salarx
    def setDepartment(self,depax):
        self.listaPedidos = depax




class CompanyEntity(BaseEntity):

    def __init__(self, idbase, name):
        super().__init__(idbase, name)
        self._depEnt = DepartmentEntity(idbase,name)

    def getDepartments(self):
        return self._depEnt

    def setDepartments(self,depa):
        return self._depEnt = depa




class DepartmentEntity(BaseEntity):
    nombre = None
    listaProfesores = None
    listaCursos = None

    def __init__(self, idbase, name):
        super().__init__(idbase, name)






