from imports import *
from models import *
from cardinfo import *

def openFF(userAgent=r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'):
    driver = webdriver.Firefox(timeout=30)
    driver.implicitly_wait(2)
    driver.set_window_size(800,800)
    return driver

def login(driver,login,password):
    driver.get("https://accounts.craigslist.org/logout")
    inputEmailHandle = driver.find_element_by_id('inputEmailHandle').send_keys(login)
    inputPassword = driver.find_element_by_id('inputPassword').send_keys(password)
    driver.find_element_by_xpath("/html/body/section/section/div/div[1]/form/div[3]/button").click()
    try:
        WebDriverWait(driver, 7).until(EC.title_contains("craigslist account"))
        return True
    except:
        loginError = driver.find_element_by_xpath("//*[@role='alert']").text
        # if "password is incorrect" or "placed on hold" or "reset your" in loginError:
        raise MyException('For login: ' + login + 'showed: ' + loginError)

def postAd(city,campaign):
    driver.get(city.mainurl)
    driver.find_element_by_xpath('//*[@id="post"]').click()
    WebDriverWait(driver, 5).until(EC.title_contains("choose type"))
    # for sale by dealer
    time.sleep(2)
    driver.find_element_by_xpath("//*[@value='fsd']").click()
    # general
    time.sleep(2)
    driver.find_element_by_xpath("//*[@value='179']").click()
    # subcity
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@value='1']").click()
    except:
        pass

    # PUT IN AD CONTENT
    if driver.find_element_by_id('contact_phone_ok').is_selected():
        driver.find_element_by_id('contact_phone_ok').click()
    if driver.find_element_by_id('contact_text_ok').is_selected():
        driver.find_element_by_id('contact_text_ok').click()
    randNum = random.randint(1,5)
    if randNum == 1:
        title = campaign.title1
    elif randNum == 2:
        title = campaign.title2
    elif randNum == 3:
        title = campaign.title3
    elif randNum == 4:
        title = campaign.title4
    elif randNum == 5:
        title = campaign.title5
    # .encode('utf8') if python2
    driver.find_element_by_id('PostingTitle').send_keys(title)
    driver.find_element_by_id('PostingBody').send_keys('<h1> CALL: ',city.phone,'</h1>',campaign.body)
    driver.find_element_by_id('GeographicArea').send_keys(campaign.licloc)
    driver.find_element_by_id('postal_code').send_keys('98011')
    driver.find_element_by_id('sale_manufacturer').send_keys(campaign.licloc)
    driver.find_element_by_id('sale_model').send_keys(campaign.licloc)
    driver.find_element_by_id('sale_size').send_keys(campaign.licloc)
    if driver.find_element_by_id('wantamap').is_selected():
        driver.find_element_by_id('wantamap').click()
    if driver.find_element_by_id('see_my_other').is_selected():
        driver.find_element_by_id('see_my_other').click()

    driver.find_element_by_xpath("//*[@id=\"postingForm\"]/button").click()

    # IMAGE WORK
    try:
        driver.find_element_by_xpath("//*[@id=\"classic\"]").click()
    except:
        pass
    while True: # repeat image attempt
        driver.find_element_by_xpath("//*[@id=\"uploader\"]/form/input[3]").send_keys("{0}{1}".format(imgPath,campaign.image))
        time.sleep(3)
        imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
        imgWaitTimer = 0
        while int(imgCount) != 1:
            time.sleep(1)
            imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
            imgWaitTimer += 1
            if imgWaitTimer == 10:
                break
        imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
        if int(imgCount) == 1:
            break
    driver.find_element_by_xpath("//*[@value='Done with Images']").click()
    driver.find_element_by_xpath("//*[@value='Continue']").click()
    driver.find_element_by_xpath("//*[@value='Continue']").click()

    # FILL IN CARD INFO
    while True:
        driver.find_element_by_id('cardNumber').send_keys(cardNum)
        driver.find_element_by_name('cvNumber').send_keys(cardCv)
        driver.find_element_by_name('expMonth').send_keys(cardMonth)
        driver.find_element_by_name('expYear').send_keys(cardYear)
        driver.find_element_by_name('cardFirstName').send_keys(cardFirstName)
        driver.find_element_by_name('cardLastName').send_keys(cardLastName)
        driver.find_element_by_name('cardAddress').send_keys(cardAddress)
        driver.find_element_by_name('cardCity').send_keys(cardCity)
        driver.find_element_by_name('cardState').send_keys(cardState)
        driver.find_element_by_name('cardPostal').send_keys(cardPostal)
        driver.find_element_by_name('contactName').send_keys(cardContactName)
        driver.find_element_by_name('contactPhone').send_keys(cardContactPhone)
        driver.find_element_by_name('finishForm').click()
        if 'Please enter' not in driver.find_element_by_xpath("//*[@class=\"highlight\"]").text:
            break

    # CONFIRMATION
    try:
        driver.find_element_by_id("postingInvoice")
        City.update(lastposted=today).where(City.id == city.id).execute()
        return 'success'
    except:
        if 'invalid' in driver.find_element_by_xpath("//*[@class=\"highlight\"]").text:
            raise MyException('Forsale app err Invalid card information')
        else:
            raise MyException('Some other error on confirmation page')

def sendText(message):
    sender = 'bullhorn0002@gmail.com'
    receiver = '9495310422@vtext.com'
    username = 'bullhorn0002@gmail.com'
    password = 'superman07'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(sender,receiver,message)
        server.quit()
    except Exception as err:
        logging.exception(err)

# START APP
if __name__ == '__main__':
    try:
        driver = openFF()
        campaigns = Campaign.select()
        for campaign in campaigns:
            login(driver,campaign.login,campaign.password)
            cities = City.select().where(City.campaign_id == campaign.id)
            for city in cities:
                # skipping if not long enough
                daysPast = ((today - city.lastposted).days)
                print('Working on campaign,city: ' + str(campaign.name) + ', ' + str(city.city))
                if daysPast < city.daystowait:
                    print('skipping ' + str(city.city) + ' : ' + str(daysPast) + ' days')
                    continue
                else:
                    postingStatus = postAd(city,campaign)
    except NoSuchElementException as err:
        sendText('Forsale app err Element not found')
        logging.exception('Forsale app err Element not found')
    except MyException as err:
        sendText(err)
        logging.exception(err)
    except Exception as err:
        logging.exception(err)
    finally:
        sys.exit()
