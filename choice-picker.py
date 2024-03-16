import tkinter as tk
import random
import tkinter.simpledialog
import os
import json
import tkinter.messagebox

OPTIONS_FILE = 'options.json'


class RestaurantApp:
    def __init__(self):

        # Load options from file if it exists
        try:
            if os.path.exists(OPTIONS_FILE):
                with open(OPTIONS_FILE, 'r') as f:
                    self.options = json.load(f)
            else:
                self.options = []
        except Exception as e:
            tkinter.messagebox.showerror(
                "Error", f"Failed to load options from file: {e}")
            self.options = []

        self.root = tk.Tk()
        self.root.title("Choice Picker App")

        # Set the window size
        window_width = 300
        window_height = 300

        # Get the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set up the window size and position
        self.root.geometry(
            f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create and pack the label, listbox, and buttons
        self.option_label = tk.Label(self.root, text="Options:")
        self.option_label.pack()

        self.option_listbox = tk.Listbox(self.root)
        self.option_listbox.pack()

        self.add_button = tk.Button(
            self.root, text="Add Option", command=self.add_option)
        self.add_button.pack()

        self.pick_button = tk.Button(
            self.root, text="Pick Option", command=self.pick_option)
        self.pick_button.pack()

        self.remove_button = tk.Button(
            self.root, text="Remove Option", command=self.remove_option)
        self.remove_button.pack()

        # Add options to option_listbox
        for option, weight in self.options:
            self.option_listbox.insert(tk.END, f"{option} (Weight: {weight})")

    def add_option(self):
        option = tkinter.simpledialog.askstring(
            "Input", "Enter an option:", parent=self.root)
        weight = tkinter.simpledialog.askinteger(
            "Input", "Enter the weight for the option (single digit):", parent=self.root)

        # Check if the option is not empty and is not already in the list of options
        if not option or any(option == existing_option for existing_option, _ in self.options):
            tkinter.messagebox.showerror(
                "Invalid input", "Option must be a non-empty string that is not already in the list.")
            return

        # Check if the weight is a single digit integer
        if weight is None or weight < 0 or weight > 9:
            tkinter.messagebox.showerror(
                "Invalid input", "Weight must be a single digit integer.")
            return

        self.options.append((option, weight))
        self.option_listbox.insert(tk.END, f"{option} (Weight: {weight})")

        self.save_options()

    def remove_option(self):
        # Get the index of the selected option
        selected = self.option_listbox.curselection()

        # If an option is selected
        if selected:
            # Remove the option from the listbox and the options list
            self.option_listbox.delete(selected)
            del self.options[selected[0]]

            self.save_options()

    def pick_option(self):
        if self.options:
            option = random.choices(
                [option for option, weight in self.options],
                weights=[weight for option, weight in self.options],
                k=1
            )[0]
            tkinter.messagebox.showinfo(
                "Result", f"You should go to: {option}")
        self.save_options()

    def run(self):
        self.root.mainloop()

    def save_options(self):
        # Save options to file
        try:
            with open(OPTIONS_FILE, 'w') as f:
                json.dump(self.options, f)
        except Exception as e:
            tkinter.messagebox.showerror(
                "Error", f"Failed to save options to file: {e}")


if __name__ == "__main__":
    app = RestaurantApp()
    app.run()
