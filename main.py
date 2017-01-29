import webapp2
import caesar
import cgi

def build_page(textarea_content):
    rot_label = "<label>Rotation number: </label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    msg_label = "<label>Type a message: </label>"
    textarea2 = "<input type='number' name='rotation'/>"
    submit = "<input type='submit'/>"
    form = ("<form method='post'>"
            + rot_label + textarea2 + "<br>"
            + msg_label + textarea +
            "<br>" + submit + "</form>")
    header = "<h2>Web caesar</h2>"
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_msg = cgi.escape(encrypted_message)
        content = build_page(escaped_msg)
        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
