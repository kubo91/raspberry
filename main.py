import couchquery
import socket
import cherrypy

cherrypy.server.socket_host='0.0.0.0'
db = couchquery.Database('http://192.168.1.21:5984/pir')
class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		return """<html>
			<body>
			<FORM>
			<INPUT Type="BUTTON" VALUE="Turn on" ONCLICK="window.location.href='http://192.168.1.21:8080/turnon'"> 
			</FORM>
			
			<FORM>
                        <INPUT Type="BUTTON" VALUE="Turn off" ONCLICK="window.location.href='http://192.168.1.21:8080/turnoff'"$
                        </FORM>

			</body>
			</html>"""

	@cherrypy.expose
	def turnon(self):
		ip = socket.gethostbyname(socket.gethostname())
 		#cherrypy.response.headers['Location'] = 60
                doc=db.get('Light')
		doc.Turn_on=1
		db.update(doc) 


		return """<html> <head> <meta http-equiv="refresh" content="0; url=http://192.168.1.21:8080/" /> </head></html>"""


        @cherrypy.expose
	def turnoff(self):
                ip = socket.gethostbyname(socket.gethostname())
                #cherrypy.response.headers['Location'] = 60
                doc=db.get('Light')
                doc.Turn_on=0
                db.update(doc)


                return """<html> <head> <meta http-equiv="refresh" content="0; url=http://192.168.1.21:8080/" /> </head></html>"""


if __name__ == '__main__':
	cherrypy.quickstart(HelloWorld())

