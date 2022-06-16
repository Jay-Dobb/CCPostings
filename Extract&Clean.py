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


PATH = "C:\Tools\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get( 'https://yakima.craigslist.org/search/moxee-wa/jjj?query=%28remote+%7C+%22work+from+home%22%29+-%28%22%2421.25%22%29+-%28lawyer%29+-%28%22law+program%22%29+-%28cleaner%29+-%28hairdresser%29+-%28%22Free+Employment%22%29+-driver+-mother&lat=46.7221&lon=-120.1035&sort=date&search_distance=250')


#Scraping All Listings Information from site for current day
allTitleListings = []
allHyperlinksListings = []
allDatesListing = []
allLocationListing = []
allCityListing = []
fullBodyText = []

#Cleaned All Listings Info for current day
noDupTitleListings = []
noDupHyperlinksListings = []
noDupDatesListing = []
noDupLocationListing = []
noDupCityListing = []
slimBodyText =[]

combinedInfoListings = []


def datetext():
    today = date.today()
    print("Today's date:", today)
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

def LocationListings():
    #something something
    # scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost
    print("test")

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
    print(stopAtdate,": All Posting Items = ",eachitem)

def titlesListclean():
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
                print("new length of body letters: ", len(bodytext)) #finished while loop

        else:
            print("Length of body text less than ",amount)
            #bodytextListSlim().append(bodytext)

        #Ended while conditonal, so add slimmed body text
        slimBodyText.append(bodytext)

        print("HyperLink index:",index," ",noDupHyperlinksListings[index])

        #slice bodytext to preview output with skim
        skimBody = (slimBodyText[index])
        print("Bodytext Index:",index," ",skimBody[0:22])
        print("       ")

        index = index + 1

def bodytextATSfilterkeywords():
    #further filter with python manipulation
    print("test")

def resultsToNotepad():
    print("- - - - - - - - -")
    print("Packing Data Into Notepad...")

    index = 0

    with open('readme.txt', 'w') as f:
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

# Modifiers
# Filter craigslist wildcards
# Prematurely stop scrap at list
# Date To Stop scrap(Current Date)
# Reduce Body text posting amount

#'https://yakima.craigslist.org/search/moxee-wa/jjj?query=%28remote+%7C+%22work+from+home%22%29+-%28%22%2421.25%22%29+-%28lawyer%29+-%28%22law+program%22%29+-%28cleaner%29+-%28hairdresser%29+-%28%22Free+Employment%22%29+-driver+-mother&lat=46.7221&lon=-120.1035&sort=date&search_distance=250"
#TO DO NEXT


# Manipulate GoogleSheets
# scrap by categories grouped
# scrap from Timezone/County/Radius Cordninates on all of West Coast | then Mid Cost




craigslistSearchFilter = "... "
stopAtdate = datetext()
stopscrapAtList = 6
shortenBodyTextLettersTo = 1900



webscrapTitlesList()

titlesListclean()

webscrapBodyText()

bodytextListSlim()

resultsToNotepad()
