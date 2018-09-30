

class ProductModel( object ):
    
    def __init__( self, product ):
        self.webSite = product[ 'webSite' ]
        self.description = product[ 'description' ]
        self.price = product[ 'price' ]
        self.colour = product[ 'colour' ]
        self.imgUrl = product[ 'imgUrl' ]
        self.createdDate = product[ 'createdDate' ]
        
    def getWebSite( self ):
        return self.webSite
    
    def getDescription( self ):
        return self.description
    
    def getPrice( self ):
        return self.price
    
    def getColour( self ):
        return self.colour
    
    def getImgUrl( self ):
        return self.imgUrl
    
    def getCreatedDate( self ):
        return self.createdDate