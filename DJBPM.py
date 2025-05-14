import tkinter as tk
from tkinter import ttk, messagebox

class DJBPM:
    def __init__(self, root):
        self.root = root
        self.root.title("DJBPM 3/4 Loop Tool - juliana!")
        self.root.resizable(True, True)

        # Make column 0 stretch, and row 2 (history) stretch
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        self.history = []

        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # Input Section
        self.input_frame = ttk.LabelFrame(self.root, text="Known BPM")
        self.input_entry = ttk.Entry(self.input_frame, font=('Arial', 12))
        self.calculate_btn = ttk.Button(
            self.input_frame,
            text="Calculate",
            command=self.calculate,
            style='Large.TButton'
        )

        # Results Section
        self.results_frame = ttk.LabelFrame(self.root, text="Adjusted BPMs")
        self.slow_bpm_var = tk.StringVar()
        self.fast_bpm_var = tk.StringVar()
        self.slow_label = ttk.Label(
            self.results_frame,
            text="Start/Loop BPM:",
            font=('Arial', 10, 'bold')
        )
        self.slow_display = ttk.Label(
            self.results_frame,
            textvariable=self.slow_bpm_var,
            font=('Arial', 12, 'bold'),
            foreground='blue'
        )
        self.fast_label = ttk.Label(
            self.results_frame,
            text="End BPM:",
            font=('Arial', 10, 'bold')
        )
        self.fast_display = ttk.Label(
            self.results_frame,
            textvariable=self.fast_bpm_var,
            font=('Arial', 12, 'bold'),
            foreground='green'
        )

        # History Section
        self.history_frame = ttk.LabelFrame(self.root, text="History")

        # Listbox without fixed height so it fills the frame
        self.history_list = tk.Listbox(
            self.history_frame,
            font=('Arial', 9),
            activestyle='none'
        )

        # Always-visible scrollbar; it'll only be active once needed
        self.scrollbar = ttk.Scrollbar(
            self.history_frame,
            orient='vertical',
            command=self.history_list.yview
        )
        self.history_list.config(yscrollcommand=self.scrollbar.set)

        # Clear button
        self.clear_btn = ttk.Button(
            self.root,
            text="Clear All",
            command=self.clear_input,
            style='Large.TButton'
        )

    def setup_layout(self):
        # Input Frame (row 0)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.input_frame.columnconfigure(0, weight=1)
        self.input_entry.grid(row=0, column=0, padx=5, pady=2, sticky='ew')
        self.calculate_btn.grid(row=0, column=1, padx=5, pady=2)

        # Results Frame (row 1)
        self.results_frame.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        self.results_frame.columnconfigure(1, weight=1)
        self.slow_label.grid(row=0, column=0, sticky='w', padx=5)
        self.slow_display.grid(row=0, column=1, padx=5, pady=2, sticky='ew')
        self.fast_label.grid(row=1, column=0, sticky='w', padx=5)
        self.fast_display.grid(row=1, column=1, padx=5, pady=2, sticky='ew')

        # History Frame (row 2)
        self.history_frame.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')
        self.history_frame.columnconfigure(0, weight=1)
        self.history_frame.rowconfigure(0, weight=1)

        self.history_list.grid(row=0, column=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Clear Button (row 3), centered horizontally
        self.clear_btn.grid(row=3, column=0, sticky='ew', pady=10, padx=10)

    def calculate(self):
        try:
            original_bpm = float(self.input_entry.get())
            if original_bpm <= 0:
                raise ValueError("BPM must be positive")

            slow_bpm = original_bpm * 0.75
            fast_bpm = original_bpm / 0.75

            self.slow_bpm_var.set(f"{slow_bpm:.2f}")
            self.fast_bpm_var.set(f"{fast_bpm:.2f}")

            history_entry = (
                f"Known: {original_bpm:.2f} | "
                f"Start/Loop: {slow_bpm:.2f} | "
                f"End: {fast_bpm:.2f}"
            )
            self.update_history(history_entry)

        except ValueError as e:
            messagebox.showerror(
                "Input Error",
                str(e) if str(e) else "Please enter a valid positive number"
            )
            self.input_entry.focus()

    def update_history(self, entry):
        self.history.insert(0, entry)
        if len(self.history) > 20:   # allow more items so scrolling can trigger
            self.history.pop()
        self.history_list.delete(0, tk.END)
        for item in self.history:
            self.history_list.insert(tk.END, item)

    def clear_input(self):
        self.input_entry.delete(0, tk.END)
        self.slow_bpm_var.set('')
        self.fast_bpm_var.set('')
        self.history.clear()
        self.history_list.delete(0, tk.END)
        self.input_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure('Large.TButton', font=('Arial', 10, 'bold'), padding=6)

    root.minsize(350, 350)
    root.geometry("350x350")

    app = DJBPM(root)
    root.mainloop()
