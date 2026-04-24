# give the random jokes by module
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# import a module to voice command what will you text it is speak a your text
import pyttsx3
engine = pyttsx3.init()
engine.say("hello , samarth how can i help you?")
engine.say(joke)
engine.runAndWait()

