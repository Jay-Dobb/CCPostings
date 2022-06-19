from __future__ import print_function

import time
from datetime import date

from text_unidecode import unidecode

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import gspread
from oauth2client.service_account import ServiceAccountCredentials


PATH = "C:\Tools\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#driver.get( 'https://yakima.craigslist.org/search/moxee-wa/jjj?query=%28remote+%7C+%22work+from+home%22%29+-%28%22%2421.25%22%29+-%28lawyer%29+-%28%22law+program%22%29+-%28cleaner%29+-%28hairdresser%29+-%28%22Free+Employment%22%29+-driver+-mother&lat=46.7221&lon=-120.1035&sort=date&search_distance=250')

gc = gspread.service_account(filename='mycredentials.json')

#Craigslist URLS
craiglistURLS = []
urlNum = 0

#Scraping All Listings Information from site for current day
allTitleListings = []
allHyperlinksListings = []
allDatesListing = []
# allLocationListing = [] #not yet used
allCityListing = []
fullBodyText = []

#Cleaned All Listings Info for current day
noDupTitleListings = []
noDupHyperlinksListings = []
noDupDatesListing = []
#noDupLocationListing = [] #not yet used
noDupCityListing = []
slimBodyText =[]

combinedInfoListings = []


def currentDate():
    today = date.today()
    print("Today's date:", today)

    if stopAtdate == 'Today':
        d4 = today.strftime("%b-%d")
        #print("d4 =", d4)


        # converting number in date into Int from strong
        dayint = int(d4[4:6])
        # print("day number ", dayint)
        # print("day number type", type(dayint))

        if dayint > 9:
            d5 = d4[:3] + " " + d4[4:6]
            #print("d5 = ", d5)
        else:
            d5 = d4[:3] + " " + d4[5:6]
            #print("d5 = ", d5)
        return d5

    else:
        print("Scraping List from: ", stopAtdate)

def craigslistCatergories():  #maybe add this to a seperate code page, it calls this not to overload the memory

    #iteration through each type of search add to (Seperate Google sheet or tab?? **Comment limit**

    # All Categories  #seperateSheet Doc
    allCategoriesSearch = 0

    if allCategoriesSearch == 0:
        partTime = 0
        fullTime = 0
        pass

    #ALL GIG work
    gigIndustSearch = 0
    if gigIndustSearch == 0:
        partTime = 0
        fullTime = 0
        pass

    #Tech = Craigslist catergory: Software /QA / DBA + Systems + Technical Support + Arch / Engineering +  Biotech Tech / Science + Web info Design
    techIndustSearch =0

    if techIndustSearch == 0:
        partTime = 0
        fullTime = 0
        pass

    #Admin Office + Accounting/Finance + Buiness Mgment + Goverment + Human Resources + Sales / Biz Dev
    adminIndustSearch = 0
    if adminIndustSearch == 0:
        partTime = 0
        fullTime = 0
        pass

    #Customer - Marketing / PR + Customer Serivce + Art/Media/Design
    #adminIndustSearch = 0
    #if adminIndustSearch == 0:
       # partTime = 0
        #fullTime = 0
        #pass

    #EDU  - Education + Nonprofit Sector + Biotech Tech / Science
    #adminIndustSearch = 0
    #if adminIndustSearch == 0:
       # partTime = 0
        #fullTime = 0
        #pass

def injectCraigslistURLS():

    #WestCoast North WASH/Van
    craiglistURLS.append('https://yakima.craigslist.org/search/moxee-wa/jjj?sort=date&lat=46.7221&lon=-120.1035&search_distance=250')

    #WestCoast South Cali/Nevada
    #craiglistURLS.append('https://visalia.craigslist.org/search/independence-ca/jjj?sort=date&lat=36.7973&lon=-117.6027&search_distance=250')

def locationListings():
    #something something
    # scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost
    pass

def filterSearch(urlNum):

    print("filtersearch url", urlNum)

    driver.get(craiglistURLS[urlNum])
    searchbox = driver.find_element(By.CSS_SELECTOR, '.querybox')
    # searchField = searchbox.find_element(By.TAG_NAME, 'input').get_attribute('value')
    # print("what is currently in searchbox", searchField)

    inputbox = searchbox.find_element(By.NAME, 'query')
    inputbox.send_keys(craigslistSearchFilter)
    inputbox.send_keys(Keys.RETURN)

def webscrapTitlesList():

    results = driver.find_elements(By.CLASS_NAME, 'result-row')
    webEle = results[0].find_element(By.CSS_SELECTOR, '.result-info')
    location = results[0].find_element(By.CSS_SELECTOR, '.result-meta')

    eachitem = 0
    for x in results:
            webEle = results[eachitem].find_element(By.CSS_SELECTOR, '.result-info')

            #DATE OF LISTING
            dateListing = unidecode(webEle.find_element(By.TAG_NAME, 'time').text) #  TAG NAME IS at end time>
            #print(dateListing)

            #TITLE POSTING NAME
            #<a  ***  href= *** "https://charleston.c.html" data-id="7492752531"  id="postid_7492752531"> the title to see here *** </a> **
            titleListing =(unidecode(webEle.find_element(By.TAG_NAME, 'a').text))
            #print(titleListing)

            #HYPERLINK
            # within <a/> find attritube href (hyperlink)
            hyperLinkitem = webEle.find_element(By.TAG_NAME, 'a').get_attribute('href')
            #hyperLinkitem = hyperLinkitem[8:]

            #print("sliced out https: ",hyperLinkitem)
            #print(hyperitem)
            #print(eachitem + 1)

            #CITY
            #<span class="result-meta">
            # <span class="nearby" title="vancouver, BC">(van &gt; Downtown Vancouver) *** </span> ***
            location = results[eachitem].find_element(By.CSS_SELECTOR, '.result-meta')
            cityListing = unidecode(location.find_element(By.TAG_NAME, 'span').text)
            #print(city)

            #adding to lists
            allTitleListings.append(str(titleListing))
            allHyperlinksListings.append(hyperLinkitem)
            allDatesListing.append(dateListing)
            allCityListing.append(cityListing)

            eachitem = eachitem + 1

            #STOPS EXTRACTING LIST AT TODAYS DATE
            if stopAtdate != "ALL":
                if (unidecode(webEle.find_element(By.TAG_NAME, 'time').text)) != stopAtdate:
                    break

    driver.quit()
    print(stopAtdate, ": All Posting Items = ", eachitem)

def titlesListclean():
    # Removes Duplicate names in main list and aligns list index for each other list and deletes those itmes
    nameSet = set()
    item = 0
    for tt, hyper, dd, city in zip(allTitleListings,allHyperlinksListings,allDatesListing,allCityListing):
        if tt not in nameSet:
            noDupTitleListings.append(tt)
            noDupHyperlinksListings.append(hyper)
            noDupDatesListing.append(dd)
            noDupCityListing.append(city)
            # vvv what makes it work
            nameSet.add(tt)
            item = item + 1
            Combined = dd + " |" + str(item) + ". " + tt + " | " + city + " | " + hyper
            combinedInfoListings.append(Combined)

    noDupTitleListings.pop(len(noDupTitleListings) - 1)
    noDupHyperlinksListings.pop(len(noDupTitleListings) - 1)
    noDupDatesListing.pop(len(noDupDatesListing) - 1)
    noDupCityListing.pop(len(noDupCityListing) - 1)
    combinedInfoListings.pop(len(combinedInfoListings) - 1)
    print(stopAtdate,": Postings Items After Cleaned Duplicates = ",len(combinedInfoListings))
    print("----- Scraping & Formatting.. ----- ")
    print(" ")

def webscrapBodyText():

    PATH = "C:\Tools\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    index = 0
    for indexlist in noDupHyperlinksListings:

        driver.get(noDupHyperlinksListings[index])
        urldriver = driver.get(noDupHyperlinksListings[index])

        ###Test Prints
        #print("HyperLink:",index," ",noDupHyperlinksListings[index])
        #print("urldriver ",urldriver)
        #print("body driver find element by css ",body)
        #print("bodytext findelement by tag",bodytext)

        # <span class="result-meta">
        # <span class="nearby" title="vancouver, BC">(van &gt; Downtown Vancouver) *** </section> ***
        body = driver.find_element(By.CSS_SELECTOR, '.userbody')
        bodytext = unidecode(body.find_element(By.TAG_NAME, 'section').text)

        #Adding to Body List
        fullBodyText.append(bodytext)

        #Preview skim body prints with index of other lists
        skimBody = (fullBodyText[index])
        #print("(loc: webscrapBodyText)", " index Title:",index,"- ", noDupTitleListings[index],noDupHyperlinksListings[index] , " | Sample Body text: ", skimBody[0:25])

        index = index + 1
        if index == stopscrapAtList:
            print(" ")
            driver.quit()
            break

def bodytextListSlim():

    index = 0
    amount = shortenBodyTextLettersTo   #slim down body of text below 1900 characters. removing between string [ :X-400 and X-200: ]
    print("[Output]:")
    for bodytext in fullBodyText:
        print("Grabbing Body Text from: Index", index, " ", noDupTitleListings[index])
        print("length of body text letters: ", len(bodytext))
        #print(bodytext)

        if len(bodytext) > amount:
            while len(bodytext) > amount:
                bodytext = bodytext[0:len(bodytext)-400] + bodytext[len(bodytext)-200:]
                #print("new length of body each time", len(bodytext))
            else:
                #print("new length of body letters: ", len(bodytext)) #finished while loop
                pass

        else:
            #print("Length of body text less than ",amount)
            #bodytextListSlim().append(bodytext)
            pass

        #Ended while conditonal, so add slimmed body text
        slimBodyText.append(bodytext)

        #print("HyperLink index:",index," ",noDupHyperlinksListings[index])

        #slice bodytext to preview output with skim
        skimBody = (slimBodyText[index])
        #print("Bodytext Index:",index," ",skimBody[0:22])
        #print("       ")

        index = index + 1

def bodytextATSfilterkeywords():
    #further filter with python manipulation
    print("test")

def injectToSheets():

    scope=   ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    credentials=ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
    gc=gspread.authorize(credentials)
    wks=gc.open('Sele').sheet1

    cListing = 0

    #Slices all strings in hyperlink list to remove https://
    stripHyperlinksListing = [w[8:] for w in noDupHyperlinksListings]

    for items in noDupTitleListings:

        wks.append_row([noDupDatesListing[cListing], stripHyperlinksListing[cListing], noDupTitleListings[cListing], noDupCityListing[cListing]])
        #[gColDate,gColLocation,gColTitle,gColHyperComment,created_on,updated_on] google sheet field    #names.
        print("Index ", cListing, " Inserted Successfully ! Title:", noDupTitleListings[cListing])
        cListing = cListing + 1

def injectBodyCommentsToSheet():

    driver.get('https://docs.google.com/spreadsheets/d/14Ns_4P9OVNf_Z2pzQ2KVrdzzmjmip9etf2-zZHJmdOw/edit?usp=sharing')

    combine_keys = ActionChains(driver)
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(1)
    combine_keys.key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("m").key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    actions.send_keys('craigslist job description')
    actions.send_keys(Keys.ENTER).perform()
    actions.send_keys(Keys.ENTER).perform()

def resultsToNotepad():
    print("- - - - - - - - -")
    print("Packing Data Into Notepad...")

    index = 0

    with open('ListOutput.txt', 'w') as f:
        for x in noDupTitleListings:
            f.write(str(combinedInfoListings[index] + slimBodyText[index]))
            f.write('\n')
            f.write(" ------------------------------------------------- ")
            f.write('\n')
            f.write('\n')
            index = index + 1

            if index == stopscrapAtList:
                break

    #TO SEE EACH ITEM LIST SEPERATE
    for x in noDupTitleListings:
        #print("Listing:",item," ",noDupDatesListing[item]," | ",noDupTitleListings[item]," || ",noDupCityListing[item]," || ",noDupHyperlinksListings[item])
        pass

    # SEE COMBINED ITEMS IN ONE LIST
    for y in noDupHyperlinksListings:
        #print(y)
        pass

#----------------------------------------------
#TO DO NEXT
# Manipulate GoogleSheets
# scrap by categories grouped
# scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost

printProcessDebug = True  #If True will print all outputs in each function to see whats going on (Not seutp yet)

# Modifiers
# Filter craigslist wildcards
# Prematurely stop scrap at list
# Date To Stop scrap(Current Date)
# Reduce Body text posting amount

craigslistSearchFilter = '(remote | "work from home") -("$21.25") -(lawyer) -("law program") -(cleaner) -(hairdresser) -("Free Employment") -driver -mother'
stopAtdate = "Jun 18"
#stopAtdate = input("Type Today or the Date to Scrape: ")   #Specify Date or Put in 'Today'
stopscrapAtList = 3
shortenBodyTextLettersTo = 1900

def sheettest():

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Sele').sheet1


    cella1 = wks.get_values("A1")
    print(cella1)


    #range = wks.getRange('B5')
    #range.activate()

    #selection = sheet.getSelection()
    #currentCell = B5
    #currentCell = selection.getCurrentCell()

injectBodyCommentsToSheet()

'''

#make this in new py file so it doesnt over load memory?
injectCraigslistURLS()
for x in craiglistURLS:
    print("In Url list Index", urlNum)
    #
    currentDate()
    #
    filterSearch(urlNum)
    #
    webscrapTitlesList()
    # nin
    titlesListclean()
    # ojo
    webscrapBodyText()
    # ihih
    bodytextListSlim()
    # hihi
    injectToSheets()
    #
    #resultsToNotepad()
    urlNum = urlNum + 1
    time.sleep(5)
    
'''