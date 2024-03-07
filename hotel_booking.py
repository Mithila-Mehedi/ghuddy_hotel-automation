import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



driver =webdriver.Chrome()
driver.get("https://dev.ghuddy.com")
parent_window = driver.current_window_handle
webTitle = driver.title
print("TITLE : ",webTitle)

driver.maximize_window()

driver.find_element(By.ID,"navbarLoginButton").click()
print("navigate to the login page by clicking on the login button")
time.sleep(1)
driver.find_element(By.NAME, "phone").send_keys("1784349364")
print("enter your phone number")
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
print("click on `Submit` button")
time.sleep(1)
driver.find_element(By.ID, "password1").send_keys("123456")
print("enter your password")
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
print("click on `Submit` button and go to homepage of Ghuddy")
time.sleep(2)



#####Book Hotel#######

## Go to hotel M.V.Crown2
driver.find_element(By.XPATH, "//*[contains(text(), 'M.V.Crown2')]").click()
print("click and go to specific hotel")
time.sleep(2)
child_windows = driver.window_handles
# print("child windows : ",child_windows)
for child in child_windows:
    if parent_window != child:
        driver.switch_to.window(child)
        time.sleep(3)
        print("Child window:", driver.title)

        add_button_xpath = "//body//div//div//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[2]//div[2]//div[3]//div[1]//div[1]//div[2]//button[2]"

        # Wait for the "Add" button to be clickable before clicking
        wait = WebDriverWait(driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))

        # Function to click the element with overlap handling
        def click_element_with_overlap_handling(driver, element):
            try:
                # Try clicking the element directly
                element.click()
                print("Room added successfully")
            except Exception as e:
                # If the direct click fails, handle the overlapping element

                # Find the coordinates of the element
                location = element.location_once_scrolled_into_view
                x, y = location['x'], location['y']

                # Execute JavaScript to remove the overlapping element from the DOM
                driver.execute_script("document.elementFromPoint(arguments[0], arguments[1]).remove();", x, y)

                # Retry clicking the element after removing the overlapping element
                element.click()
                print("overlapped guest element is removed")

        # Use the custom function to click the "Add" button with overlap handling
        click_element_with_overlap_handling(driver, add_button)

        # Assuming there is a submit button for the overlapping element
        overlapping_submit_xpath = "//span[contains(@class,'absolute xl:left-[0rem] xl:top-[7rem] w-[34.3rem] msm:w-[43rem] sm:w-[42rem] md:w-[49rem] right-0 xl:w-2/3 xl:max-w-[65.3rem] top-[6rem] hidden xl:block z-[2000]')]//button[contains(@class,'bg-btn-primary hover:bg-btn-secondary w-full rounded-[16px] mt-[1.75rem] text-txt-secondary py-3.5')][normalize-space()='Submit']"

        # Wait for the submit button to be clickable before clicking
        overlapping_submit = wait.until(EC.element_to_be_clickable((By.XPATH, overlapping_submit_xpath)))

        # Click the submit button for the overlapping element
        overlapping_submit.click()
        print("Overlapping element handled successfully")

        try:
            # Wait for the element to be clickable within a longer time frame (e.g., 20 seconds)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
            element.click()
            print("Element clicked successfully and added a room for checkout")
            time.sleep(5)
        except TimeoutException:
            print(e)

    ## Checkout

    checkout_button_xpath = "//div[contains(@class,'flex justify-start items-center gap-x-[8px] mt-[47px]')]//button[contains(@class,'')][normalize-space()='Checkout']"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkout_button_xpath)))
        element.click()
        print("checkout button clicked successfully")
        time.sleep(3)
    except TimeoutException as e:
        print(e)

    ## Proceed with booking
    visa_card_xpath = "//input[@id='default-radio-2']"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, visa_card_xpath)))
        element.click()
        print("Visa card clicked successfully")
        time.sleep(2)
    except TimeoutException as e:
        print(e)

    ## Agree with TNC by checking the checkbox

    checkbox_xpath = "//div[@class='min-w-[16px] min-h-[16px] border-[1.5px] rounded-[4px] border-btn-secondary']"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
        element.click()
        print("agreement checked successfully")
        time.sleep(2)
    except TimeoutException as e:
        print(e)

    ## Go to step 2 by clicking on PROCEED WITH BOOKING button

    proceed_with_booking_xpath = "//button[contains(@class,'w-full rounded-full border border-btn-primary py-[12px] bg-btn-primary cursor-pointer text-bg-primary hover:bg-btn-secondary hover:border-btn-secondary text-base14 active:bg-bg-primary active:border active:border-btn-secondary active:text-btn-secondary')]"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, proceed_with_booking_xpath)))
        element.click()
        print("Proceed with booking successfully")
        time.sleep(2)
    except TimeoutException as e:
        print(e)

    ## select address
    address_xpath = "//button[normalize-space()='Next']"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, address_xpath)))
        element.click()
        print("Address selected successfully")
        time.sleep(2)
    except TimeoutException as e:
        print(e)

    ## proceed with payment
    proceed_with_payment_xpath = "//button[contains(@class,'w-full rounded-full border border-btn-primary py-[12px] bg-btn-primary cursor-pointer text-bg-primary hover:bg-btn-secondary hover:border-btn-secondary text-base14 active:bg-bg-primary active:border active:border-btn-secondary active:text-btn-secondary')]"
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, proceed_with_payment_xpath)))
        element.click()
        print("Proceed with payment successfully")
        time.sleep(2)
    except TimeoutException as e:
        print(e)

    ## bank details

    card_name = "cardNumber"
    card_name_to_send = "4012001037141112"
    card_exp_month = "expMnth"
    card_exp_month_to_send = "12"
    card_exp_year = "expYear"
    card_exp_year_to_send = "27"
    card_holder_name = "cardholderName"
    card_holder_name_to_send = "Automation"
    pay_xpath = "//input[@id='proceed"
    cvv = "cardCvv"
    cvv_to_send = "212"



    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, card_name)))
        element.send_keys(card_name_to_send)

    except TimeoutException as e:
        print(e)

    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, card_exp_month)))
        element.send_keys(card_exp_month_to_send)
    except TimeoutException as e:
        print(e)

    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, card_exp_year)))
        element.send_keys(card_exp_year_to_send)
    except TimeoutException as e:
        print(e)

    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, cvv)))
        element.send_keys(cvv_to_send)
    except TimeoutException as e:
        print(e)

    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, card_holder_name)))
        element.send_keys(card_holder_name_to_send)
    except TimeoutException as e:
        print(e)

    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, pay_xpath)))
        element.click()
    except TimeoutException as e:
        print(e)









