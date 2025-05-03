from datetime import datetime


class TelaConsulta:
    def __init__(self,data:datetime,cpf_usuario:str,consulta_id:str):
        self.cpf_usuario = cpf_usuario
        self.data = data
        
    def carregar_consultas(self):
        #implementar
        pass
    
    def atualizar_status(self):
        #implementar
        pass
    
    def cancelar_consulta(self, consulta_id):
        #implementar
        pass