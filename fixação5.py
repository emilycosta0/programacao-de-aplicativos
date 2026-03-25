usuarios = ["admin", "convidado", "suporte", "teste"]
usuarios.remove("teste")
del usuarios[0]
print(f"A lista de usuarios ficou desta forma: {usuarios}.")
