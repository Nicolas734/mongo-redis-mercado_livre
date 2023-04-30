import pymongo
import redis
import login.login as login
import favoritos.favoritos as favoritos

##Agroberto  6335e0ca502273bf5be0732c

##Nicolas   6328e1f92e18e5646b7c57f2

client_mongo = pymongo.MongoClient("mongodb+srv://Nicolas:NKpAgEPNEdDGuE1F@nicolas.yt3g1l9.mongodb.net/?retryWrites=true&w=majority")
client_redis = redis.Redis(host='redis-19904.c266.us-east-1-3.ec2.cloud.redislabs.com',
    port= 19904,
    password='senha')

mydb = client_mongo.mercado_livre

execucao = True

while execucao:

        print('''\nOpções: \n
        [1] Cadastrar
        [2] Login
        [3] Deslogar
        [4] Favoritar
        [0] Sair
        ''')

        opcoes = input(str("Escolha uma das opções: "))
        
        match int(opcoes):
            case 1:
                login.cadastrar(mydb,client_redis)
            case 2:
                login.login(mydb,client_redis)
            case 3:
                login.deslogar(mydb,client_redis)
            case 4:
                favoritos.favoritar(mydb,client_redis)
            case 0:
                execucao = False
                print("\nAté mais \n")
                break