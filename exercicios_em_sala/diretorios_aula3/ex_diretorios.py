import os
#imprima meu diretorio de trabalho
print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

#criar novas pastas
# os.makedirs(".teste1/teste2")

path = 'C:\\Windows\\System32\\calc.exe'

print(os.path.basename(path))

print(os.path.dirname(path))