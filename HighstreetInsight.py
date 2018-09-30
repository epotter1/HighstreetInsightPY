

from services.HttpService import HttpService
from services.HtmlService import HtmlService
  
    
class HighstreetInsight( object ):
    
    def __init__( self ):
        
        self.httpService = HttpService()
        self.htmlService = HtmlService()
        
        self.beginApp()
        
    
    def beginApp( self ):
        
        if not self.loginToFrontTableInsightsAPI():
            print( "Login attempt was unsuccessful. " )
            return
        else: 
            print( "Login attempt was successful. " )
            self.getfrontTableInsightsProducts()
            
        
    def loginToFrontTableInsightsAPI( self ):
        
        return self.httpService.authorise( email='t.potter@teapotmedia-webdesign.co.uk', password='tpotter22' )
    
    
    def getfrontTableInsightsProducts( self ):
        
        products = self.httpService.getAsosProducts( startDate='2018-09-28 00:00:00', endDate='2018-09-29 11:00:00' )
        
        if products != False:
            print( "Asos product retrieval was successful. " )
            self.htmlService.renderProducts( products )
            self.htmlService.compileHtml()
        else:
            print( "Asos product retrieval was unsuccessful. " )
        
        
        
HighstreetInsight = HighstreetInsight()
        