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
    def setId(self,idbasex):
        self.idbase = idbasex
    def setName(self,namex):
        self.name = namex
    def equals(self):
        print(" Verifica que sean iguales")
    def hashCode(self):
        print(" Realiza el hashCode")





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
        self.salary =salarx
    def setDepartment(self,depax):
        self.listaPedidos = depax




class CompanyEntity(BaseEntity):

    def __init__(self, idbase, name):
        super().__init__(idbase, name)
        self._depEnt = DepartmentEntity(idbase,name)

    def getDepartments(self):
        return self._depEnt

    def setDepartments(self,idbasex,namex):
        self._depEnt = DepartmentEntity(idbasex,namex)




class DepartmentEntity(BaseEntity):


    def __init__(self, idbase, name):
        super().__init__(idbase, name)

    def getCompany(self):

    def setCompany(self):

    def getEmployees(self):

    def setEmpolees(self):







