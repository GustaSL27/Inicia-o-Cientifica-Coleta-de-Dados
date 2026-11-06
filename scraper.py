from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

#COLETA A LEGENDA DE CADA VIDEO
def extrair_legendas(videos):
    legendas = []

    for video in videos:
        try:
            imagem = video.find_element(By.TAG_NAME, "img")
            legenda = imagem.get_attribute("alt")

            legendas.append(legenda)

        except Exception as erro:
            print("Erro ao extrair legenda:", erro)
            legendas.append("Legenda não encontrada")

    return legendas

#ROLA A ÁREA DE COMENTÁRIOS
def scroll_comentarios(driver):
    print("Começando a rolagem automatica dos comentarios")

    primeiro_comentario = driver.find_element(By.XPATH, "//span[@style='color: var(--ui-text-1); font-size: 15px; font-weight: 478;']")
    primeiro_comentario.click()

    for j in range(100):
        driver.switch_to.active_element.send_keys(Keys.PAGE_DOWN)
        print(f"Rolagem {j + 1}/100 feita.")
        sleep(1)

#COLETA E SALVA OS COMENTARIOS
def coleta(driver, link):
    comentarios = driver.find_elements(
        By.XPATH, 
        "//span[@style='color: var(--ui-text-1); font-size: 15px; font-weight: 478;']"
    )

    with open("comentarios.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(f"\nVídeo: {link}\n")

        comentarios_salvos = set()

        for comentario in comentarios:
            texto = comentario.text.strip()  # o .strip() "limpa" o comentario retirando espaços vazios antes e depois do comentario
            if texto:  # para se tiver linhas vazias não salvar
                comentarios_salvos.add(texto)

def extrair_dados(driver, videos, links):
    #CRIA PASTA DATA
    os.makedirs("data", exist_ok=True)

    #EXTRAI AS LEGENDA DOS VIDEOS
    legendas = extrair_legendas(videos)

    #PECORRE OS LINKS DOS VIDEOS
    for i, link in enumerate(links):
        numero = i + 1
        legenda = legendas[i]

        print(f"\nProcessando vídeo {numero}/{len(links)}")
        
        #ABRE O VIDEO
        driver.get(link)

        #CRIA ARQUIVO PARA CADA VIDEO
        caminho = f"data/video{numero}.txt"

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"LINK: {link}\n\n")
            arquivo.write("LEGENDA:\n")
            arquivo.write(f"{legenda}\n\n")

            # AGUARDA A ABERTURA DOS COMENTÁRIOS
            input("Abra os comentários e pressione Enter...")

            #CARREGA MAIS COMENTARIOS E COLETA OS COMENTARIOS
            scroll_comentarios(driver)
            coleta(driver, arquivo)

            print(f"Dados salvos em {caminho}")
    
    print("\nCoelta finalizada.")
