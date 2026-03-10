id_usuario = int(input("Digite seu ID de usuario: "))
valor_da_compra = float(input("Digite o valor da sua compra: "))

if id_usuario % 2 == 0 and valor_da_compra > 500:
    print(f"Parabéns, usuario {id_usuario}. Você ganhou um cupom para sua compra de R$ {valor_da_compra:.2f}.")
else:
    print(f"Obrigado pela compra, usuario {id_usuario}. Continue acompanahando nossas promoções!")