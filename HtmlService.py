import webbrowser, os


class HtmlService( object ):
    
    def __init__( self ):
        
        self.browser = webbrowser
        self.htmlScript = None
        
        self.bodyHtml = []
        
        self.initHtmlScript()
        
    
    
    def initHtmlScript( self ):
        
        self.htmlScript = open( 'html/HighstreetInsight.html', 'w+' )
        self.htmlScript.write( "" )
        self.htmlScript.flush()
        
        
        
    def renderProducts( self, products ):
        
        startWrap = """ 
            <section id='productsWrap'>
                <ul id='productsList'>
        """
        productCards = "";
        
        for product in products:
            
            productCards += f"""
                <li>
                    <div class='productCardWraps'>
                        <div class='productCardImgWrap'>
                            <img src='{ product.getImgUrl() }' />
                        </div>
                        <div class='productCardTitleWrap'>
                            <h4 class='productCardTitle'>
                                { product.getDescription() }
                            </h4>
                            <h4 class='productCardPrice'>
                                £{ product.getPrice() }
                            </h4>
                            <h4 class='productCardColour'>
                                { product.getColour() }
                            </h4>
                        </div>
                    </div>
                </li>
            """
            
        endWrap = """ 
                </ul>
            <section>
        """
        
        productHtml = startWrap + productCards + endWrap
        
        self.bodyHtml.append( productHtml )
        
        
        
    def compileHtml( self ):
        
        bodyHtml = ""
        
        for body in self.bodyHtml:
             bodyHtml += body
        
        compiledHtml = self.getHeadHtml() + self.getHeaderHtml() + bodyHtml + self.getFooterHtml()
        
        self.writeAndRun( compiledHtml )
        
            
      
    def writeAndRun( self, compiledHtml ):
        
        self.htmlScript.write( compiledHtml )
        self.htmlScript.close()
        
        #self.browser.open_new_tab( 'html/HighstreetInsight.html' )file:///D:/data-science-projects/highstreet-insight-py/html/HighstreetInsight.html
        #self.browser.open( 'file:///D:/data-science-projects/highstreet-insight-py/html/HighstreetInsight.html' )
        #self.browser.get('windows-default').open('file://' + os.path.realpath('/html/HighstreetInsight.html'))
        
        
    
    def getHeadHtml( self ):
        
        return """
            <html>
                <head>
                    <title>HighStreet Insight</title>
                    <link rel='stylesheet' href='../css/HighstreetInsight.css'>
                    <script type='text/javascript' src='../js/HighstreetInsight.js'></script>
                </head>
            </html>
            <body>
        """
        
        
        
    def getHeaderHtml( self ):
        
        return """
                 <section id='header'>
                    <div id='headerMain'>
                        <h1>EMMYS APP</h1>
                        <h5>(WITH PIE CHARTS...)</h5>
                    </div>
                    <div id='headerMenuWrap'>
                        <ul id='headerMenu'>
                            <li onclick="switchView( 'products' )">
                                <h4>Products</h4>
                            </li>
                            <li>
                                <h4>Pie charts</h4>
                            </li>
                            <li>
                                <h4>Calander</h4>
                            </li>
                            <li>
                                <h4>Distribution</h4>
                            </li>
                        </ul>
                    </div>
                </section>
        """
        
        
        
    def getFooterHtml( self ):
        
         return """ 
                </ul>
            <section>
        """
        
        
        