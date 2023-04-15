import requests


#Get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/posts')
#print(resultado_get.json())

#Get com Id
resultado_getID = requests.get('https://jsonplaceholder.typicode.com/posts/5')
#print(resultado_getID.json())

#Post - Criando um novo recurso
postagem = {'userId': 1, 'id': 5, 'title': 'Mestre da Automação', 'body': 'Olá, eu sou uma nova postagem'}
resultado_post = requests.post('https://jsonplaceholder.typicode.com/posts', postagem)
#print(resultado_post.json())


#PUT - Atualizar um recurso ecistente
postagem_up = {'userId': 1, 'id': 5, 'title': 'Postagem Atualizada', 'body': 'Olá, Atualizai a postagem'}
resultado_att = requests.put('https://jsonplaceholder.typicode.com/posts/5', postagem_up)
#print(resultado_att.json())

#DELETE - Excluir um recurso
resultado_delet = requests.delete('https://jsonplaceholder.typicode.com/posts/5')
print(resultado_delet.json())