from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_item_from_lt(model):
    
    options = Options()
    # options.add_argument('--headless')  # 웹 브라우저 창 숨기기

    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    
    browser.get(f"https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q={model}")
    
    check = browser.find_elements(By.CSS_SELECTOR, ".srchProductList")
    
    if len(check) != 0 :
        elements = browser.find_elements(By.CSS_SELECTOR, ".srchGridProductUnitLink")
        
        elements[0].click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.new_window_is_opened)
        handles = browser.window_handles
        browser.switch_to.window(handles[-1])
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    result = {}
    
    title_tag = soup.find("h2",class_="productNameText")
    if title_tag != None:
        title = title_tag.text.strip()
    else:
        title = "";

    price_tag = soup.find('div', {'class': 'quantity-wrap'}).find('span', {'class': 'won'})
    if price_tag != None:
        price = re.sub(r"[^\d]", "", price_tag.text.strip())
    else:
        price = "";
        
    color_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(7) dd")
    if color_tag != None:
        color = color_tag.text.strip()
    else:
        color = "";
    
    size_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(8) dd")
    if size_tag != None:
        size = size_tag.text.strip()
    else:
        size = "";
    
    material_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(6) dd")
    if material_tag != None:
        material = material_tag.text.strip()
    else:
        material = "";
    
    country_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(10) dd")
    if country_tag != None:
        country = country_tag.text.strip()
    else:
        country = "";
    
    company_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(9) dd")
    if company_tag != None:
        company = company_tag.text.strip()
    else:
        company = "";
    
    create_date_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(12) dd")
    if create_date_tag != None:
        create_date = create_date_tag.text.strip()
    else:
        create_date = "";
    
    washing_method_tag = soup.select_one("div.detailsFull div.properties dl:nth-of-type(11) dd")
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