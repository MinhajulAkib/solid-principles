class Connector:
    #abstraction layer
    
    def request(self, url, method):
        pass
        
class Xhtml(Connector):

    def request(self, url, method):
        pass
        
#new class added
class Mock(Connector):
    
    def request(self, url, method):
        pass
        
# high level module
class Http:

    def __init__(self, conn: Connector):
        self.conn = conn
        
    def post(self, url):
        self.conn.request(url, 'POST')
        
    def get(self, url):
        self.conn.request(url, 'GET')
