import qrcode

# Texto que você deseja gerar o QR Code
print("Texto que você deseja gerar o QR Code")
texto = input()

# Gerando o QR Code a partir do texto
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(texto)
qr.make(fit=True)

# Salvando o QR Code em um arquivo de imagem
img = qr.make_image(fill_color="black", back_color="white")

print("Nome do arquivo")
nome_arquivo = input()
img.save(nome_arquivo+".png")
