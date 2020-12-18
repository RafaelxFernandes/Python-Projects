import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["Yes", "Affirmative", "Sure", "Do it!", "Yeah!", "Confirm"]
        self.cancel = ["No", "Negative", "Don't", "Cancel"]

    
    def discover(self, text):
        if("what" in text and "name" in text):
            if("my" in text):
                self.respond("You haven't told my your name yet...")
            else:
                self.respond("My name is Python Commander. How are you?")

        if("launch" in text or "open" in text):
            app = text.split(" ", 1)[-1]
            self.respond("Opening " + app + "...")
            os.system(app)


    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)