from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

def scrape_item_from_hd(model):
    
    options = Options()
    options.add_argument('--headless')  # 웹 브라우저 창 숨기기

    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    
    browser.get(f"https://www.hmall.com/p/pde/search.do?searchTerm={model}")
    
    check = browser.find_elements(By.CSS_SELECTOR, ".product-area")
    
    if len(check) != 0 :
        elements = browser.find_elements(By.CSS_SELECTOR, ".pdthumb div")
        
        elements[0].click()
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    result = {}
    
    title_tag = soup.find("strong",class_="prduct-name")
    if title_tag != None:
        title = title_tag.text.strip()
    else:
        title = "";

    price_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'tblwrap'}).find_all('tr')[1].find('td')
    if price_tag != None:
        price = re.sub(r"[^\d]", "", price_tag.text.strip())
    else:
        price = "";
        
    color_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[1].find('p')
    if color_tag != None:
        color = color_tag.text.strip()
    else:
        color = "";
        
    size_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[2].find('p')
    if size_tag != None:
        size = size_tag.text.strip()
    else:
        size = "";
        
    material_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[0].find('p')
    if material_tag != None:
        material = material_tag.text.strip()
    else:
        material = "";
        
    country_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[4].find('p')
    if country_tag != None:
        country = country_tag.text.strip()
    else:
        country = "";
        
    company_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[3].find('p')
    if company_tag != None:
        company = company_tag.text.strip()
    else:
        company = "";
    
    create_date_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[6].find('p')
    if create_date_tag != None:
        create_date = create_date_tag.text.strip()
    else:
        create_date = "";
    
    washing_method_tag = soup.find('div', {'id': 'PDAItemOptBasicInfoHtml'}).find('div', {'class': 'basic-txt01'}).find_all('div', {'class': 'txt-info'})[5].find('p')
    if washing_method_tag != None:
        washing_method = washing_method_tag.text.strip()
    else:
        washing_method = "";
    
    result["title"] = title
    result["model"] = model
    result["price"] = price
    result["color"] = color
    result["size"] = size
    result["material"] = material
    result["country"] = country
    result["company"] = company
    result["create_date"] = create_date
    result["washing_method"] = washing_method

    browser.quit()
    
    return result