import json

aluno = {
    "matemática": 8.5,
    "portugues": 9.0,
    "soma": 0
}

matemática = aluno ["matemática"]
portugues = aluno ["portugues"]


soma_de_valor = matemática + portugues 
aluno["soma"] = soma_de_valor

with open("notas.json", 'a') as arquivo:
    json.dump(aluno, arquivo, ensure_ascii=False)

print("notas carregdas : ")
print(f"Matemática: {matemática}")
print(f"Português: {portugues}")
print(f"Soma das notas: {soma_de_valor}")