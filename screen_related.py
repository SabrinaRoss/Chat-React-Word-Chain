import pyautogui
import keyboard 
import time
from enum import Enum

class Software(Enum): # this enum class could likely be in a diffrent file
    DISCORD = 1
    SLACK = 2

#Note: When putting emotes needs space after each letter
class ScreenRelated:
    def __init__(self):
        self.size = pyautogui.size()
        self.current_mouse_pos = pyautogui.position()
        self.reaction_text_bar_pos = (0, 0)
        self.reaction_plus_icon_pos = (0, 0)
        self.message_text_bar_pos = (0, 0)
        self.is_reaction: bool = False #change this later to make a function to change it in tui
        self.software = Software(Software.DISCORD)

    def grab_software_using(self):
        print("What Software are you going to use this program on?")
        for software in Software:
            print(f'Application: {software.name}, pleases type {software.value} to use')
        temp = input("\nType your desired software here: ")
        print(Software.__members__.values())
        if temp.isdigit():
            temp = int(temp)
            if temp in [s.value for s in Software]:
                self.software = Software(temp)
                print(f'You selected: {self.software}')
            print(temp)
            return 
        self.grab_software_using() # yes I am aware this could stack overflow

    def grab_reaction_text_bar_pos(self):
        print("Press shift over the Reaction Text Bar to grab it's location on the screen")
        keyboard.wait('shift')
        self.reaction_text_bar_pos = pyautogui.position()
    
    def grab_reaction_plus_icon_pos(self):
        print("Press shift over the Reaction Plus Icon to grab it's location on the screen")
        keyboard.wait('shift')
        self.reaction_plus_icon_pos = pyautogui.position()
    
    def grab_message_text_bar_pos(self):
        print("Press shift over the Message Text Bar to grab it's location on the screen")
        keyboard.wait('shift')
        self.message_text_bar_pos = pyautogui.position()

    def type_sentence_to_screen(self, msg):
        y_offset: int = 42 # should really not be using magic numbers and instead should be like slowly incrementing clicks upwards until reach the new button locationm but for now it works
        lo_message = list(msg)
        first = True
        for i in lo_message:
            if i != ' ':
                new_message = ""
                match(self.software):
                    case Software.DISCORD:
                        new_message = ":regional_indicator_" + i
                    case Software.SLACK:
                        new_message = ":alphabet-white-" + i

                self.type_letter_to_screen(new_message, first)
                pyautogui.press('enter')
                if first and self.is_reaction:
                    self.reaction_plus_icon_pos = (self.reaction_plus_icon_pos[0], self.reaction_plus_icon_pos[1] - y_offset)
                    first = False
                    time.sleep(.5)   
            else:
                print(self.is_reaction)
                if self.is_reaction:
                    # idk maybe do something with this later
                    pass
                else:
                    new_message = i # technically keeping it i is more efficient (slightly) but I want to keep a standardisation between the if statemetn
                    self.type_letter_to_screen(new_message)
                    pyautogui.keyDown('shift')
                    pyautogui.press('enter')
                    pyautogui.keyUp('shift')
        if not self.is_reaction:
            pyautogui.press('enter')
        
    def type_letter_to_screen(self, msg, first: bool = False):
        if self.is_reaction:
            pyautogui.moveTo(self.reaction_plus_icon_pos)
            time.sleep(.75)
            pyautogui.click()
            if first and self.software == Software.DISCORD:
                pyautogui.click()
            time.sleep(.5)
            if self.software == Software.DISCORD:
                pyautogui.moveTo(self.reaction_text_bar_pos)
                pyautogui.click()   
        else:
            pyautogui.moveTo(self.message_text_bar_pos)
            pyautogui.click()
        time.sleep(.5)
        pyautogui.write(msg, interval=0)
