from GerenciarS3 import GerenciarS3

controla_S3 = GerenciarS3('aulanoiteamanda000')

controla_S3.lista_arquivos()
diretorio_destino = 'aula07_06/arquivos'
nome_arquivo = 'ex3_amanda_aui3.png'
controla_S3.download_arquivo(nome_arquivo, diretorio_destino)