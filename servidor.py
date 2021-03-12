from socket import *

#dados da conexão com o servidor

meuHost = 'localhost'
minhaPorta = 50007
sockobj = socket (AF_INET, SOCK_STREAM) #Voce está usando um servidor TCP-IP

sockobj.bind((meuHost, minhaPorta))

sockobj.listen(5)

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
