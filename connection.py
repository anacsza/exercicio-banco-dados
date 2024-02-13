import sqlite3

connection = sqlite3.connect('banco')
cursor = connection.cursor()

print("1. Crie uma tabela chamada alunos com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).")
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')
print("")

print("2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.")
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Mae C. Jemison", 67, "Astronomia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Marie Curie", 67, "Química");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Nina Silva", 44, "TI");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Nina da Hora", 29, "Ciências da Computação");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Sonia Guimarães", 66, "Física");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Y", 66, "Engenharia");')
print("")

print("3. Consultas Básicas\nEscreva consultas SQL para realizar as seguintes tarefas:")
print("a) Selecionar todos os registros da tabela alunos.")
alunos = cursor.execute('SELECT * FROM alunos;')
for aluno in alunos:
    print(aluno)
print("")

print("Selecionar o nome e a idade dos alunos com mais de 20 anos.")
alunos = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
for aluno in alunos:
    print(aluno)
print("")

print("c) Selecionar os alunos do curso de Engenharia em ordem alfabética.")
alunos = cursor.execute('SELECT nome, idade FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
for aluno in alunos:
    print(aluno)
print("")

print("d) Contar o número total de alunos na tabela")
alunos = cursor.execute('SELECT COUNT(nome) FROM alunos;')
for aluno in alunos:
    print(aluno)
print("")

print("4. Atualização e Remoção")
print("a) Atualize a idade de um aluno específico na tabela.")
cursor.execute('UPDATE alunos SET idade = 20 WHERE id = 1;')
print("")

print("b) Remova um aluno pelo seu ID.")
cursor.execute('DELETE FROM alunos WHERE id = 1;')
print("")

print("5. Criar uma Tabela e Inserir Dados\nCrie uma tabela chamada clientes com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.")
cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Bertha Lutz", 82, 1000000.99);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Grace Hopper", 86, 9999999999.99);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Jaqueline Goes", 34, 123456789123456.99);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Sarah Catherine Gilbert", 61, 98765431654987.99);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Carmen Portinho", 98, 100000000000.99);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "X", 18, 1000.99);')
print("")

print("6. Consultas e Funções Agregadas\nEscreva consultas SQL para realizar as seguintes tarefas:")
print("a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.")
clientes = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for cliente in clientes:
    print(cliente)
print("")

print("b) Calcule o saldo médio dos clientes.")
clientes = cursor.execute('SELECT AVG(saldo) FROM clientes;')
for cliente in clientes:
    print(cliente)
print("")

print("c) Encontre o cliente com o saldo máximo.")
clientes = cursor.execute('SELECT nome FROM clientes WHERE saldo IN (SELECT MAX(saldo) FROM clientes);')
for cliente in clientes:
    print(cliente)
print("")

print("d) Conte quantos clientes têm saldo acima de 1000.")
clientes = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 1000;')
for cliente in clientes:
    print(cliente)
print("")

print("7. Atualização e Remoção com Condições")
print("a) Atualize o saldo de um cliente específico.")
cursor.execute('UPDATE clientes SET saldo = 55555555555.55 WHERE id = 6;')
print("")

print("b) Remova um cliente pelo seu ID.")
cursor.execute('DELETE FROM clientes WHERE id = 6;')
print("")

print("8. Junção de Tabelas\nCrie uma segunda tabela chamada compras com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela clientes), produto (texto) e valor (real).")
cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY(cliente_id) REFERENCES clientes(id));')
print("")

print("Insira algumas compras associadas a clientes existentes na tabela clientes.")
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Arroz", 10.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, "Feijão", 10.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 2, "Farofa", 8.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 3, "Leite", 3.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 3, "Farinha", 15.00);')
print("")

print("Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.")
compras = cursor.execute('SELECT nome, produto, valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id;')
for compra in compras:
    print(compra)
print("")

connection.commit()
connection.close()