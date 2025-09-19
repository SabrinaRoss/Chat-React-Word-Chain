import pyautogui
import keyboard 
import time

#Note: When putting emotes needs space after each letter
class ScreenRelated:
    def __init__(self):
        self.size = pyautogui.size()
        self.current_mouse_pos = pyautogui.position()
        self.reaction_text_bar_pos = (0, 0)
        self.reaction_plus_icon_pos = (0, 0)
        self.message_text_bar_pos = (0, 0)
        self.is_reaction: bool = False #change this later to make a function to change it in tui

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
        y_offset: int = 40 # should really not be using magic numbers and instead should be like slowly incrementing clicks upwards until reach the new button locationm but for now it works
        lo_message = list(msg)
        first = True
        for i in lo_message:
            if i != ' ':

                new_message = ":regional_indicator_" + i
                self.type_letter_to_screen(new_message, first)
                pyautogui.press('enter')
                if first and self.is_reaction:
                    self.reaction_plus_icon_pos = (self.reaction_plus_icon_pos[0], self.reaction_plus_icon_pos[1] - y_offset)
                    first = False
                    time.sleep(.5)   
            else:
                if self.is_reaction:
                    # idk maybe do something with this later
                    pass
                else:
                    new_message = i # technically keeping it i is more efficient (slightly) but I want to keep a standardisation between the if statemetn
                    self.type_letter_to_screen(i)
                    pyautogui.press('enter')
        
    def type_letter_to_screen(self, msg, first: bool = False):
        if self.is_reaction:
            pyautogui.moveTo(self.reaction_plus_icon_pos)
            pyautogui.click()
            if first:
                pyautogui.click()
            time.sleep(.5)
            pyautogui.moveTo(self.reaction_text_bar_pos)
            pyautogui.click()
        else:
            pyautogui.moveTo(self.message_text_bar_pos)
            pyautogui.click()
        time.sleep(.5)
        pyautogui.write(msg, interval=.05)