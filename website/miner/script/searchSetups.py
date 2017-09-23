import time
from ..models import Filter, Result

class LaserSearch:

    matchingLaserLinks = []

    def __init__(self, minLaserPower, maxLaserPrice):
        # (These arguments will be different for each 'SearchType' class)
        self.minLaserPower = minLaserPower
        self.maxLaserPrice = maxLaserPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

    def setResultsTimeLeft(self, resultsTimeLeft):
        self.resultsTimeLeft = resultsTimeLeft

    def setResultsTitles(self, resultsTitles): # Acquire lower case titles.
        self.resultsTitles = resultsTitles

    def setResultsPrices(self, resultsPrices): # Acquire prices as floats
        self.resultsPrices = resultsPrices

    def setResultsURLs(self, resultsURLs): # Acquire URLs
        self.resultsURLs = resultsURLs

    def setResultsImageURLs(self, resultsImageURLs): # Acquire URLs
        self.resultsImageURLs = resultsImageURLs

    def getTotalMatchesFound(self):
        return self.totalMatchesFound

    def getMatchingLinks(self):
        return self.matchingLaserLinks

    def itemFound(self, currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        self.totalMatchesFound += 1
        self.matchingLaserLinks.append(currentUrl)
        result = Result()
        result.filter = Filter.objects.get(pk=5)
        result.result_title = currentTitle
        result.result_url = currentUrl
        result.result_image_url = currentImageURL
        result.date_found = time.time()
        result.price = currentPriceAsFloat
        result.is_favorite = False
        result.save()
        print("found - adding to Database")

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTimeLeft = self.resultsTimeLeft[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = self.resultsPrices[i]
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]


            # TODO: Find out if it is possible to make this in GUI style.
            # i.e. add keywords and a numerical range check with a word in front or behind...???
            keyword6 = " metal cutter "

            for power in range(2000):
                keyword1 = " " + str(power + self.minLaserPower) + "w "
                keyword2 = " " + str(power + self.minLaserPower) + " w "
                keyword3 = " " + str(power + self.minLaserPower) + "kw "
                keyword4 = " " + str(power + self.minLaserPower) + " kw "
                keyword5 = " saw " # used to ignore titles with 'saw'

                if (currentTitleLC.count(keyword1) > 0 or currentTitleLC.count(keyword2) > 0 \
                        or currentTitleLC.count(keyword3) > 0 or currentTitleLC.count(keyword4) > 0) \
                    and currentPriceAsFloat < self.maxLaserPrice and currentTitleLC.count(keyword5) == 0:
                    self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)
                    break
                elif currentTitleLC.count(keyword6) > 0:
                    if currentPriceAsFloat <= self.maxLaserPrice:
                        self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)




