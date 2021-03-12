from socket import *

#dados do cliente para conexão com o server

serverHost = 'localhost'
serverPort = 50007  
mensagem = [b'Ola,bem vindo!'] 
#cria o objeto socket e conectar ao servidor
sockobj = socket (AF_INET, SOCK_STREAM) #Voce está usando um servidor TCP-IP
sockobj.connect((serverHost, serverPort))
for linha in mensagem:
    sockobj.send(linha)
    #resposta do servidor
    data = sockobj.recv(1024)
    print('CLiente recebeu:', data)
    
sock.close()

#testando a conexãocom o servidor

while True:
    conexao, endereco = sockobj.accept()
    print('o servidor esta conectado por', endereco)
    while True:
        data = conexao.recv(1024)
        if not data:
            break
        conexao.send(b'eco =>' + data)
    conexao.close()
