from classes.GerenciarS3 import GerenciarS3

class menugerenciadorS3:
    def _init_(self, nome_bucket):
        self.gerenciador = GerenciarS3(nome_bucket)
        
    def exibir_menu(self):
        print('---Menu---')
        print('1')