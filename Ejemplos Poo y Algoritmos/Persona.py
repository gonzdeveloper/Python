
class Persona:   
        
    def __init__(self,nombre='',apellido='',edad=0):        
        self._apellido=apellido
        self._edad=edad
        self._nombre=nombre
        
    @property
    def nombre(self):
        return self._nombre   
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
        
    @property
    def apellido(self):
        return self._apellido   
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        self._edad=edad

class Maestro(Persona):
    
    def __init__(self,titulo=''):
        super().__init__()
        self._titulo=titulo
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self._titulo=titulo
    

if __name__=='__main__':
    maestro=Maestro()
    maestro.nombre='Gonzalo'   
    maestro.apellido='Ferrando'
    maestro.titulo='Tecnólogo'
    print(maestro.nombre+' '+maestro.apellido+' '+maestro.titulo)