# repita os passos manuais, usando código
# se sem conta: apertar pular na parte de login, selecionar data mes e ano, apertar em avançar, concordar com os termos
# abrir o painel de comentarios
# scrollar a aba de comentarios para carregar novos e repetir

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

# abrir o video no tiktok
driver = webdriver.Chrome()
driver.get('https://www.tiktok.com/@plnacional_/video/7676218963205819656?q=bolsonaro&t=1792603634517')

# abrir o painel de comentarios e fazer o captcha
input("Role a página até carregar os comentários desejados e pressione ENTER no terminal")

# coletar os primeiros comentarios
comentarios = driver.find_elements(By.XPATH, "//span[@style='color: var(--ui-text-1); font-size: 15px; font-weight: 478;']")

# salvar em um txt
with open("comentarios.txt", "a", encoding='utf-8') as comentarios_file:
    for i in range(len(comentarios)):
        texto = comentarios[i].text.strip() # o .strip() "limpa" o comentario retirando espaços vazios antes e depois do comentario
        if texto:  # para se tiver linhas vazias não salvar
            comentarios_file.write(f'{i + 1}- {texto}{os.linesep}')

print("Pressione ENTER para fechar o tiktok")
input()

