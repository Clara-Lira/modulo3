#abrindo um arquivo para leitura
file = "../arquivo.txt"
path = "path/"
filepath = path + file

#filename =
with open('../arquivo.txt', "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)