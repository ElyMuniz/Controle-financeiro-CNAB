import ipdb


def handle_uploaded_file(f):
    with open("f", "r", encoding="utf-8") as destination:
        for linha in f:
            texto = linha.decode("utf-8")
            dados = {}
            dados["tipo"] = texto[0:1]
            dados["data"] = texto[1:9]
            dados["valor"] = texto[9:19]
            dados["CPF"] = texto[19:30]
            dados["cartao"] = texto[30:42]
            dados["hora"] = texto[42:48]
            dados["dono"] = texto[48:62]
            dados["loja"] = texto[62:81]
            print(dados)
            # destination.write(chunk)
