# repita os passos manuais, usando código
# se sem conta: apertar pular na parte de login, selecionar data mes e ano, apertar em avançar, concordar com os termos
# scrollar a aba de comentarios para carregar novos e repetir
# https://www.tiktok.com/@plnacional_/video/7676218963205819656?q=bolsonaro&t=1792603634517

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys

# abrir o video no tiktok
def abrir_video(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# scrollar a aba de comentarios para carregar novos e repetir
def scroll_comentarios(driver):
    print("Começando a rolagem automatica dos comentarios")

    primeiro_comentario = driver.find_element(By.XPATH,
                                              "//span[@style='color: var(--ui-text-1); font-size: 15px; font-weight: 478;']")
    primeiro_comentario.click()

    for j in range(100):
        driver.switch_to.active_element.send_keys(
            Keys.PAGE_DOWN)  # envia pg down pro elemento "ativo" encontrado anteriormente (primeiro_comentario)
        print(f"Rolagem {j + 1}/100 feita.")
        sleep(1)

# coletar e salva os comentarios
def coleta(driver):
    comentarios = driver.find_elements(By.XPATH,
                                       "//span[@style='color: var(--ui-text-1); font-size: 15px; font-weight: 478;']")

    with open("comentarios4.txt", "a", encoding='utf-8') as comentarios_file:
        for i in range(len(comentarios)):
            texto = comentarios[
                i].text.strip()  # o .strip() "limpa" o comentario retirando espaços vazios antes e depois do comentario
            if texto:  # para se tiver linhas vazias não salvar
                comentarios_file.write(f'{i + 1}- {texto}{os.linesep}')

# define o main do programa
def main():
    url = input("URL do video: ")
    driver = abrir_video(url)

    # abrir o painel de comentarios e fazer o captcha
    input("Abra a aba de comentários e pressione ENTER no terminal")

    scroll_comentarios(driver)
    coleta(driver)
    input("Pressione ENTER para fechar o tiktok")

main()
