import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

class DJBPMCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("DJ BPM Calculator")
        self.root.resizable(False, False)
        self.history = []
        
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        # Input Section
        self.input_frame = ttk.LabelFrame(self.root, text="Original BPM")
        self.input_entry = ttk.Entry(self.input_frame, width=20, font=('Arial', 12))
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
            text="From/Slow BPM (-25%):", 
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
            text="To/Fast BPM (+33%):", 
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
        self.history_list = tk.Listbox(
            self.history_frame, 
            height=5, 
            width=40, 
            font=('Arial', 9)
        )
        
        # Clear button
        self.clear_btn = ttk.Button(
            self.root, 
            text="Clear All", 
            command=self.clear_input,
            style='Large.TButton'
        )
        
    def setup_layout(self):
        # Input Frame
        self.input_frame.pack(padx=10, pady=10, fill='x')
        self.input_entry.pack(side='left', padx=5, pady=2, expand=True)
        self.calculate_btn.pack(side='right', padx=5, pady=2)
        
        # Results Frame
        self.results_frame.pack(padx=10, pady=5, fill='x')
        self.slow_label.grid(row=0, column=0, sticky='w', padx=5)
        self.slow_display.grid(row=0, column=1, padx=5, pady=2)
        self.fast_label.grid(row=1, column=0, sticky='w', padx=5)
        self.fast_display.grid(row=1, column=1, padx=5, pady=2)
        
        # History Frame
        self.history_frame.pack(padx=10, pady=5, fill='x')
        self.history_list.pack(padx=5, pady=5, fill='both', expand=True)
        
        # Clear button
        self.clear_btn.pack(pady=10, ipadx=20)
        
    def calculate(self):
        try:
            original_bpm = float(self.input_entry.get())
            if original_bpm <= 0:
                raise ValueError("BPM must be positive")
                
            slow_bpm = original_bpm * 0.75
            fast_bpm = original_bpm / 0.75
            
            self.slow_bpm_var.set(f"{slow_bpm:.1f}")
            self.fast_bpm_var.set(f"{fast_bpm:.1f}")
            
            history_entry = f"Start: {original_bpm:.1f} | Slow: {slow_bpm:.1f} | Fast: {fast_bpm:.1f}"
            self.update_history(history_entry)
                        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e) if str(e) else "Please enter a valid positive number")
            self.input_entry.focus()
            
    def update_history(self, entry):
        self.history.insert(0, entry)
        if len(self.history) > 5:
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
    root.geometry("400x400")
    app = DJBPMCalculator(root)
    root.mainloop()
