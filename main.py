from selenium import webdriver
from crawler import coletar_links
from scraper import extrair_dados

def main():
    #ABRE UMA SESSÃO CHROME CONTROLADA PELO SELENIUM
    driver = webdriver.Chrome()

    #ABRE A CONTA DO LULA NO TIKTOK
    url = "https://www.tiktok.com/@lulaoficial"

    #ENCONTTRA OS LINKS DOS VIDEOS
    videos, links = coletar_links(driver, url)

    #COLETA LEGENDA E COMENTARIOS
    extrair_dados(driver, videos, links)

    #FECHA O NAVEGADOR
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main()
