from selenium.webdriver.support import expected_conditions as EC
from behave import *
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait








@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome('C:/bin/chromedriver')


@when('open scanmalta page')
def openHomePage(context):
    context.driver.get('https://www.scanmalta.com/')


@then('verify that the logo present on page')
def verifyLogo(context):
    time.sleep(2)  # Let the user actually see something!
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/header/div/div/div/div/div[1]/strong/img[1]')))
    time.sleep(2)
    page_title = context.driver.title
    print("The title is ", page_title)
    time.sleep(10)
    assert page_title == 'Computers Store Malta | SCAN'
    if not "Computers Store Malta | SCAN" in context.driver.title:
        raise Exception("Unable to load Computers Store Malta page!")


@then('search for Lenovo laptop')
def searchLenovo(context):
    # Search input for laptop
    search = context.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/header/div/div/div/div/div[3]/div/div[3]/div[2]/div[1]/form/div[1]/input')
    search.send_keys('Lenovo Laptop')
    time.sleep(3)

    search_click = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/header/div/div/div/div/div[3]/div/div[3]/div[2]/div[1]/form/div[3]/button/span')
    search_click.click()
    time.sleep(5)


@then('add the product to your shopping cart')
def addLenovo(context):
    click_lenovo = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[5]/div[2]/ol/li[1]/div/div[2]/strong/a')
    click_lenovo.click()
    time.sleep(5)

    add_warranty = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[3]/div/div[1]/div/div/div[2]/input')
    add_warranty.click()
    time.sleep(3)

    add_warranty_microsoft = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[3]/div/div[2]/div/div/div[2]/input')
    add_warranty_microsoft.click()
    time.sleep(3)

    add_to_cart = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[4]/div/div/div[2]/button')
    add_to_cart.click()
    time.sleep(5)

@then('assert that the item has been added to your cart')
def assertLenovo(context):
    checkout_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/button[2]').is_displayed()
    assert checkout_button is True
    time.sleep(5)

@then('the product pricing matches the one listed in the single product page view.')
def assertPrice(context):
    price_cart = context.driver.find_element(By.CSS_SELECTOR, "span[class='price']")
    price_cart = price_cart.text
    print('The price_cart is ', price_cart)

    time.sleep(3)
    keep_shopping_button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/button[1]/span/span')
    keep_shopping_button.click()

    time.sleep(3)
    price_before_cart = context.driver.find_element(By.XPATH, '//*[@id="product-price-33145"]')
    #price_before_cart = context.driver.find_element(By.CSS_SELECTOR, "span[class='price']")
    price_before_cart = price_before_cart.text
    print('The price_before_cart is ', price_before_cart)


    if price_cart == price_before_cart:
        print("Assertion is correct")
        return 1
    else:
        print("Test Lenovo failed")
        return 0
    print("Scenario 1 has finished.")


@then('close browser')
def closeBrowser(context):
    context.driver.close()















@given('launch chrome browser2')
def launchBrowser(context):
    context.driver = webdriver.Chrome('C:/bin/chromedriver')


@when('open scanmalta page2')
def openHomePage(context):
    context.driver.get('https://www.scanmalta.com/')


@then('verify that the logo present on page2')
def verifyLogo(context):
    time.sleep(2)  # Let the user actually see something!
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/header/div/div/div/div/div[1]/strong/img[1]')))
    time.sleep(2)
    page_title = context.driver.title
    print("The title is ", page_title)
    time.sleep(10)
    assert page_title == 'Computers Store Malta | SCAN'
    if not "Computers Store Malta | SCAN" in context.driver.title:
        raise Exception("Unable to load Computers Store Malta page!")


@then('search for Apple Macbook2')
def searchMacBook(context):
    # Search input for laptop
    search = context.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/header/div/div/div/div/div[3]/div/div[3]/div[2]/div[1]/form/div[1]/input')
    search.send_keys('Apple Macbook')
    time.sleep(3)

    search_click = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/header/div/div/div/div/div[3]/div/div[3]/div[2]/div[1]/form/div[3]/button/span')
    search_click.click()
    time.sleep(5)

    sorting_tab_button = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[5]/div[1]/div[4]/select')
    sorting_tab_button.click()
    time.sleep(5)

    sel = Select(context.driver.find_element(By.ID, "sorter"))
    sel.select_by_visible_text('Price')
    time.sleep(8)

    macbook_button = context.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div[3]/div/div[2]/ol/li[1]/div/div[2]/strong/a')
    macbook_button.click()
    time.sleep(3)


@then('add the products twice to your shopping cart2')
def addMacbooks(context):

    add_warranty = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[3]/div/div[1]/div/div/div[2]/input')
    add_warranty.click()
    time.sleep(3)

    add_warranty_microsoft = context.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[3]/div/div[2]/div/div/div[2]/input')
    add_warranty_microsoft.click()
    time.sleep(3)

    add_2_button =  context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[4]/div/div/div[1]/div/div/div[2]/button')
    add_2_button.click()
    time.sleep(3)


    add_to_cart = context.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/form/div/div[2]/div[4]/div/div/div[2]/button')
    add_to_cart.click()
    time.sleep(10)

@then('assert that the items have been added to your cart2')
def assertMacbook(context):
    quantity = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/ol/li/div/div[2]/div/div[2]/div/div[2]/input').get_attribute("data-item-qty")
    print("To quantity einai ", quantity)
    time.sleep(10)

    checkout_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/button[2]/span').is_displayed()
    assert checkout_button is True
    time.sleep(3)

@then('assert the total price is correct2')
def assertPrice(context):
    total_price = context.driver.find_element(By.CSS_SELECTOR, "span[class='price']")
    total_price = total_price.text
    total_price = re.sub('€', '', total_price)
    total_price = re.sub(',', '', total_price)
    #total_price = re.sub('.', ',', total_price)
    print("The total_price is ", total_price)
    total_price = float(total_price)

    print('The total_price is ', total_price)

    time.sleep(3)
    keep_shopping_button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/button[1]/span/span')
    keep_shopping_button.click()

    time.sleep(3)
    #price_before_cart = context.driver.find_element(By.CSS_SELECTOR, "span[class='price']")
    #price_before_cart = price_before_cart.text
    price_before_cart = context.driver.find_element(By.XPATH, '//*[@id="product-price-30388"]')
    price_before_cart = price_before_cart.text
    price_before_cart = re.sub('€', '', price_before_cart)
    price_before_cart = re.sub(',', '', price_before_cart)
    #price_before_cart = re.sub('.', ',', price_before_cart)
    price_before_cart = float(price_before_cart)

    print('The price_before_cart is ', price_before_cart)

    if (price_before_cart * 2) == total_price:
        print("Assertion is correct")
        return 1
    else:
        print("Test Macbook failed")
        return 0
    #assert total_price  price_before_cart
    print("Scenario 1 has finished.")
    time.sleep(10000)


@then('close browser2')
def closeBrowser(context):
    context.driver.close()