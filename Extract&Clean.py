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

PATH = Service("C:\Tools\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)




gc = gspread.service_account(filename='mycredentials.json')

#Craigslist URLS
craiglistURLS = []


#Scraping All Listings Information from site for current day
allTitleListings = []
allHyperlinksListings = []
allDatesListing = []
#allLocationListing = [] #not yet used
allCityListing = []
fullBodyText = []

#Cleaned All Listings Info for current day
noDupTitleListings = []
noDupHyperlinksListings = []
noDupDatesListing = []
#noDupLocationListing = [] #not yet used
noDupCityListing = []
occurenceList = []
slimBodyText = []

combinedInfoListings = []
#### Defined Lists


def currentDate():

    today = date.today()
    print(" ")
    print("Today's date:", today)

    if stopAtdate == 'Today':

        d4 = today.strftime("%b-%d")
        dayint = int(d4[4:6])          # converting number in date into Int from strong
        d5 = d4

        if debugPrints == True:
            print(' ')
            print('----- currentDate() ------')
            print("d4 =", d4)
            print("day number ", dayint)
            print("day number type", type(dayint))

        if dayint > 9:                 #If the Date day is greater that 9 (double digits, format for double digits)

            d5 = d4[:3] + " " + d4[4:6]

            if debugPrints == True:
                print("d5 = ", d5)
                print("Scraping List from** D5: ", d5)
                print("----- currentDate() ------")
                print(" ")

        return d5
    else:
        print("Scraping List from**: ", stopAtdate)
        print("----- currentDate() ------")
        print(" ")
        return stopAtdate

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

    #WestCoast North Cali/Nev/Oregan
    craiglistURLS.append('https://susanville.craigslist.org/search/ravendale-ca/jjj?lat=40.8302&lon=-119.899&sort=date&search_distance=250')

    #WestCoast SouthCali
    craiglistURLS.append('https://visalia.craigslist.org/search/porterville-ca/jjj?lat=36.0537&lon=-119.0514&search_distance=250&sort=date')

    #Mid South Nevada/Phonix
    craiglistURLS.append('https://showlow.craigslist.org/search/heber-az/jjj?lat=34.6079&lon=-110.6193&search_distance=250&sort=date')

    #mid South Texas
    craiglistURLS.append('https://lubbock.craigslist.org/search/maple-tx/jjj?lat=34.0017&lon=-103.0086&search_distance=250&sort=date')

    # mid mid texas
    craiglistURLS.append('https://waco.craigslist.org/search/clifton-tx/jjj?lat=31.8017&lon=-97.557&search_distance=250&sort=date')

    # mid mid Colorado
    craiglistURLS.append('https://denver.craigslist.org/search/byers-co/jjj?lat=39.8246&lon=-103.9639&search_distance=250&sort=date')

    # north mid idaho
    craiglistURLS.append('https://eastidaho.craigslist.org/search/blackfoot-id/jjj?lat=43.4539&lon=-112.5305&search_distance=250&sort=date')
    # North mid Montana
    craiglistURLS.append('https://billings.craigslist.org/search/pompeys-pillar-mt/jjj?lat=45.9053&lon=-107.71&search_distance=250&sort=date')

    #north mid North dakatoa/ SD
    craiglistURLS.append('https://bismarck.craigslist.org/search/strasburg-nd/jjj?lat=46.1148&lon=-100.3369&search_distance=250&sort=date')

    #midwest Minnsota/wisconsin/Chicago
    craiglistURLS.append('https://lacrosse.craigslist.org/search/houston-mn/jjj?lat=43.7754&lon=-91.5472&sort=date&search_distance=250')

    # Mid Mid Utah
    craiglistURLS.append('https://provo.craigslist.org/search/duchesne-ut/jjj?lat=39.9005&lon=-110.5223&search_distance=230&sort=date&sort=date')


def locationListings():
    #something something
    # scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost
    pass

def filterSearch(urlNum):

    if partFull == 'p':
        driver.get(craiglistURLS[urlNum] + '&employment_type=2&employment_type=3&employment_type=4')
    else:
        driver.get(craiglistURLS[urlNum])

    searchbox = driver.find_element(By.CSS_SELECTOR, '.querybox')
    # searchField = searchbox.find_element(By.TAG_NAME, 'input').get_attribute('value')
    inputbox = searchbox.find_element(By.NAME, 'query')
    inputbox.send_keys(craigslistSearchFilter)
    inputbox.send_keys(Keys.RETURN)

    if debugPrints == True:
        print('----- filterSearch() ------')
        print("filtersearch url", urlNum)
        print("what is currently in searchbox")
        print('----- filterSearch() ------')
        print(' ')

def webscrapTitlesList():

    dateStop = currentDate()

    if debugPrints == True: print("----webscrapTitleslist()----")

    results = driver.find_elements(By.CLASS_NAME, 'result-row')
    webEle = results[0].find_element(By.CSS_SELECTOR, '.result-info')
    location = results[0].find_element(By.CSS_SELECTOR, '.result-meta')


    eachitem = 0
    for x in results:

        webEle = results[eachitem].find_element(By.CSS_SELECTOR, '.result-info')

        #DATE OF LISTING
        dateListing = unidecode(webEle.find_element(By.TAG_NAME, 'time').text) #  TAG NAME IS at end time>
        if debugPrints == True: print("Date of post ", eachitem, ": ", dateListing)

        #TITLE POSTING NAME
        #<a  ***  href= *** "https://charleston.c.html" data-id="7492752531"  id="postid_7492752531"> the title to see here *** </a> **
        titleListing =(unidecode(webEle.find_element(By.TAG_NAME, 'a').text))
        if debugPrints == True: print("Title of post ", eachitem, ": ", titleListing)

        #HYPERLINK
        # within <a/> find attritube href (hyperlink)
        hyperLinkitem = webEle.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if debugPrints == True: print("Hyperlink of post ", eachitem, ": ", hyperLinkitem)

        #CITY
        #<span class="result-meta">
        # <span class="nearby" title="vancouver, BC">(van &gt; Downtown Vancouver) *** </span> ***
        location = results[eachitem].find_element(By.CSS_SELECTOR, '.result-meta')
        cityListing = unidecode(location.find_element(By.TAG_NAME, 'span').text)
        if debugPrints == True: print("CityLoc of post ", eachitem, ": ", cityListing)

        #adding to lists
        allTitleListings.append(str(titleListing))
        allHyperlinksListings.append(hyperLinkitem)
        allDatesListing.append(dateListing)
        allCityListing.append(cityListing)

        eachitem = eachitem + 1

        if debugPrints == True:
            print("----webscrapTitleslist()----")
            print(" ")

        if stopAtdate != "all":              #STOPS EXTRACTING LIST AT TODAYS DATE
            if (unidecode(webEle.find_element(By.TAG_NAME, 'time').text)) != dateStop:
                print("Grabbing Dates:", dateStop)
                print(" ")
                break

    driver.quit()
    print(stopAtdate, ": All Posting Items = ", eachitem)

def titlesListclean():

    okeywords = ['CHEFS', 'DISHWASHERS', 'Tutoring', 'Tutor', 'In-Home Care', 'Surrogate','Cashier'
                'BROKERS', 'Mother','carpenter','Taxi','Real Estate Agent','Freelance Writer','Property Management']


    # Removes Duplicate names in main list and aligns list index for each other list and adds only non duplicates to new list
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

    filtered_titles = [f'{m}' for i, (t, m) in enumerate(zip(allHyperlinksListings, allTitleListings)) if not any(w in m for w in okeywords)]

    for m in filtered_titles:
        print(m)

    for words in okeywords:
        occurences = sum(x.count(words) for x in allTitleListings)
        if occurences > 0:
            occurenceAmt = sum(x.count(words) for x in allTitleListings)
            occurenceDetails = str(occurenceAmt) + ' Occurences For:' + words
            occurenceList.append(occurenceDetails)

    occurenceList.sort(reverse=True)
    for item in occurenceList:
        print(item)


    print("\n----- Scraping & Formatting (Stops at ",stopscrapAtList,")... ----- \n ")

def webscrapBodyText(stopscrapAtList):

    PATH = Service("C:\Tools\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH)

    index = 0

    #---- Determines to use all string for all listing to convert the input number from str to Int
    if stopscrapAtList == 'all':
        print("ALL")
    else:
        stopscrapAtList = int(stopscrapAtList)
    #----

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

        try:
            body = driver.find_element(By.CSS_SELECTOR, '.userbody')
            bodytext = unidecode(body.find_element(By.TAG_NAME, 'section').text)
            # Adding to Body List
            fullBodyText.append(bodytext)

            # Preview skim body prints with index of other lists
            skimBody = (fullBodyText[index])
        except:
            print("body not found on index: ",index)
            pass


        print(" index Title:",index,"- ", noDupTitleListings[index],noDupHyperlinksListings[index] , " | Sample Body text: ", skimBody[0:20])

        index = index + 1
        if index == stopscrapAtList:
            driver.quit()
            print("----- webscrapBodyText() -----")
            print(" ")
            break
        else:
            stopscrapAtList == 'all'
            continue


def bodytextATSfilterkeywords():

    #if these keywords are contained with the body text remove from each list the index
    keywords = ['live in','live-in', 'property management', 'maintaining property', 'paint', 'painting','Clean laundry','prospective tenants'
                'civil engineering', 'remote and onsite','We encourage applicants of all ages','commission brokerage','cashier duties'
                'we encourage applicants of all ages', 'This is not a remote position','NOT A WORK FROM HOME','this is not a remote position','Store Clerk','Real Estate Investor'
                'degree in civil engineering ' ,'surrogate mother','Transportation ','surrogate','drives','Pathrise','some in-person',"job is not remote"
                 "We're selective, and only work with motivated candidates who are serious about leveling up their careers.","unit complex",'cents per word']

    for words in keywords:
        occurences = sum(x.count(words) for x in fullBodyText)
        if occurences > 0:
            occurenceAmt = sum(x.count(words) for x in fullBodyText)
            occurenceDetails = str(occurenceAmt) + ' Occurences For:' + words
            occurenceList.append(occurenceDetails)

    occurenceList.sort(reverse=True)
    for item in occurenceList:
        print(item)

    wordsFound = 0
    for text in fullBodyText:
        for xs in keywords:
            if xs in text:
                itemlist = (fullBodyText.index(text))
                skimTitle = noDupTitleListings[itemlist]
                wordsFound = wordsFound + 1
                print("index: ", itemlist,' | ', skimTitle[0:45], " | Word Found: ", xs)

    filtered_titles = [f'{t}' for i, (t, m) in enumerate(zip(noDupTitleListings, fullBodyText)) if not any(w in m for w in keywords)]
    filtered_bodytext = [f'{m}' for i, (t, m) in enumerate(zip(noDupTitleListings, fullBodyText)) if not any(w in m for w in keywords)]

    print("\n Total Words Found: ",wordsFound)
    print("Postings = ", len(combinedInfoListings))
    print('Postings After Filtering',len(filtered_titles),  '\n')

    for items in filtered_titles:
        itemindex = filtered_titles.index(items)
        print("index:",itemindex," ",items)


def bodytextListSlim():

    index = 0
    amount = shortenBodyTextLettersTo   #slim down body of text below 1900 characters. removing between string [ :X-400 and X-200: ]
    print("[Output]:")
    for bodytext in fullBodyText:
        if debugPrints == True: print("Grabbing Body Text from: Index", index, " ", noDupTitleListings[index])
        if debugPrints == True: print("length of body text letters: ", len(bodytext))
        #if debugPrints == True: print(bodytext)  #prints full body

        if len(bodytext) > amount:
            while len(bodytext) > amount:
                bodytext = bodytext[0:len(bodytext)-400] + bodytext[len(bodytext)-200:]
                if debugPrints == True: print("new length of body each time", len(bodytext))
            else:
                if debugPrints == True: print("new length of body letters: ", len(bodytext)) #finished while loop
                pass

        else:
            if debugPrints == True: print("Length of body text less than ",amount)
            #bodytextListSlim().append(bodytext)
            pass


        slimBodyText.append(bodytext)            #Ended while conditonal, so add slimmed body text
        skimBody = (slimBodyText[index])             #slice bodytext to preview output with skim

        if debugPrints == True:
            print("HyperLink index:",index," ",noDupHyperlinksListings[index])
            print("Bodytext Index:",index," ",skimBody[0:22],"\n")

        index = index + 1

def injectToListingsSheets():
    print(" ")

    scope=   ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    credentials=ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
    gc=gspread.authorize(credentials)
    wks=gc.open('Sele').sheet1

    cListing = 0

    #Slices all strings in hyperlink list to remove https://
    stripHyperlinksListing = [w[8:] for w in noDupHyperlinksListings]

    for items in slimBodyText:

        wks.append_row([noDupDatesListing[cListing], stripHyperlinksListing[cListing], noDupTitleListings[cListing], noDupCityListing[cListing]])
        #[gColDate,gColLocation,gColTitle,gColHyperComment,created_on,updated_on] google sheet field    #names.
        print("Index ", cListing, " Inserted Successfully ! Title:", noDupTitleListings[cListing])
        cListing = cListing + 1

    cella1 = wks.get_values("A1")
    print(cella1)

def injectBodyCommentsToSheet():

    PATH = Service("C:\Tools\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH)

    driver.get('https://docs.google.com/spreadsheets/d/14Ns_4P9OVNf_Z2pzQ2KVrdzzmjmip9etf2-zZHJmdOw/edit?usp=sharing')

    combine_keys = ActionChains(driver)
    actions = ActionChains(driver)

    time.sleep(1)
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(1)

    bodylisting = 0
    for listings in slimBodyText:
        actions.send_keys(Keys.ARROW_DOWN).perform()
        combine_keys.key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("m").key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
        actions.send_keys(slimBodyText[bodylisting])
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER).perform()
        bodylisting = bodylisting + 1

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

###----------------------------------------------
#TO DO NEXT
# Manipulate GoogleSheets
# scrap by categories grouped
# scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost


### Modifiers

# Debugprints - Prints out every step
# craigslistsearchfilter - Filter craigslist wildcards
# shortenbodytextlettersto - Reduce Body text posting amount
# stopscrapatlist - Prematurely stop scrap at list
# stopAtDate - Date To Stop scrap put in Today or the previous Date



debugPrints = False
craigslistSearchFilter = '(remote | "work from home") -(lawyer) -("performed in person") -("level up your") -license -driver -mergers -HVAC -housekeeper'
shortenBodyTextLettersTo = 1900
stopAtdate = "Jul 11"

init = input("Run Single function (S) or Full Program (F) (Use s or f): ")
stopscrapAtList = input("How many listings to pull (or type 'all'): ")
urlNum = int(input("Craigslist location 1 - Van/Sea, 2 - Oregan/Sea, 3 -Cali: "))
partFull = input("Partime (p) or fulltime (f)? ")

if init == 's':
    injectBodyCommentsToSheet()

elif init == 'f':
    # make this in new py file so it doesnt over load memory?
    injectCraigslistURLS()

#print("In Url list Index", urlNum)
#
#
filterSearch(urlNum)
#
webscrapTitlesList()
# nin
titlesListclean()
# ojo
print("print outside",noDupTitleListings)
#webscrapBodyText(stopscrapAtList)
# ihih
#bodytextATSfilterkeywords()

#bodytextListSlim()
# hihi
#injectToListingsSheets()
#
#injectBodyCommentsToSheet()
# resultsToNotepad()
# urlNum = urlNum + 1
# time.sleep(5)


