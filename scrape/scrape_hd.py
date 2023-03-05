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
        # 브랜드명 과 모덺명 을 잘라야 함.
        title = title_tag.text.strip()
    else:
        title = "";
        
    model_tag = soup.find("p",class_="cdtl_model_num")
    if model_tag != None:
        model_list = model_tag.text.split(":")
        model = model_list[1].strip()
    else:
        model = "";
        
    price_tag = soup.find("span", class_="cdtl_old_price")
    if price_tag != None:
        price = re.sub(r'[^0-9]', '', price_tag.select("em")[0].text)
    else:
        price = "";
        
    color_tag = soup.find("div", class_="cdtl_tbl ty2")
    if color_tag != None:
        color = color_tag.select('td > div')[1].text
    else:
        color = "";
        
    size_tag = soup.find("div", class_="cdtl_tbl ty2")
    if size_tag != None:
        size = size_tag.select('td > div')[2].text
    else:
        size = "";
        
    material_tag = soup.find("div", class_="cdtl_tbl ty2")
    if material_tag != None:
        material = material_tag.select('td > div')[0].text
    else:
        material = "";
        
    country_tag = soup.find("div", class_="cdtl_tbl ty2")
    if country_tag != None:
        country = country_tag.select('td > div')[8].text
    else:
        country = "";
        
    company_tag = soup.find("div", class_="cdtl_tbl ty2")
    if company_tag != None:
        company_list = company_tag.select('td > div')[7].text.split("/")
        company = company_list[0]
    else:
        company = "";
    
    create_date_tag = soup.find("div", class_="cdtl_tbl ty2")
    if create_date_tag != None:
        create_date = create_date_tag.select('td > div')[4].text
    else:
        create_date = "";
    
    washing_method_tag = soup.find("div", class_="cdtl_tbl ty2")
    if washing_method_tag != None:
        washing_method = washing_method_tag.select('td > div')[3].text
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