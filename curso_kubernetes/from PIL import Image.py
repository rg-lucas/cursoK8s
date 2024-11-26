from PIL import Image
import os

# Defina o caminho da pasta onde as imagens estão localizadas
pasta_imagens = r'C:\caminho\para\sua\pasta'

# Defina as dimensões desejadas
nova_largura = 600
nova_altura = 600

# Loop para percorrer todas as imagens da pasta
for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
        caminho_completo = os.path.join(pasta_imagens, nome_arquivo)

        # Abra a imagem
        img = Image.open(caminho_completo)

        # Redimensione a imagem
        img_redimensionada = img.resize((nova_largura, nova_altura))

        # Salve a imagem redimensionada (sobrescreve o arquivo original)
        img_redimensionada.save(caminho_completo)

print("Imagens redimensionadas com sucesso!")
