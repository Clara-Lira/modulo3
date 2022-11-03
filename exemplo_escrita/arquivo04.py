filename = "arquivo_escrita1.txt"

with open(filename, "w") as file_object:
    file_object.write("Eu amo python!\n")
    file_object.write("Eu amo comer pizza!")