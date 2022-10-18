from bson.json_util import dumps
from bson.objectid import ObjectId
import json


def favoritar(client_mongo,client_redis):
    favoritos = []
    mycol_usuarios = client_mongo.usuarios
    mycol_produtos = client_mongo.produtos
    usuario = mycol_usuarios.find_one(ObjectId('6328e1f92e18e5646b7c57f2'))
    
    
    ## salva novos produtos a lista de favoritos no redis
    favoritos.append(mycol_produtos.find_one(ObjectId('630d2cceca06592c1def5643')))
    favoritos.append(mycol_produtos.find_one(ObjectId('632a0c86b07c794dc11db15a')))
    
    for favorito in favoritos:
        client_redis.hset("user:" + usuario['email'], str(favorito['nome']), dumps(favorito))

    ## limpa a lista dos favoritos
    favoritos.clear()

    ## atualiza a listagem de favoritos do mongo
    dados = client_redis.hkeys("user:" + usuario['email'])
    for dado in dados:
        if dado.decode() == 'status':
            print('status')
        else:
            favoritos.append(json.loads(client_redis.hget("user:" + usuario['email'],dado.decode())))
    
    mycol_usuarios.update_one({"_id":ObjectId(usuario["_id"])}, {"$set": {
        "nome":usuario['nome'],
        "email":usuario['email'],
        "telefone":usuario['telefone'],
        "cpf":usuario['cpf'],
        "rg":usuario['rg'],
        "data_nascimento":usuario['data_nascimento'],
        "enderecos":usuario["enderecos"],
        "lista_favoritos":favoritos,
        "compras":usuario["compras"]
    }}, upsert=True)