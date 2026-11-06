from selenium import webdriver
from selenium.webdriver.common.by import By

def coletar_links(driver, url):
    driver.get(url)

    #PERMITE FAZER LOGIN, SE NECESSÁRIO
    input("Se precisar, faça login no TikTok. Depois aperte Enter...")

    #LOCALIZANDO ELEMENTOS USANDO UM SELETOR CSS
    videos = driver.find_elements(
        By.CSS_SELECTOR,
        'a[href*="/video/"]'
    )
    print("Quantidade de elementos encontrados:", len(videos))

    links = []

    for video in videos:
        link = video.get_attribute("href")

        if(link and link not in links):
            links.append(link)
            
    print("Quantidade de links encontrados:", len(links))

    return videos, links
