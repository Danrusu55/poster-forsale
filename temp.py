from imports import *
from models import *


def openFF(userAgent=r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'):
    opts = Options()
    opts.add_argument("user-agent={0}".format(userAgent))
    driver = webdriver.Chrome(executable_path="/Users/danrusu/Dropbox/chromedriver-mac",chrome_options=opts)
    driver.implicitly_wait(10)

    driver.get("https://accounts.craigslist.org/logout")
    inputEmailHandle = driver.find_element_by_id('inputEmailHandle').send_keys('daniel7rusu@gmail.com')
    inputPassword = driver.find_element_by_id('inputPassword').send_keys('$Krys1212')
    driver.find_element_by_xpath("/html/body/section/section/div/div[1]/form/div[3]/button").click()
    return driver


# START APP

db = sqlite3.connect('forsaledb.db')
cursor = db.cursor()

cursor.execute('SELECT * FROM campaigns')
campaigns = cursor.fetchall()
for campaign in campaigns:
    cursor.execute('SELECT * ')



# close connection
db.close()



driver = openFF()

#campaigns = ['plumbing']
# campaigns = ['concrete','carpentry','flooring']
if campaign == 'plumbing':
    postingTitle = '[[PLUMBING]] PLUMBER 24/7! GREAT RATES! - PLUMBERS clogs ect'
    postingBody = 'NEED A LOCAL PLUMBER? <br><br>AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. <br><br>Customer service is a top priority for us, which is why we have served our community well for over 10 years. With a highly trained team behind your back, you can rest assured knowing that your plumbing job will get done right the first time.<br><br>Services include:<br>Water Heater Repair & Install <br> Pipe Replacement & Repairs<br>Drain Cleaning & Unclogging<br>Leaky Faucets Or Pipes.<br>Fixture Installed Plumbing <br>Toilet Installation & Repair.<br>Tub, Shower & Sink Plumber. <br>Anything plumbing.<br>Drain Stoppages<br>Faucets Sinks, Tubs, Toilets<br>Garbage Disposals<br>Leak Repairs<br>Complete Drain Cleaning Services<br>Main Line Stoppages<br>Sink And Toilet Clogs<br>HydroJetting Service<br>Drain Maintenance<br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br>You Name It - We Do It! <br>  Competitive Prices'
    postingGeo = 'Plumber Plumbing Plumbers'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/plumbing.jpg'
elif campaign == 'roofing':
    postingTitle = '((ROOF)) NEED A ROOFER? | ROOFING SERVICES | ROOFERS 24/7'
    postingBody = 'NEED A LOCAL ROOFER? <br><br>AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. <br><br>Want dependable service? Our company has served this area for over 10 years, building long lasting relationships with our team of roofing experts. We can help you with any of your roofing needs.<br><br>CALL 7 DAYS A WEEK / 24 HOURS A DAY FOR EMERGENCIES.<br><br>Roofers for New Installs, Repairs, & Maintenance.<br><br>Services include:<br>New Roof Installations (All Types) <br>Re-Roofs<br>Roof Repairs<br>*Restorations* <br>Leak Detection & Repairs <br>*Emergency*<br><br>No job is too big or too small!<br>Roofers with Years Of Experience <br>Full Service Roofing<br>Competitive Pricing'
    postingGeo = 'roofers roofer roofing replacement repair '
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/roofing1.png'
elif campaign == 'electrical':
    postingTitle = '** LOCAL 24/7 ELECTRICIAN AVAILABLE. ELECTRICAL. ELECTRIC. CALL NOW! '
    postingBody = """NEED A LOCAL ELECTRICIAN? <br><br>AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. <br><br>Want dependable service? Our company has served this area for over 10 years, building long lasting friendships with our valuable team of experts. We can help you with any of your electrical needs.<br><br>AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES.
    <br><br>
    Electrician Specializing in Repairs, Remodels, and new Installs..
    <br><br>
    Services include:<br>
    Wiring & Re-Wiring<br>
    Trouble Shooting<br>
    Service Upgrades<br>
    Outlets<br>
    Lighting Fixtures Installed<br>
    Ceiling & Attic Fans<br>
    *Buzzing or hot outlet *<br>
    *Dimmers * <br>
    *Indoor and outdoor lighting * <br>
    *Motion sensor lights * <br>
    *New circuits * <br>
    *New construction * <br>
    *New receptacles and switches * <br>
    *Recessed lighting * <br>
    <br><br>
    No job is too big or too small!<br>
    Local Electricians with Years Of Experience <br>
    Full Service Electrical Work<br>
    Competitive Pricing"""

    postingGeo = 'roofers roofer roofing replacement repair '
    postingGeo = 'Electrical Electrican Electricians'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/electrical-low.jpg'
elif campaign == 'personalinjury':
    postingTitle = '**24/7 Personal Injury Attorney Attorneys | Lawyer FREE Consult! '
    postingBody = 'Have you or a loved one been injured recently? It is vital that you act quickly to get what\'s owed to you! <br><br> >>>>>>>>>>>>>>>>>>> Why Choose Us?<br><br>- No Fee Unless We Win Your Case!<br>-24 Hour On-Call Help Line<br>-Free injury consultation/case review<br><br>An experienced Personal Injury Lawyer will conduct an investigation while evidence is still intact and witnesses can remember the details of the accident.<br><br> There are statutes of limitations governing many personal injury claims, making it crucial that you file suit before these time limits expire. <br><br>Our attorney, or injury lawyers, can help you navigate this complex process to ensure all deadlines are met and all evidence is properly gathered.<br><br>DON\'T WAIT! CALL US NOW!'
    postingGeo = 'Attorney Attorneys Lawyer Lawyers Law Firm Personal injury'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/pi.jpg'
elif campaign == 'damagerestoration':
    postingTitle = '** Water Flood Fire Damage Restoration - MOLD - 24/7 Service'
    postingBody = 'Need a Restoration contractor for flood/fire damage?<br><br>GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES.<br><br> Water Damage Restoration: Whether you have a flood, an unexpected leak, mold frozen or broken pipe water damage, sewage damage, flooded basement, or fire damage we fully understand the urgency of getting your home repaired and be able to move back in asap. <br><br>That\'s why you need 24 hour water/fire damage response. <br><br>For water damage -<br> The sooner you get the water out, the less damage you\'ll likely incur. Experts say that the worst damage occurs when water has been standing for more than 48 hours, which means timing is everything. <br> For fire damage - the sooner you get everything damaged replaced and repaired, the sooner you can move back in to your beautiful home. <br><br> Make sure you get a contractor that has the necessary equipment for any size job and take care of everything from cleanup to repairs and everything in between. You\'ll get the services you need from us, and nothing else, no pressure sales. Even though the damage may look severe, cleanup and restoration can produce amazing results. We can successfully restore damaged structures for commercial or residential property.'
    postingGeo = 'Water Flood Fire Damage Restoration Contractor'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/damagerestoration.jpg'
elif campaign == 'locksmith':
    postingTitle = '*_ MOBILE **LOCKSMITH** **LOCKSMITHS ** CLICK NOW'
    postingBody = """NEED A LOCAL LOCKSMITH? <br><br>AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. <br><br>We are here for you, for any emergency situation, security problems and day by day service that you need.
    <br><br>
    WE OFFER THE FOLLOWING SERVICES: <br><br>
    Lock Repair<br>
    Lock Replacement<br>
    Lock Installation<br>
    Lock Re-Key<br>
    Master Key Systems<br>
    Lockout solutions<br>
    Emergency mobile locksmith services<br>
    File Cabinet Locks <br>
    Automotive Locksmith Services<br>
    Car Lock Out solutions<br>
    Emergency auto locksmith services<br>
    Car Key cutting <br>
    Mail Box Locks<br>
    <br><br>
    GIVE US A CALL NOW!
    """
    postingGeo = 'Locksmith Locksmiths Emergency'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/locksmith.jpg'

# NOT READY/NOT USED
elif campaign == 'handyman':
    postingTitle = 'Handyman | Drywall | Remodeling | Contractor LOWcost!'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable Handyman Specializing in Kitchens and Bathrooms, Drywall, Carpentry, Electrical, Painting, Plumbing, Tile all types, Pop corn Ceiling removal. <br><br>  I do it all. Give me a call if you want an honest handyman that wont overcharge or skimp on quality.  <br><br>  We Specialize In... <br> Handyman<br> Carpentry<br> Concrete<br> Garage Door<br>  Flooring<br> Heating & Cooling<br> Landscaping<br> Plumbing<br> Painting<br> Remodeling (Kitchen, Bathrooms,etc.)<br>  Roofing<br> Siding<br> Gutters<br> Tiling & More <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Handyman Drywall Remodeling'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/handyman/00M0M_723nJvwoEZf_600x450.jpg'
elif campaign == 'garagedoor':
    postingTitle = 'GARAGE DOOR SERVICE REPAIR SPECIALISTS SAVE $200 GARAGE DOORS '
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable Garage Door company Specializing in Repairs, Maintenance, and new Installs. <br><br>  Our crew does it all. Give me a call if you want honest techs that wont overcharge or skimp on quality.  <br><br>  We Specialize In... Broken springs Replaced <br> Broken or Frayed Cables Replaced <br> Track Straightened or Replaced <br> Service and Installs <br> Roller Serviced or Replace <br> Broken Hinges Replaced <br> Garage Door Opener Repairs <br> New Opener Installations <br> Remotes <br> Rail Repairs <br> General Service and Maintenance <br> Noisy doors Silenced  <br> Broken or cracked rollers <br> Bent Tracks <br> Garage doors  <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Garage Door Repair Springs Garage doors torsion repair'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/garagedoor/1garaged.jpg'
elif campaign == 'flooring':
    postingTitle = '50% Off! CARPET, TILE, HARDWOOD, LAMINATE INSTALL & PRODUCT!'
    postingBody = 'EMPIRE FLOORING. GREAT PRICES AND EXCELLENT WORK (Ask about our current 50% off promotion)!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable Flooring company Specializing in Repairs, Remodels, and new Installs. We provide the product and the install! <br><br>  Our crew does it all. Give me a call if you want honest flooring techs that wont overcharge or skimp on quality.  <br><br>  We Specialize In...  Installation Labor <br> Materials <br> Padding <br> Underlayment <br> Furniture Moving <br> Floor Prep <br> Removal / Haul Away <br> Stair Labor <br> Transitions <br> Base Moldings <br> Product- Carpet, Hardwood, Tile, Vinyl <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices<br><br>(50% Discount is applied to the regular price of select styles of Carpet, Hardwood, Tile and Laminate; basic installation; and standard padding and materials. Excludes stairs, floor prep, take-up of permanently affixed flooring, non-standard furniture moving, upgrades, other miscellaneous charges, and prior purchases. Product may not be sold separate from installation. Residential installations only. Not available in all areas or in stores)"'
    postingGeo = 'Flooring Hardwood Carpet Tile'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/elocal-images/flooring.jpg'
elif campaign == 'remodeling':
    postingTitle = 'Kitchen Bathroom Remodeling General Contractor Additions!!'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable General contractor Specializing in Repairs, Remodels, and new builds. <br><br>  Our crew does it all. Give me a call if you want an honest contractor that wont overcharge or skimp on quality.  <br><br>  We Specialize In... Construction Manager Services <br> General Contracting <br> Design-build Services <br> Excavating <br> Structural Concrete <br> Concrete Flatwork <br> Structural Framing <br> Large and Small Scale Renovation <br> Ground-up Construction <br> Carpentry-all Types <br> Interior Finishes <br> Concrete Countertops <br> Mechanical Design/Installation <br> Electrical Design/Installation <br> Spray Foam Installation <br> Interior and Exterior Painting and Staining <br> Demolition and Clean-up <br> Masonry <br> Roofing <br> Handyman <br> Structural Engineering <br> Architectural Drawings <br> Interior Decorating <br> Landscaping Design & Architecture  <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'general contractor remodeling additions'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/gc/bathroom-renovation-before-and-after.jpg'
elif campaign == 'landscaping':
    postingTitle = 'LANDSCAPING | LAWN CARE | EXCAVATING | TREE SERVICE | YARD WORK'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable landscaping company Specializing in Repairs, Remodels, and new Installs. <br><br>  Our crew does it all. Give me a call if you want honest lawn care workers that wont overcharge or skimp on quality.  <br><br>  We Specialize In...  Manicuring of lawns <br>  Edging and also fertilizing of lawns <br>  Building of yards with dirt and lay grass <br>  Trimming and shaping of bushes <br>  Pruning and cutting down of trees <br>  Planting of trees <br>  Planting of flowers <br>  remove and build fences <br>  build retaining walls   <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Landscaping Lawn Care Yard Tree service'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/landscaping/1.jpg'
elif campaign == 'carpentry':
    postingTitle = 'FENCE | CARPENTRY | DECK | PATIO | We do it all, Low cost!'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable Carpenter Specializing in Fence, Finish work, millwork, deck, moldings, ect. <br><br>  Our crew does it all. Give me a call if you want honest carpenters that wont overcharge or skimp on quality.  <br><br>  We Specialize In... Fine Finish Carpentry, Millwork, Interior and Exterior Woodwork, <br> Custom Built-ins and Shelving, Bench - Storage Units, Desks, <br> Trim, Molding, Wainscot, Paneling, Doors, Windows, Hardware, <br> Butcher Block and Laminate Counters Installation, <br> Interior & Exterior Railing, Decks, Gates, Fences,  <br> Fabrication, Installation, Re-facing.<br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Fence Deck Carpentry Millwork Woodwork'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/carpentry/1.jpg'
elif campaign == 'concrete':
    postingTitle = 'CONCRETE | BRICK | DRIVEWAY | DRIVEWAYS | GET A QUOTE!'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable concrete company Specializing in Masonry, patio, driveway, brickwork, asphalt, ect. <br><br>  Our crew does it all. Give me a call if you want honest works that wont overcharge or skimp on quality.  <br><br>  We Specialize In... masonry work custom work/concrete/block and brick wall and fireplaces  <br>home additions  <br>drywall  <br>stucco fire pits  <br>flagstone  <br> pavers patio  <br>walkway <br> wood rot repair  <br>pool repairs  <br> spa repair <br> driveways <br> pathways <br> sidewalks <br> wooden decks <br> Jacuzzi brick around <br> pool decking <br> plumbing copping <br> tile <br> Mexican tile  <br>water fall <br> light fixtures <br> water fountains and plumbing<br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Concrete Driveway Brick Masonry Patio'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/concrete/1.jpg'
elif campaign == 'painting':
    postingTitle = 'INTERIOR & EXTERIOR PAINTING | BEST PAINTER PAINTERS!!'
    postingBody = 'GREAT PRICES AND EXCELLENT WORK!! AVAILABLE 7 DAYS A WEEK/24 HOURS A DAY FOR EMERGENCIES. ALL WORK GUARANTEED.<br><br> Affordable Painter Specializing in Repairs, Remodels, and new Installs. <br><br>  Our crew does it all. Give me a call if you want honest painters that wont overcharge or skimp on quality.  <br><br>  We Specialize In... INTERIOR/EXTERIOR <br> RESIDENTIAL/COMMERCIAL <br> HOMES,OFFICES,APARTMENTS,BUILDINGS <br> WE\'LL PATCH AND PAINT BEDROOMS,LIVING ROOMS,KITCHENS,BATHROOMS <br> DOORS,CEILINGS,WINDOWS,GARAGES <br> EVERYTHING INSIDE AND OUT  <br><br>   No job is too big or too small for us, we do it all!<br> We Have Years Of Experience <br> 100% Satisfaction Guaranteed <br> You Name It - We\'ll Do It! <br>  Competitive Prices'
    postingGeo = 'Painting Painter Painters'
    imgPath = '/Users/danrusu/Dropbox/campaign-images/painting/1.jpg'

for city in citiesArray:
    driver.get(city[0])
    try:
        driver.find_element_by_xpath('//*[@id="post"]').click()
    except:
        pass
    WebDriverWait(driver, 5).until(EC.title_contains("choose type"))
    driver.find_element_by_xpath("/html/body/article/section/form/blockquote/label[7]/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/article/section/form/blockquote/label[24]/input").click()
    time.sleep(1)

    # subcity
    try:
        driver.find_element_by_xpath("/html/body/article/section/form/blockquote/label[1]/input").click()
    except:
        pass

    # neighborhood
    if 'sfbay' in city[0] or 'nyc' in city[0]:
        try:
            driver.find_element_by_xpath("/html/body/article/section/form/table/tbody/tr/td[1]/blockquote/label[1]/input").click()
        except:
            pass

    if driver.find_element_by_id('contact_phone_ok').is_selected():
        driver.find_element_by_id('contact_phone_ok').click()
    if driver.find_element_by_id('contact_text_ok').is_selected():
        driver.find_element_by_id('contact_text_ok').click()
    driver.find_element_by_id('PostingTitle').send_keys(postingTitle)
    driver.find_element_by_id('PostingBody').send_keys('<h1>CALL US RIGHT NOW! ',city[1],'</h1><br>',postingBody)
    driver.find_element_by_id('Ask').send_keys(askingPrice)
    try:
        driver.find_element_by_id('GeographicArea').send_keys(postingGeo)
    except:
        pass
    driver.find_element_by_id('postal_code').send_keys(zipCode)
    driver.find_element_by_id('sale_manufacturer').send_keys(postingGeo)
    driver.find_element_by_id('sale_model').send_keys(postingGeo)
    driver.find_element_by_id('sale_size').send_keys(postingGeo)
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
        print('started image for ' + city[0])
        driver.find_element_by_xpath("//*[@id=\"uploader\"]/form/input[3]").send_keys("{0}".format(imgPath))
        time.sleep(3)
        imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
        print('image count found first ' + str(imgCount))
        imgWaitTimer = 0
        while int(imgCount) != 1:
            time.sleep(1)
            imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
            print('image count found in loop ' + str(imgCount))
            imgWaitTimer += 1
            print(imgWaitTimer)
            if imgWaitTimer == 10:
                break
        imgCount = driver.find_element_by_xpath("//*[@class='imgcount']").text
        print('image count found last ' + str(imgCount))
        if int(imgCount) == 1:
            break

    driver.find_element_by_xpath("//*[@value='Done with Images']").click()

    # END IMAGE WORK

    driver.find_element_by_xpath("//*[@value='Continue']").click()

    driver.find_element_by_xpath("//*[@value='Continue']").click()

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
