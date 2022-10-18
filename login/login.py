from bson.json_util import dumps
from bson.objectid import ObjectId

def cadastrar(client_mongo,client_redis):
    mycol = client_mongo.usuarios
    usuario = mycol.find_one(ObjectId('6335e0ca502273bf5be0732c'))
    
    for favorito in usuario['lista_favoritos']:
        
        client_redis.hset('user:' + usuario['email'], str(favorito['nome']), dumps(favorito))
        
    client_redis.hset('user:' + usuario['email'], 'status', 'deslogado')    
    print(client_redis.hgetall('user:' + usuario['email']))
    print(client_redis.hkeys('user:' + usuario['email']))
    print(client_redis.keys())
    #print(client_redis.delete("user:nicolas@gmail.com"))

def login(client_mongo,client_redis):
    mycol = client_mongo.usuarios
    usuario = mycol.find_one(ObjectId('6335e0ca502273bf5be0732c'))
    client_redis.hset('user:' + usuario['email'], 'status', 'logado')    
    print(client_redis.hget('user:' + usuario['email'], 'status'))


def deslogar(client_mongo,client_redis):
    mycol = client_mongo.usuarios
    usuario = mycol.find_one(ObjectId('6335e0ca502273bf5be0732c'))
    client_redis.hset('user:' + usuario['email'], 'status', 'deslogado')    
    print(client_redis.hget('user:' + usuario['email'], 'status'))