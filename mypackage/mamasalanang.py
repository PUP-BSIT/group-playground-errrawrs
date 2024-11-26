import pyfiglet

def ascii_art_text(text):
    # Generate ASCII art from the input text
    ascii_art = pyfiglet.figlet_format(text)
    
    # Print the ASCII art
    print(ascii_art)

# Example usage
ascii_art_text(input("Enter a Word: ")) 
