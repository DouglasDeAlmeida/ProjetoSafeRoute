from selenium import webdriver
from time import sleep

# 2) FUNCAO DE ACESSO  E USO DA FERRAMENTA - PICO DE HORARIO:

# 2.1) definir uma funcao para acessar a ferramenta de horario de pico de horario
def obter_driver():
    """" Foi utilizado para navegador o Chrome Veresao 86, e seus respectivo Driver instalado no python,
     criado o driver como biblioteca e salvo na pasta "Chrome Driver" e classe ("chromedriver.exe")
     """
    driver = webdriver.Chrome(executable_path=r"C:\Users\PICHAU\PycharmProjects\webscraping\chromedriver.exe")
    #return driver
    driver.get(
        "https://www.google.com/search?rlz=1C1GCEU_pt-BRBR912BR912&sxsrf=ALeKk01IjtydkA-vB_mCNePTR5woQlm3jA%3A1606856203153&ei=C67GX67iCNfE5OUPjeqEiAk&q=shopping+iguatemi+sao+paulo&oq=s&gs_lcp=CgZwc3ktYWIQARgAMgQIIxAnMgQIIxAnMgQIIxAnMgQIABBDMgUIABCxAzIICC4QsQMQgwEyBAgAEEMyCAguELEDEIMBMgUIABCxAzIICC4QsQMQgwE6BwgjEOoCECc6BwgAELEDEEM6AggAUO0uWLpEYOVQaANwAHgEgAGMAogBgw-SAQMyLTiYAQCgAQGgAQKqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab")
    driver.implicitly_wait(20)
    agora = driver.find_element_by_class_name("ujewvc").text
    sleep(5)  # Esta funcao estabelece o tempo para ferramenta agora executar;
    print(agora)
    return agora
    driver.quit()



def classificacao_metricas_observadas():
    agora =obter_driver()

    if agora == "Agora: não é movimentado":
        nivel_aglomeracao = 14
        print(agora)
        return nivel_aglomeracao
    if agora == "Agora: Não muito movimentado":
        nivel_aglomeracao = 25
        print(agora)
        return nivel_aglomeracao
    if agora == "Agora: Um pouco movimentado":
        nivel_aglomeracao = 35
        print(agora)
        return nivel_aglomeracao
    elif agora == "Agora: Tão movimentado como de costume":
        nivel_aglomeracao = 50
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return nivel_aglomeracao
    elif agora == "Agora: muito movimentado":
        nivel_aglomeracao = 66
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return nivel_aglomeracao

    elif agora == "Agora: Mais movimentado":
        nivel_aglomeracao = 75
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return nivel_aglomeracao

