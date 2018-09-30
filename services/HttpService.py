import requests
import json
from models.ProductModel import ProductModel


class HttpService( object ):
    
    def __init__( self ):
        
        self.productModel = ProductModel
        self.headers = {}
        
        
    def authorise( self, email, password ):
        
        login = {
            'email': email,
            'password': password      
        }
        
        response = requests.post( 'http://fronttableinsight.co.uk/api/v1.0/authorise', json=login ).json()
        
        if response[ 'tokenData' ] != False:
            self.headers[ 'Authorization' ] = 'Bearer ' + response[ 'tokenData' ][ 'token' ]
            return True
        else:
            return False
        
    
    def getAsosProducts( self, startDate, endDate ):
        
        dateRange = {
            'startDate': startDate,
            'endDate': endDate      
        }
        
        self.headers[ 'datainsight' ] = json.dumps( dateRange );
        
        response = requests.get( 'http://fronttableinsight.co.uk/api/v1.0/asos_products', headers=self.headers ).json()
        
        if response[ 'modelData' ] != False:
            modelData = []
            
            for model in response[ 'modelData' ]:
                modelData.append( self.productModel( model ) )
        else: 
            return False
                
        return modelData