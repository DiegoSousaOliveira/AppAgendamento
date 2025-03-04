from datetime import datetime


class telaAgendamento:
    def __init__(self,data:datetime,cpf_usuario:str,medicos : list[Medico]):
        self.data = data
        self.cpf_usuario = cpf_usuario
        #fazer medicos:list<medico>
    
    
    def carregar_medicos():
        #implementar
        pass
    
    #implementar
    def agendar(self):
       return {
           "data": self.data.strftime("%Y-%m-%d %H:%M:%S"),
           "cpf_usuario": self.cpf,
           "medicos": [repr(medico) for medico in self.medicos]
      }
       pass