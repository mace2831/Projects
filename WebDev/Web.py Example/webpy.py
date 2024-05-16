import web

#define routes web.py will respond to
routes = (
    "/(.*)", "home"
)

#create app object, providing routes and globals as arguments
app = web.application(routes, globals())

#define the home class which will respond to our default route
class home:
    
    #method to respond to GET requests
    def GET(self, name):
        
        #tell the browser we are sending html 
        web.header("Content-Type", "text/html")
        #set name to world if name not set
        if not name:
            name = "World"
        #return string to display in browser
        return "<h1>Hello, " + name + "!</h1>"
    
#make sure we're in the main program scope, then run!
if __name__ == "__main__":
    app.run()