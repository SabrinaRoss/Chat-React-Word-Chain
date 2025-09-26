from screen_related import ScreenRelated, Software

def main():
    screen = ScreenRelated()
    
    screen.grab_software_using()
    screen.grab_message_text_bar_pos()
    screen.grab_reaction_plus_icon_pos()
    screen.grab_reaction_text_bar_pos()
    
    is_reaction = input("You you want to message the text or react the message? (1 for message, 2 for reaction): \n")
    if is_reaction == '2':
        screen.is_reaction = True
    else: 
        screen.is_reaction = False
    
    message = input("Enter the message that you want to reaction blast to the message, note: do not repeat letters: \n")
    
    screen.type_sentence_to_screen(message)

if __name__ == "__main__":
    main()