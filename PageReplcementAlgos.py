# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches

# def fifo(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     for i, page in enumerate(ref_string):
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 memory.pop(0)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def lru(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     recently_used = []
#     for i, page in enumerate(ref_string):
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 lru_page = recently_used.pop(0)
#                 memory.remove(lru_page)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         else:
#             recently_used.remove(page)
#         recently_used.append(page)
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def draw_memory_chart(states, frames):
#     fig, ax = plt.subplots(figsize=(len(states) * 0.6, frames * 0.6))
#     ax.set_title("Page Replacement Process")
#     ax.set_xlabel("Step")
#     ax.set_ylabel("Memory Frames")

#     for i, (mem, status, page) in enumerate(states):
#         for j in range(frames):
#             if j < len(mem):
#                 val = mem[j]
#                 color = 'lightcoral' if status == "Fault" and j == len(mem)-1 else 'lightgreen'
#                 ax.add_patch(plt.Rectangle((i, frames - j - 1), 1, 1, color=color, edgecolor='black'))
#                 ax.text(i + 0.5, frames - j - 0.5, str(val), va='center', ha='center')
#             else:
#                 ax.add_patch(plt.Rectangle((i, frames - j - 1), 1, 1, color='white', edgecolor='gray'))

#     ax.set_xticks([i + 0.5 for i in range(len(states))])
#     ax.set_xticklabels([f'{page}' for _, _, page in states])
#     ax.set_yticks([])

#     hit_patch = mpatches.Patch(color='lightgreen', label='Hit')
#     fault_patch = mpatches.Patch(color='lightcoral', label='Page Fault')
#     ax.legend(handles=[hit_patch, fault_patch], loc='upper right')

#     plt.tight_layout()
#     plt.show()

# def run_algorithm():
#     try:
#         ref_string = list(map(int, entry_ref.get().split()))
#         frames = int(entry_frames.get())
#         algo = var_algo.get()

#         if algo == "FIFO":
#             faults, states = fifo(ref_string, frames)
#         elif algo == "LRU":
#             faults, states = lru(ref_string, frames)
#         else:
#             messagebox.showinfo("Coming Soon", "Only FIFO and LRU are implemented so far.")
#             return

#         result_label.config(text=f"Total Page Faults: {faults}")
#         draw_memory_chart(states, frames)

#     except Exception as e:
#         messagebox.showerror("Input Error", f"Error: {str(e)}")

# # GUI setup
# root = tk.Tk()
# root.title("Page Replacement Simulator")

# tk.Label(root, text="Reference String (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
# entry_ref = tk.Entry(root, width=40)
# entry_ref.grid(row=0, column=1)

# tk.Label(root, text="Number of Frames:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
# entry_frames = tk.Entry(root, width=10)
# entry_frames.grid(row=1, column=1, sticky="w")

# tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
# var_algo = tk.StringVar(root)
# var_algo.set("FIFO")
# tk.OptionMenu(root, var_algo, "FIFO", "LRU").grid(row=2, column=1, sticky="w")

# tk.Button(root, text="Run", command=run_algorithm).grid(row=3, column=0, columnspan=2, pady=10)
# result_label = tk.Label(root, text="Total Page Faults: ")
# result_label.grid(row=4, column=0, columnspan=2, pady=5)

# root.mainloop()
# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches

# def fifo(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     for i, page in enumerate(ref_string):
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 memory.pop(0)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def lru(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     recently_used = []
#     for i, page in enumerate(ref_string):
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 lru_page = recently_used.pop(0)
#                 memory.remove(lru_page)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         else:
#             recently_used.remove(page)
#         recently_used.append(page)
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def draw_memory_chart(states, frames):
#     fig, ax = plt.subplots(figsize=(len(states) * 0.6, frames * 0.6))
#     ax.set_title("Page Replacement Process")
#     ax.set_xlabel("Step")
#     ax.set_ylabel("Memory Frames")

#     for i, (mem, status, page) in enumerate(states):
#         for j in range(frames):
#             if j < len(mem):
#                 val = mem[j]
#                 color = 'lightcoral' if status == "Fault" and j == len(mem)-1 else 'lightgreen'
#                 ax.add_patch(plt.Rectangle((i, frames - j - 1), 1, 1, color=color, edgecolor='black'))
#                 ax.text(i + 0.5, frames - j - 0.5, str(val), va='center', ha='center')
#             else:
#                 ax.add_patch(plt.Rectangle((i, frames - j - 1), 1, 1, color='white', edgecolor='gray'))

#     ax.set_xticks([i + 0.5 for i in range(len(states))])
#     ax.set_xticklabels([f'{page}' for _, _, page in states])
#     ax.set_yticks([])

#     hit_patch = mpatches.Patch(color='lightgreen', label='Hit')
#     fault_patch = mpatches.Patch(color='lightcoral', label='Page Fault')
#     ax.legend(handles=[hit_patch, fault_patch], loc='upper right')

#     plt.tight_layout()
#     plt.show()

# def run_algorithm():
#     try:
#         ref_string = list(map(int, entry_ref.get().split()))
#         frames = int(entry_frames.get())
#         algo = var_algo.get()

#         if frames <= 0:
#             raise ValueError("Frame count must be positive.")

#         if algo == "FIFO":
#             faults, states = fifo(ref_string, frames)
#         elif algo == "LRU":
#             faults, states = lru(ref_string, frames)
#         else:
#             messagebox.showinfo("Coming Soon", "Only FIFO and LRU are implemented so far.")
#             return

#         # Output result
#         result_label.config(text=f"Total Page Faults: {faults}")

#         # Textual step-by-step output
#         text_output.delete("1.0", tk.END)
#         for i, (mem, status, page) in enumerate(states):
#             text_output.insert(tk.END, f"Step {i+1} - Page: {page} -> {status}, Memory: {mem}\n")

#         # Graphical output
#         draw_memory_chart(states, frames)

#     except Exception as e:
#         messagebox.showerror("Input Error", f"Error: {str(e)}")

# # GUI setup
# root = tk.Tk()
# root.title("Page Replacement Simulator")

# tk.Label(root, text="Reference String (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
# entry_ref = tk.Entry(root, width=40)
# entry_ref.grid(row=0, column=1)

# tk.Label(root, text="Number of Frames:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
# entry_frames = tk.Entry(root, width=10)
# entry_frames.grid(row=1, column=1, sticky="w")

# tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
# var_algo = tk.StringVar(root)
# var_algo.set("FIFO")
# tk.OptionMenu(root, var_algo, "FIFO", "LRU", "Optimal", "Clock", "Enhanced Second-Chance", "LFU", "MFU", "Random", "NRU", "Aging Algorithm").grid(row=2, column=1, sticky="w")

# tk.Button(root, text="Run", command=run_algorithm).grid(row=3, column=0, columnspan=2, pady=10)
# result_label = tk.Label(root, text="Total Page Faults: ")
# result_label.grid(row=4, column=0, columnspan=2, pady=5)

# # Text area for step-by-step output
# text_output = tk.Text(root, height=15, width=60)
# text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.patches as mpatches

# # Algorithms return memory states list for all steps
# def fifo(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     for page in ref_string:
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 memory.pop(0)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def lru(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     recently_used = []
#     for page in ref_string:
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 lru_page = recently_used.pop(0)
#                 memory.remove(lru_page)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         else:
#             recently_used.remove(page)
#         recently_used.append(page)
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# class PageReplacementApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Simulator")

#         # Input UI
#         tk.Label(root, text="Reference String (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
#         self.entry_ref = tk.Entry(root, width=40)
#         self.entry_ref.grid(row=0, column=1)

#         tk.Label(root, text="Number of Frames:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
#         self.entry_frames = tk.Entry(root, width=10)
#         self.entry_frames.grid(row=1, column=1, sticky="w")

#         tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
#         self.var_algo = tk.StringVar(root)
#         self.var_algo.set("FIFO")
#         tk.OptionMenu(root, self.var_algo, "FIFO", "LRU", "Optimal", "Clock", "Enhanced Second-Chance", "LFU", "MFU", "Random", "NRU", "Aging Algorithm").grid(row=2, column=1, sticky="w")

#         self.run_button = tk.Button(root, text="Run", command=self.start_simulation)
#         self.run_button.grid(row=3, column=0, columnspan=2, pady=10)

#         self.result_label = tk.Label(root, text="Total Page Faults: ")
#         self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

#         # Text area for step-by-step output
#         self.text_output = tk.Text(root, height=10, width=60)
#         self.text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#         # Placeholder for matplotlib figure in Tkinter
#         self.fig, self.ax = plt.subplots(figsize=(6, 3))
#         self.canvas = FigureCanvasTkAgg(self.fig, master=root)
#         self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

#         # Next step button for animation
#         self.next_button = tk.Button(root, text="Next Step", command=self.next_step, state="disabled")
#         self.next_button.grid(row=7, column=0, columnspan=2, pady=10)

#         # Internal state for simulation
#         self.states = []
#         self.current_step = 0
#         self.frames = 0
#         self.page_faults = 0

#     def start_simulation(self):
#         try:
#             ref_string = list(map(int, self.entry_ref.get().split()))
#             self.frames = int(self.entry_frames.get())
#             algo = self.var_algo.get()

#             if self.frames <= 0:
#                 raise ValueError("Frame count must be positive.")

#             if algo == "FIFO":
#                 self.page_faults, self.states = fifo(ref_string, self.frames)
#             elif algo == "LRU":
#                 self.page_faults, self.states = lru(ref_string, self.frames)
#             else:
#                 messagebox.showinfo("Coming Soon", "Only FIFO and LRU are implemented so far.")
#                 return

#             self.result_label.config(text=f"Total Page Faults: {self.page_faults}")

#             # Disable inputs & run button during animation
#             self.entry_ref.config(state='disabled')
#             self.entry_frames.config(state='disabled')
#             self.next_button.config(state='normal')
#             self.run_button.config(state='disabled')

#             self.text_output.delete("1.0", tk.END)
#             self.current_step = 0

#             # Draw first step
#             self.draw_step()

#         except Exception as e:
#             messagebox.showerror("Input Error", f"Error: {str(e)}")

#     def draw_step(self):
#         self.ax.clear()
#         mem, status, page = self.states[self.current_step]
#         self.text_output.insert(tk.END, f"Step {self.current_step + 1} - Page: {page} -> {status}, Memory: {mem}\n")
#         self.text_output.see(tk.END)

#         # Draw memory frames as rectangles
#         for j in range(self.frames):
#             if j < len(mem):
#                 val = mem[j]
#                 color = 'lightcoral' if (status == "Fault" and j == len(mem) - 1) else 'lightgreen'
#                 self.ax.add_patch(plt.Rectangle((0, self.frames - j - 1), 1, 1, color=color, edgecolor='black'))
#                 self.ax.text(0.5, self.frames - j - 0.5, str(val), va='center', ha='center')
#             else:
#                 self.ax.add_patch(plt.Rectangle((0, self.frames - j - 1), 1, 1, color='white', edgecolor='gray'))

#         self.ax.set_xlim(0, 1)
#         self.ax.set_ylim(0, self.frames)
#         self.ax.set_xticks([])
#         self.ax.set_yticks([])
#         self.ax.set_title(f"Step {self.current_step + 1}: Processing Page {page} ({status})")

#         # Legend
#         hit_patch = mpatches.Patch(color='lightgreen', label='Hit')
#         fault_patch = mpatches.Patch(color='lightcoral', label='Page Fault')
#         self.ax.legend(handles=[hit_patch, fault_patch], loc='upper right')

#         self.canvas.draw()

#     def next_step(self):
#         if self.current_step < len(self.states) - 1:
#             self.current_step += 1
#             self.draw_step()
#         else:
#             # End of simulation
#             self.next_button.config(state='disabled')
#             messagebox.showinfo("Simulation Finished", "You have reached the last step.")
#             # Re-enable inputs and run button
#             self.entry_ref.config(state='normal')
#             self.entry_frames.config(state='normal')
#             self.run_button.config(state='normal')

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.patches as mpatches

# def fifo(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     for page in ref_string:
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 memory.pop(0)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# def lru(ref_string, frames):
#     memory_states = []
#     memory = []
#     page_faults = 0
#     recently_used = []
#     for page in ref_string:
#         status = "Hit"
#         if page not in memory:
#             if len(memory) >= frames:
#                 lru_page = recently_used.pop(0)
#                 memory.remove(lru_page)
#             memory.append(page)
#             page_faults += 1
#             status = "Fault"
#         else:
#             recently_used.remove(page)
#         recently_used.append(page)
#         memory_states.append((list(memory), status, page))
#     return page_faults, memory_states

# class PageReplacementApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Simulator")

#         tk.Label(root, text="Reference String (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
#         self.entry_ref = tk.Entry(root, width=40)
#         self.entry_ref.grid(row=0, column=1)

#         tk.Label(root, text="Number of Frames:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
#         self.entry_frames = tk.Entry(root, width=10)
#         self.entry_frames.grid(row=1, column=1, sticky="w")

#         tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
#         self.var_algo = tk.StringVar(root)
#         self.var_algo.set("FIFO")
#         tk.OptionMenu(root, self.var_algo, "FIFO", "LRU", "Optimal", "Clock", "Enhanced Second-Chance", "LFU", "MFU", "Random", "NRU", "Aging Algorithm").grid(row=2, column=1, sticky="w")

#         self.run_button = tk.Button(root, text="Run", command=self.start_simulation)
#         self.run_button.grid(row=3, column=0, columnspan=2, pady=10)

#         self.result_label = tk.Label(root, text="Total Page Faults: ")
#         self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

#         self.text_output = tk.Text(root, height=10, width=60)
#         self.text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#         self.fig, self.ax = plt.subplots(figsize=(6, 3))
#         self.canvas = FigureCanvasTkAgg(self.fig, master=root)
#         self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

#         # Simulation state
#         self.states = []
#         self.current_step = 0
#         self.frames = 0
#         self.page_faults = 0

#     def start_simulation(self):
#         try:
#             ref_string = list(map(int, self.entry_ref.get().split()))
#             self.frames = int(self.entry_frames.get())
#             algo = self.var_algo.get()

#             if self.frames <= 0:
#                 raise ValueError("Frame count must be positive.")

#             if algo == "FIFO":
#                 self.page_faults, self.states = fifo(ref_string, self.frames)
#             elif algo == "LRU":
#                 self.page_faults, self.states = lru(ref_string, self.frames)
#             else:
#                 messagebox.showinfo("Coming Soon", "Only FIFO and LRU are implemented so far.")
#                 return

#             self.result_label.config(text=f"Total Page Faults: {self.page_faults}")

#             # Disable inputs during animation
#             self.entry_ref.config(state='disabled')
#             self.entry_frames.config(state='disabled')
#             self.run_button.config(state='disabled')

#             self.text_output.delete("1.0", tk.END)
#             self.current_step = 0

#             # Start auto animation
#             self.animate_step()

#         except Exception as e:
#             messagebox.showerror("Input Error", f"Error: {str(e)}")

#     def draw_step(self):
#      self.ax.clear()
#      mem, status, page = self.states[self.current_step]
#      self.text_output.insert(tk.END, f"Step {self.current_step + 1} - Page: {page} -> {status}, Memory: {mem}\n")
#      self.text_output.see(tk.END)

#     bar_width = 0.6
#     y_positions = range(len(mem))  # For horizontal bars
    
#     colors = []
#     for i, val in enumerate(mem):
#         # Highlight the most recently added page if fault
#         if status == "Fault" and i == len(mem) - 1:
#             colors.append('lightcoral')
#         else:
#             colors.append('lightgreen')
    
#     self.ax.bar(y_positions, mem, color=colors, width=bar_width, edgecolor='black')

#     # Annotate each bar with page number
#     for i, val in enumerate(mem):
#         self.ax.text(i, val/2 if val != 0 else 0.5, str(val), ha='center', va='center', fontsize=14, color='black')

#     self.ax.set_ylim(0, max(mem) + 1 if mem else 1)
#     self.ax.set_xlim(-0.5, len(mem) - 0.5)
#     self.ax.set_xticks(y_positions)
#     self.ax.set_xticklabels([f'Frame {i+1}' for i in y_positions], fontsize=12)
#     self.ax.set_yticks([])

#     self.ax.set_title(f"Step {self.current_step + 1}: Processing Page {page} ({status})", fontsize=16)

#     hit_patch = mpatches.Patch(color='lightgreen', label='Hit')
#     fault_patch = mpatches.Patch(color='lightcoral', label='Page Fault')
#     self.ax.legend(handles=[hit_patch, fault_patch], loc='upper right', fontsize=12)

#     self.canvas.draw()


#     def animate_step(self):
#         self.draw_step()

#         if self.current_step < len(self.states) - 1:
#             self.current_step += 1
#             # Call animate_step again after 1000 ms (1 second)
#             self.root.after(1000, self.animate_step)
#         else:
#             # Animation finished
#             messagebox.showinfo("Simulation Finished", "Simulation complete.")
#             self.entry_ref.config(state='normal')
#             self.entry_frames.config(state='normal')
#             self.run_button.config(state='normal')

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementApp(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.patches as mpatches

# class PageReplacementSimulator:
#     def __init__(self, root):
#         self.root = root
#         root.title("Page Replacement Simulator")

#         # Inputs
#         tk.Label(root, text="Reference String (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
#         self.entry_ref = tk.Entry(root, width=40)
#         self.entry_ref.grid(row=0, column=1, sticky="w")

#         tk.Label(root, text="Number of Frames:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
#         self.entry_frames = tk.Entry(root, width=10)
#         self.entry_frames.grid(row=1, column=1, sticky="w")

#         tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
#         self.var_algo = tk.StringVar(root)
#         self.var_algo.set("FIFO")
#         tk.OptionMenu(root, self.var_algo, "FIFO", "LRU").grid(row=2, column=1, sticky="w")

#         tk.Button(root, text="Run", command=self.run_algorithm).grid(row=3, column=0, columnspan=2, pady=10)

#         self.result_label = tk.Label(root, text="Total Page Faults: ")
#         self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

#         # Text output area
#         self.text_output = tk.Text(root, height=15, width=60)
#         self.text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#         # Matplotlib figure for visualization (bigger & horizontal)
#         self.fig, self.ax = plt.subplots(figsize=(10, 3))
#         self.canvas = FigureCanvasTkAgg(self.fig, master=root)
#         self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

#         self.states = []  # To hold each step (memory, status, page)
#         self.current_step = 0

#     def fifo(self, ref_string, frames):
#         memory = []
#         page_faults = 0
#         steps = []
#         for page in ref_string:
#             if page not in memory:
#                 if len(memory) >= frames:
#                     memory.pop(0)
#                 memory.append(page)
#                 page_faults += 1
#                 steps.append((memory.copy(), "Fault", page))
#             else:
#                 steps.append((memory.copy(), "Hit", page))
#         return page_faults, steps

#     def lru(self, ref_string, frames):
#         memory = []
#         page_faults = 0
#         recently_used = []
#         steps = []
#         for page in ref_string:
#             if page not in memory:
#                 if len(memory) >= frames:
#                     lru_page = recently_used.pop(0)
#                     memory.remove(lru_page)
#                 memory.append(page)
#                 page_faults += 1
#                 steps.append((memory.copy(), "Fault", page))
#             else:
#                 recently_used.remove(page)
#                 steps.append((memory.copy(), "Hit", page))
#             recently_used.append(page)
#         return page_faults, steps

#     def run_algorithm(self):
#         self.text_output.delete('1.0', tk.END)
#         self.ax.clear()
#         self.canvas.draw()
#         self.current_step = 0
#         try:
#             ref_string = list(map(int, self.entry_ref.get().split()))
#             frames = int(self.entry_frames.get())
#             algo = self.var_algo.get()

#             if algo == "FIFO":
#                 faults, self.states = self.fifo(ref_string, frames)
#             elif algo == "LRU":
#                 faults, self.states = self.lru(ref_string, frames)
#             else:
#                 messagebox.showinfo("Not Implemented", "Only FIFO and LRU are implemented.")
#                 return

#             self.result_label.config(text=f"Total Page Faults: {faults}")

#             # Start visualization steps automatically
#             self.root.after(500, self.show_next_step)

#         except Exception as e:
#             messagebox.showerror("Input Error", "Please enter a valid reference string and frame count.")
#             print(e)

#     def show_next_step(self):
#         if self.current_step >= len(self.states):
#             return  # Finished all steps
#         self.draw_step()
#         self.current_step += 1
#         self.root.after(1000, self.show_next_step)  # 1 second delay between steps

#     def draw_step(self):
#         self.ax.clear()
#         mem, status, page = self.states[self.current_step]
#         self.text_output.insert(tk.END, f"Step {self.current_step + 1} - Page: {page} -> {status}, Memory: {mem}\n")
#         self.text_output.see(tk.END)

#         bar_width = 0.6
#         y_positions = range(len(mem))  # Positions along x-axis for horizontal bars

#         colors = []
#         for i, val in enumerate(mem):
#             # Highlight the most recently added page in red if fault
#             if status == "Fault" and i == len(mem) - 1:
#                 colors.append('lightcoral')
#             else:
#                 colors.append('lightgreen')

#         self.ax.bar(y_positions, mem, color=colors, width=bar_width, edgecolor='black')

#         # Annotate each bar with page number (in the middle of bar height)
#         for i, val in enumerate(mem):
#             self.ax.text(i, val/2 if val != 0 else 0.9, str(val), ha='center', va='center', fontsize=14, color='black')

#         self.ax.set_ylim(0, max(mem) + 1 if mem else 1)
#         self.ax.set_xlim(-0.5, len(mem) - 0.5)
#         self.ax.set_xticks(y_positions)
#         self.ax.set_xticklabels([f'Frame {i+1}' for i in y_positions], fontsize=12)
#         self.ax.set_yticks([])

#         self.ax.set_title(f"Step {self.current_step + 1}: Processing Page {page} ({status})", fontsize=16)

#         hit_patch = mpatches.Patch(color='lightgreen', label='Hit')
#         fault_patch = mpatches.Patch(color='lightcoral', label='Page Fault')
#         self.ax.legend(handles=[hit_patch, fault_patch], loc='upper right', fontsize=12)

#         self.canvas.draw()


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementSimulator(root)
#     root.mainloop()




# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.patches as mpatches


# class PageReplacementSimulator(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Page Replacement Simulator")
#         self.geometry("900x600")
#         self.configure(bg="#f0f0f0")

#         # Data holders
#         self.steps = []
#         self.current_step = 0

#         self.create_widgets()

#     def create_widgets(self):
#         # Top frame for inputs
#         input_frame = ttk.Frame(self)
#         input_frame.pack(pady=10, padx=20, fill='x')

#         # Reference string input
#         ttk.Label(input_frame, text="Reference String (space-separated):").grid(row=0, column=0, sticky="w")
#         self.ref_entry = ttk.Entry(input_frame)
#         self.ref_entry.grid(row=0, column=1, sticky="ew", padx=10)
#         self.ref_entry.insert(0, "7 0 1 2 0 3 0 4 2 3")

#         # Number of frames input
#         ttk.Label(input_frame, text="Number of Frames:").grid(row=1, column=0, sticky="w")
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.grid(row=1, column=1, sticky="w", padx=10)
#         self.frames_entry.insert(0, "3")

#         # Algorithm selection
#         ttk.Label(input_frame, text="Choose Algorithm:").grid(row=2, column=0, sticky="w")
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var, values=["LRU", "FIFO"], state="readonly", width=10)
#         algo_combo.grid(row=2, column=1, sticky="w", padx=10)

#         # Run button
#         run_button = ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation)
#         run_button.grid(row=3, column=0, columnspan=2, pady=10)

#         # Expand input_frame columns nicely
#         input_frame.columnconfigure(1, weight=1)

#         # Output frame for text and chart
#         output_frame = ttk.Frame(self)
#         output_frame.pack(fill="both", expand=True, padx=20, pady=10)

#         # Text output area with scrollbar
#         text_frame = ttk.Frame(output_frame)
#         text_frame.pack(side="left", fill="both", expand=True)

#         self.output_text = tk.Text(text_frame, height=15, width=50, wrap="none", font=("Consolas", 10))
#         self.output_text.pack(side="left", fill="both", expand=True)
#         self.output_text.config(state="disabled")

#         scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.output_text.yview)
#         scrollbar.pack(side="right", fill="y")
#         self.output_text['yscrollcommand'] = scrollbar.set

#         # Chart frame
#         chart_frame = ttk.Frame(output_frame)
#         chart_frame.pack(side="left", fill="both", expand=True, padx=(20,0))

#         self.fig, self.ax = plt.subplots(figsize=(7, 3))
#         self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
#         self.canvas.get_tk_widget().pack(fill="both", expand=True)

#         # Navigation frame for steps
#         nav_frame = ttk.Frame(self)
#         nav_frame.pack(pady=5)

#         self.prev_button = ttk.Button(nav_frame, text="Previous Step", command=self.prev_step, state="disabled")
#         self.prev_button.pack(side="left", padx=5)

#         self.next_button = ttk.Button(nav_frame, text="Next Step", command=self.next_step, state="disabled")
#         self.next_button.pack(side="left", padx=5)

#         # Status label
#         self.status_label = ttk.Label(self, text="Enter inputs and run simulation.", font=("Arial", 10))
#         self.status_label.pack(pady=5)

#     def run_simulation(self):
#         ref_string = self.ref_entry.get().strip()
#         if not ref_string:
#             messagebox.showerror("Error", "Reference string cannot be empty.")
#             return

#         try:
#             pages = list(map(int, ref_string.split()))
#         except ValueError:
#             messagebox.showerror("Error", "Reference string must be integers separated by spaces.")
#             return

#         try:
#             num_frames = int(self.frames_entry.get())
#             if num_frames <= 0:
#                 raise ValueError()
#         except ValueError:
#             messagebox.showerror("Error", "Number of frames must be a positive integer.")
#             return

#         algorithm = self.algorithm_var.get()

#         if algorithm == "LRU":
#             self.steps, page_faults = self.simulate_lru(pages, num_frames)
#         elif algorithm == "FIFO":
#             self.steps, page_faults = self.simulate_fifo(pages, num_frames)
#         else:
#             messagebox.showerror("Error", f"Algorithm '{algorithm}' not supported.")
#             return

#         # Show total faults in status
#         self.status_label.config(text=f"Total Page Faults: {page_faults}")

#         # Display all steps text
#         self.output_text.config(state="normal")
#         self.output_text.delete(1.0, "end")
#         for step_text in self.steps:
#             self.output_text.insert("end", step_text + "\n")
#         self.output_text.config(state="disabled")

#         # Reset navigation
#         self.current_step = 0
#         self.prev_button.config(state="disabled")
#         self.next_button.config(state="normal" if len(self.steps) > 1 else "disabled")

#         # Show first step graph
#         self.show_step_graph(self.current_step)

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages, start=1):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     # Remove LRU page
#                     # LRU is page with earliest last occurrence
#                     last_used_indices = [max([idx for idx, p in enumerate(pages[:i-1]) if p == mem_page], default=-1) for mem_page in memory]
#                     lru_index = last_used_indices.index(min(last_used_indices))
#                     memory[lru_index] = page
#             else:
#                 # On hit, no replacement, but reorder for LRU if desired (not necessary for visualization)
#                 pass

#             # Compose step text
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         queue = []

#         for i, page in enumerate(pages, start=1):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     queue.append(page)
#                 else:
#                     # Remove first inserted page (FIFO)
#                     removed = queue.pop(0)
#                     memory[memory.index(removed)] = page
#                     queue.append(page)
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def show_step_graph(self, step_idx):
#         if step_idx < 0 or step_idx >= len(self.steps):
#             return

#         step_info = self.steps[step_idx]
#         # Parse step info: "Step X - Page: Y -> Hit/Fault, Memory: [..]"
#         try:
#             parts = step_info.split(", Memory: ")
#             mem_str = parts[1]
#             mem_list = eval(mem_str)
#             # Extract page and fault/hit info
#             left = parts[0].split("->")
#             page_info = left[0].strip()
#             fault_hit = left[1].strip()
#             page_num = int(page_info.split("Page: ")[1])
#         except Exception as e:
#             print(f"Parsing error: {e}")
#             return

#         # Clear previous plot
#         self.ax.clear()

#         # Bar colors: Fault=red, Hit=green
#         colors = []
#         for p in mem_list:
#             if p == page_num and fault_hit == "Fault":
#                 colors.append("#f08080")  # light red
#             else:
#                 colors.append("#90ee90")  # light green

#         # Horizontal bar chart
#         y_pos = range(len(mem_list))
#         self.ax.barh(y_pos, mem_list, color=colors, edgecolor="black", height=0.6)

#         # Label bars with page numbers
#         for i, val in enumerate(mem_list):
#             self.ax.text(val / 2 if val != 0 else 0.1, i, str(val), va='center', ha='center', fontsize=12, fontweight='bold')

#         self.ax.set_yticks(y_pos)
#         self.ax.set_yticklabels([f"Frame {i+1}" for i in y_pos], fontsize=11)
#         self.ax.invert_yaxis()
#         self.ax.set_xlabel("Page Number", fontsize=12)
#         self.ax.set_title(f"{step_info}", fontsize=14)

#         # Legend
#         hit_patch = mpatches.Patch(color="#90ee90", label="Hit")
#         fault_patch = mpatches.Patch(color="#f08080", label="Page Fault")
#         self.ax.legend(handles=[hit_patch, fault_patch])

#         self.fig.tight_layout()
#         self.canvas.draw()

#         # Update navigation buttons
#         self.prev_button.config(state="normal" if step_idx > 0 else "disabled")
#         self.next_button.config(state="normal" if step_idx < len(self.steps) - 1 else "disabled")

#         # Scroll output_text to this step line
#         self.output_text.config(state="normal")
#         self.output_text.see(f"{step_idx + 1}.0")
#         self.output_text.config(state="disabled")

#     def next_step(self):
#         if self.current_step < len(self.steps) - 1:
#             self.current_step += 1
#             self.show_step_graph(self.current_step)

#     def prev_step(self):
#         if self.current_step > 0:
#             self.current_step -= 1
#             self.show_step_graph(self.current_step)


# if __name__ == "__main__":
#     app = PageReplacementSimulator()
#     app.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.patches as mpatches


# class PageReplacementSimulator(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Page Replacement Simulator")
#         self.geometry("900x600")
#         self.configure(bg="#f0f0f0")

#         # Data holders
#         self.steps = []
#         self.current_step = 0
#         self.animation_running = False
#         self.step_delay = 1500  # milliseconds delay between steps

#         self.create_widgets()

#     def create_widgets(self):
#         # Top frame for inputs
#         input_frame = ttk.Frame(self)
#         input_frame.pack(pady=10, padx=20, fill='x')

#         # Reference string input
#         ttk.Label(input_frame, text="Reference String (space-separated):").grid(row=0, column=0, sticky="w")
#         self.ref_entry = ttk.Entry(input_frame)
#         self.ref_entry.grid(row=0, column=1, sticky="ew", padx=10)
#         self.ref_entry.insert(0, "7 0 1 2 0 3 0 4 2 3")

#         # Number of frames input
#         ttk.Label(input_frame, text="Number of Frames:").grid(row=1, column=0, sticky="w")
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.grid(row=1, column=1, sticky="w", padx=10)
#         self.frames_entry.insert(0, "3")

#         # Algorithm selection
#         ttk.Label(input_frame, text="Choose Algorithm:").grid(row=2, column=0, sticky="w")
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var, values=["LRU", "FIFO"], state="readonly", width=10)
#         algo_combo.grid(row=2, column=1, sticky="w", padx=10)

#         # Run button
#         run_button = ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation)
#         run_button.grid(row=3, column=0, columnspan=2, pady=10)

#         # Expand input_frame columns nicely
#         input_frame.columnconfigure(1, weight=1)

#         # Output frame for text and chart
#         output_frame = ttk.Frame(self)
#         output_frame.pack(fill="both", expand=True, padx=20, pady=10)

#         # Text output area with scrollbar
#         text_frame = ttk.Frame(output_frame)
#         text_frame.pack(side="left", fill="both", expand=True)

#         # Bigger font for step text
#         self.output_text = tk.Text(text_frame, height=15, width=50, wrap="none", font=("Consolas", 14))
#         self.output_text.pack(side="left", fill="both", expand=True)
#         self.output_text.config(state="disabled")

#         scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.output_text.yview)
#         scrollbar.pack(side="right", fill="y")
#         self.output_text['yscrollcommand'] = scrollbar.set

#         # Chart frame
#         chart_frame = ttk.Frame(output_frame)
#         chart_frame.pack(side="left", fill="both", expand=True, padx=(20,0))

#         self.fig, self.ax = plt.subplots(figsize=(7, 3))
#         self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
#         self.canvas.get_tk_widget().pack(fill="both", expand=True)

#         # Status label
#         self.status_label = ttk.Label(self, text="Enter inputs and run simulation.", font=("Arial", 12))
#         self.status_label.pack(pady=5)

#     def run_simulation(self):
#         if self.animation_running:
#             # If animation is running, ignore repeated run
#             return

#         ref_string = self.ref_entry.get().strip()
#         if not ref_string:
#             messagebox.showerror("Error", "Reference string cannot be empty.")
#             return

#         try:
#             pages = list(map(int, ref_string.split()))
#         except ValueError:
#             messagebox.showerror("Error", "Reference string must be integers separated by spaces.")
#             return

#         try:
#             num_frames = int(self.frames_entry.get())
#             if num_frames <= 0:
#                 raise ValueError()
#         except ValueError:
#             messagebox.showerror("Error", "Number of frames must be a positive integer.")
#             return

#         algorithm = self.algorithm_var.get()

#         if algorithm == "LRU":
#             self.steps, page_faults = self.simulate_lru(pages, num_frames)
#         elif algorithm == "FIFO":
#             self.steps, page_faults = self.simulate_fifo(pages, num_frames)
#         else:
#             messagebox.showerror("Error", f"Algorithm '{algorithm}' not supported.")
#             return

#         # Show total faults in status
#         self.status_label.config(text=f"Total Page Faults: {page_faults} (Animating...)")

#         # Clear text box (we will show steps one by one)
#         self.output_text.config(state="normal")
#         self.output_text.delete(1.0, "end")
#         self.output_text.config(state="disabled")

#         self.current_step = 0
#         self.animation_running = True
#         self.animate_steps()

#     def animate_steps(self):
#         if self.current_step >= len(self.steps):
#             self.animation_running = False
#             self.status_label.config(text=f"Simulation complete! Total steps: {len(self.steps)}")
#             return

#         # Add current step to text output
#         self.output_text.config(state="normal")
#         self.output_text.insert("end", self.steps[self.current_step] + "\n")
#         self.output_text.see("end")
#         self.output_text.config(state="disabled")

#         # Show graph for this step
#         self.show_step_graph(self.current_step)

#         self.current_step += 1
#         # Call this function again after delay
#         self.after(self.step_delay, self.animate_steps)

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages, start=1):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     # Remove LRU page: page with earliest last occurrence before current i
#                     last_used_indices = [max([idx for idx, p in enumerate(pages[:i-1]) if p == mem_page], default=-1) for mem_page in memory]
#                     lru_index = last_used_indices.index(min(last_used_indices))
#                     memory[lru_index] = page
#             # Compose step text
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         queue = []

#         for i, page in enumerate(pages, start=1):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     queue.append(page)
#                 else:
#                     removed = queue.pop(0)
#                     memory[memory.index(removed)] = page
#                     queue.append(page)
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def show_step_graph(self, step_idx):
#         if step_idx < 0 or step_idx >= len(self.steps):
#             return

#         step_info = self.steps[step_idx]
#         try:
#             parts = step_info.split(", Memory: ")
#             mem_str = parts[1]
#             mem_list = eval(mem_str)
#             left = parts[0].split("->")
#             page_info = left[0].strip()
#             fault_hit = left[1].strip()
#             page_num = int(page_info.split("Page: ")[1])
#         except Exception as e:
#             print(f"Parsing error: {e}")
#             return

#         self.ax.clear()

#         colors = []
#         for p in mem_list:
#             if p == page_num and fault_hit == "Fault":
#                 colors.append("#f08080")  # light red for fault
#             else:
#                 colors.append("#90ee90")  # light green for hit/other pages

#         y_pos = range(len(mem_list))
#         self.ax.barh(y_pos, mem_list, color=colors, edgecolor="black", height=0.6)

#         for i, val in enumerate(mem_list):
#             self.ax.text(val / 2 if val != 0 else 0.1, i, str(val), va='center', ha='center', fontsize=14, fontweight='bold')

#         self.ax.set_yticks(y_pos)
#         self.ax.set_yticklabels([f"Frame {i+1}" for i in y_pos], fontsize=12)
#         self.ax.invert_yaxis()
#         self.ax.set_xlabel("Page Number", fontsize=12)
#         self.ax.set_title(f"{step_info}", fontsize=14)

#         hit_patch = mpatches.Patch(color="#90ee90", label="Hit")
#         fault_patch = mpatches.Patch(color="#f08080", label="Page Fault")
#         self.ax.legend(handles=[hit_patch, fault_patch])

#         self.fig.tight_layout()
#         self.canvas.draw()


# if __name__ == "__main__":
#     app = PageReplacementSimulator()
#     app.mainloop()




# import tkinter as tk
# from tkinter import ttk, messagebox

# class PageReplacementSimulator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Simulator")

#         self.pages = []
#         self.steps = []

#         # Input Frame
#         input_frame = ttk.Frame(root)
#         input_frame.pack(pady=10)

#         ttk.Label(input_frame, text="Pages (space-separated):").grid(row=0, column=0, padx=5)
#         self.pages_entry = ttk.Entry(input_frame, width=30)
#         self.pages_entry.grid(row=0, column=1, padx=5)

#         ttk.Label(input_frame, text="Frames:").grid(row=0, column=2, padx=5)
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.grid(row=0, column=3, padx=5)

#         ttk.Label(input_frame, text="Algorithm:").grid(row=0, column=4, padx=5)
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var,
#                                   values=["LRU", "FIFO", "Optimal", "LFU", "MFU"],
#                                   state="readonly", width=10)
#         algo_combo.grid(row=0, column=5, padx=5)

#         ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation).grid(row=0, column=6, padx=5)

#         # Output Frame
#         self.output_text = tk.Text(root, height=20, width=90)
#         self.output_text.pack(pady=10)

#     def run_simulation(self):
#         try:
#             self.pages = list(map(int, self.pages_entry.get().strip().split()))
#             num_frames = int(self.frames_entry.get())
#             algorithm = self.algorithm_var.get()

#             if not self.pages or num_frames <= 0:
#                 raise ValueError

#             if algorithm == "LRU":
#                 self.steps, page_faults = self.simulate_lru(self.pages, num_frames)
#             elif algorithm == "FIFO":
#                 self.steps, page_faults = self.simulate_fifo(self.pages, num_frames)
#             elif algorithm == "Optimal":
#                 self.steps, page_faults = self.simulate_optimal(self.pages, num_frames)
#             elif algorithm == "LFU":
#                 self.steps, page_faults = self.simulate_lfu(self.pages, num_frames)
#             elif algorithm == "MFU":
#                 self.steps, page_faults = self.simulate_mfu(self.pages, num_frames)

#             self.display_output(page_faults)
#         except Exception as e:
#             messagebox.showerror("Error", "Invalid input. Please enter correct values.")

#     def display_output(self, faults):
#         self.output_text.delete(1.0, tk.END)
#         for step in self.steps:
#             self.output_text.insert(tk.END, step + "\n")
#         self.output_text.insert(tk.END, f"\nTotal Page Faults: {faults}")

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             if page not in memory:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory.pop(0)
#                     memory.append(page)
#             else:
#                 memory.remove(page)
#                 memory.append(page)

#             step_type = "Fault" if page not in memory[:-1] else "Hit"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         faults = 0
#         pointer = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory[pointer] = page
#                     pointer = (pointer + 1) % num_frames
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_optimal(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     future = []
#                     for mem_page in memory:
#                         try:
#                             idx = pages[i+1:].index(mem_page)
#                         except ValueError:
#                             idx = float('inf')
#                         future.append(idx)
#                     replace_index = future.index(max(future))
#                     memory[replace_index] = page
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_lfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     min_freq = min(freq[pg] for pg in memory)
#                     candidates = [pg for pg in memory if freq[pg] == min_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             else:
#                 freq[page] += 1

#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

#     def simulate_mfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     max_freq = max(freq[pg] for pg in memory)
#                     candidates = [pg for pg in memory if freq[pg] == max_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             else:
#                 freq[page] += 1

#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")

#         return steps, faults

# # Launch the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementSimulator(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox

# class PageReplacementSimulator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Simulator")

#         self.pages = []
#         self.steps = []

#         # Input Frame
#         input_frame = ttk.Frame(root)
#         input_frame.pack(pady=10)

#         ttk.Label(input_frame, text="Pages (space-separated):").grid(row=0, column=0, padx=5)
#         self.pages_entry = ttk.Entry(input_frame, width=30)
#         self.pages_entry.grid(row=0, column=1, padx=5)

#         ttk.Label(input_frame, text="Frames:").grid(row=0, column=2, padx=5)
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.grid(row=0, column=3, padx=5)

#         ttk.Label(input_frame, text="Algorithm:").grid(row=0, column=4, padx=5)
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var,
#                                   values=["LRU", "FIFO", "Optimal", "LFU", "MFU"],
#                                   state="readonly", width=10)
#         algo_combo.grid(row=0, column=5, padx=5)

#         ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation).grid(row=0, column=6, padx=5)

#         # Output Frame
#         self.output_text = tk.Text(root, height=20, width=90)
#         self.output_text.pack(pady=10)

#     def run_simulation(self):
#         try:
#             pages_input = self.pages_entry.get().strip()
#             frames_input = self.frames_entry.get().strip()

#             if not pages_input or not frames_input:
#                 raise ValueError("Both pages and frames must be provided.")

#             self.pages = list(map(int, pages_input.split()))
#             num_frames = int(frames_input)

#             if num_frames <= 0:
#                 raise ValueError("Number of frames must be greater than 0.")

#             algorithm = self.algorithm_var.get()

#             if algorithm == "LRU":
#                 self.steps, page_faults = self.simulate_lru(self.pages, num_frames)
#             elif algorithm == "FIFO":
#                 self.steps, page_faults = self.simulate_fifo(self.pages, num_frames)
#             elif algorithm == "Optimal":
#                 self.steps, page_faults = self.simulate_optimal(self.pages, num_frames)
#             elif algorithm == "LFU":
#                 self.steps, page_faults = self.simulate_lfu(self.pages, num_frames)
#             elif algorithm == "MFU":
#                 self.steps, page_faults = self.simulate_mfu(self.pages, num_frames)

#             self.display_output(page_faults)

#         except ValueError as ve:
#             messagebox.showerror("Input Error", str(ve))
#         except Exception as e:
#             messagebox.showerror("Error", f"An unexpected error occurred.\n{e}")

#     def display_output(self, faults):
#         self.output_text.delete(1.0, tk.END)
#         for step in self.steps:
#             self.output_text.insert(tk.END, step + "\n")
#         self.output_text.insert(tk.END, f"\nTotal Page Faults: {faults}")

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             if page in memory:
#                 memory.remove(page)
#                 memory.append(page)
#                 hit = True
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory.pop(0)
#                     memory.append(page)
#                 hit = False

#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")
#         return steps, faults

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         faults = 0
#         pointer = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory[pointer] = page
#                     pointer = (pointer + 1) % num_frames

#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")
#         return steps, faults

#     def simulate_optimal(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     future = []
#                     for mem_page in memory:
#                         try:
#                             idx = pages[i+1:].index(mem_page)
#                         except ValueError:
#                             idx = float('inf')
#                         future.append(idx)
#                     replace_index = future.index(max(future))
#                     memory[replace_index] = page
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")
#         return steps, faults

#     def simulate_lfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             if page in memory:
#                 freq[page] += 1
#                 hit = True
#             else:
#                 faults += 1
#                 hit = False
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     min_freq = min(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == min_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")
#         return steps, faults

#     def simulate_mfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []

#         for i, page in enumerate(pages):
#             if page in memory:
#                 freq[page] += 1
#                 hit = True
#             else:
#                 faults += 1
#                 hit = False
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     max_freq = max(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == max_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory.copy()}")
#         return steps, faults

# # Launch the GUI app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementSimulator(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class PageReplacementSimulator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Visual Simulator")
#         self.root.geometry("1200x700")

#         self.pages = []
#         self.steps = []
#         self.memory_states = []
#         self.current_step = 0

#         # Top Input Frame
#         input_frame = ttk.Frame(root)
#         input_frame.pack(fill='x', pady=20)

#         ttk.Label(input_frame, text="Pages (space-separated):").pack(side='left', padx=5)
#         self.pages_entry = ttk.Entry(input_frame, width=30)
#         self.pages_entry.pack(side='left', padx=8)

#         ttk.Label(input_frame, text="Frames:").pack(side='left', padx=8)
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.pack(side='left', padx=8)

#         ttk.Label(input_frame, text="Algorithm:").pack(side='left', padx=8)
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var,
#                                   values=["LRU", "FIFO", "Optimal", "LFU", "MFU"],
#                                   state="readonly", width=20)
#         algo_combo.pack(side='left', padx=8)

#         ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation).pack(side='left', padx=8)

#         # Step Text
#         self.step_text = tk.StringVar()
#         self.step_label = ttk.Label(root, textvariable=self.step_text, font=("Arial", 14), anchor="w")
#         self.step_label.pack(fill='x', padx=10)

#         # Horizontal Split Frame for Output and Graph
#         main_frame = ttk.Frame(root)
#         main_frame.pack(fill='both', expand=True, padx=10, pady=10)

#         # Left: Output Text
#         left_frame = ttk.Frame(main_frame)
#         left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))

#         self.output_text = tk.Text(left_frame, height=20, font=("Arial", 12))
#         self.output_text.pack(fill='both', expand=True)

#         # Right: Graph
#         right_frame = ttk.Frame(main_frame)
#         right_frame.pack(side='right', fill='both', expand=True)

#         self.figure, self.ax = plt.subplots(figsize=(6, 5))
#         self.canvas = FigureCanvasTkAgg(self.figure, master=right_frame)
#         self.canvas.get_tk_widget().pack(fill='both', expand=True)

#     def run_simulation(self):
#         try:
#             pages_input = self.pages_entry.get().strip()
#             frames_input = self.frames_entry.get().strip()

#             if not pages_input or not frames_input:
#                 raise ValueError("Both pages and frames must be provided.")

#             self.pages = list(map(int, pages_input.split()))
#             num_frames = int(frames_input)

#             if num_frames <= 0:
#                 raise ValueError("Number of frames must be greater than 0.")

#             algorithm = self.algorithm_var.get()

#             if algorithm == "LRU":
#                 self.steps, faults, self.memory_states = self.simulate_lru(self.pages, num_frames)
#             elif algorithm == "FIFO":
#                 self.steps, faults, self.memory_states = self.simulate_fifo(self.pages, num_frames)
#             elif algorithm == "Optimal":
#                 self.steps, faults, self.memory_states = self.simulate_optimal(self.pages, num_frames)
#             elif algorithm == "LFU":
#                 self.steps, faults, self.memory_states = self.simulate_lfu(self.pages, num_frames)
#             elif algorithm == "MFU":
#                 self.steps, faults, self.memory_states = self.simulate_mfu(self.pages, num_frames)

#             self.output_text.delete(1.0, tk.END)
#             self.output_text.insert(tk.END, f"Total Page Faults: {faults}\n")

#             self.current_step = 0
#             self.animate_steps()
#         except ValueError as ve:
#             messagebox.showerror("Input Error", str(ve))
#         except Exception as e:
#             messagebox.showerror("Error", f"Unexpected error:\n{e}")

#     def animate_steps(self):
#      if self.current_step >= len(self.memory_states):
#         return

#      memory, page, step_type = self.memory_states[self.current_step]
#      self.ax.clear()

#      colors = []
#      labels = []

#     # Mark each bar individually (Hit -> green, Fault -> red for the current page)
#      for i, val in enumerate(memory):
#         if val == page:
#             if step_type == 'Hit':
#                 colors.append('#90ee90')  # light green
#                 labels.append('Hit')
#             else:
#                 colors.append('#f08080')  # light red
#                 labels.append('Page Fault')
#         else:
#             colors.append('#90ee90')  # default to green for old pages
#             labels.append('Hit')      # they are not triggering faults now

#     # Plot bars
#      bars = self.ax.barh(range(len(memory)), memory, color=colors)

#     # Add values on top of bars
#      for bar, val in zip(bars, memory):
#         self.ax.text(bar.get_x() + bar.get_width()/2.0, bar.get_height()/2.0,
#                      f'{val}', ha='center', va='center', fontsize=12, color='black')

#     # Title with step info
#      self.ax.set_title(f"Step {self.current_step + 1}: Processing Page {page} ({step_type})")

#     # Legend
#      from matplotlib.patches import Patch
#      legend_elements = [
#         Patch(facecolor='#90ee90', edgecolor='black', label='Hit'),
#         Patch(facecolor='#f08080', edgecolor='black', label='Page Fault')
#     ]
#      self.ax.legend(handles=legend_elements, loc='upper right')

#      self.ax.set_xticks(range(len(memory)))
#      self.ax.set_xticklabels([f'Frame {i+1}' for i in range(len(memory))])
#      self.ax.set_yticks([])
#      self.canvas.draw()

#     # Update step info
#      step_text = self.steps[self.current_step]
#      self.output_text.insert(tk.END, step_text + "\n")
#      self.step_text.set(step_text)

#      self.current_step += 1
#      self.root.after(1000, self.animate_steps)



#     # ----------------- Algorithms -------------------

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 memory.remove(page)
#                 memory.append(page)
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory.pop(0)
#                     memory.append(page)
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         pointer = 0
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory[pointer] = page
#                     pointer = (pointer + 1) % num_frames
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_optimal(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     future_use = []
#                     for mem_page in memory:
#                         try:
#                             idx = pages[i+1:].index(mem_page)
#                         except ValueError:
#                             idx = float('inf')
#                         future_use.append(idx)
#                     replace_index = future_use.index(max(future_use))
#                     memory[replace_index] = page
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_lfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 freq[page] += 1
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     min_freq = min(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == min_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_mfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 freq[page] += 1
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     max_freq = max(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == max_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementSimulator(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.patches import Patch

# class PageReplacementSimulator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Page Replacement Visual Simulator")
#         self.root.geometry("1200x700")

#         self.pages = []
#         self.steps = []
#         self.memory_states = []
#         self.current_step = 0

#                 # Algorithm Description Mapping
#         self.algo_descriptions = {
#             "LRU": "LRU (Least Recently Used): Replaces the page that hasn't been used for the longest time.",
#             "FIFO": "FIFO (First-In-First-Out): Replaces the oldest loaded page in memory.",
#             "Optimal": "Optimal: Replaces the page that will not be used for the longest period in the future.",
#             "LFU": "LFU (Least Frequently Used): Replaces the page with the lowest access frequency.",
#             "MFU": "MFU (Most Frequently Used): Replaces the page with the highest access frequency.",
#         }

#         # 🆕 Algorithm Description Label (at the top)
#         self.algo_description_text = tk.StringVar()
#         ttk.Label(root, textvariable=self.algo_description_text,
#                   font=("Arial", 12, "italic"), foreground="blue",
#                   anchor="w", wraplength=1100, justify="left").pack(fill='x', padx=10, pady=(10, 0))


#         # Input Frame
#         input_frame = ttk.Frame(root)
#         input_frame.pack(fill='x', pady=20)

#         ttk.Label(input_frame, text="Pages (space-separated):").pack(side='left', padx=5)
#         self.pages_entry = ttk.Entry(input_frame, width=30)
#         self.pages_entry.pack(side='left', padx=8)

#         ttk.Label(input_frame, text="Frames:").pack(side='left', padx=8)
#         self.frames_entry = ttk.Entry(input_frame, width=5)
#         self.frames_entry.pack(side='left', padx=8)

#         ttk.Label(input_frame, text="Algorithm:").pack(side='left', padx=8)
#         self.algorithm_var = tk.StringVar(value="LRU")
#         algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var,
#                                   values=["LRU", "FIFO", "Optimal", "LFU", "MFU"],
#                                   state="readonly", width=20)
#         algo_combo.pack(side='left', padx=8)

#         ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation).pack(side='left', padx=8)

#         # Step Text
#         self.step_text = tk.StringVar()
#         self.step_label = ttk.Label(root, textvariable=self.step_text, font=("Arial", 14), anchor="w")
#         self.step_label.pack(fill='x', padx=10)

#         # Output and Graph
#         main_frame = ttk.Frame(root)
#         main_frame.pack(fill='both', expand=True, padx=10, pady=10)

#         # Left: Output
#         left_frame = ttk.Frame(main_frame)
#         left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))

#         self.output_text = tk.Text(left_frame, height=20, font=("Arial", 12))
#         self.output_text.pack(fill='both', expand=True)

#         # Right: Graph
#         right_frame = ttk.Frame(main_frame)
#         right_frame.pack(side='right', fill='both', expand=True)

#         self.figure, self.ax = plt.subplots(figsize=(6, 5))
#         self.canvas = FigureCanvasTkAgg(self.figure, master=right_frame)
#         self.canvas.get_tk_widget().pack(fill='both', expand=True)

#     def run_simulation(self):
#         try:
#             pages_input = self.pages_entry.get().strip()
#             frames_input = self.frames_entry.get().strip()

#             if not pages_input or not frames_input:
#                 raise ValueError("Both pages and frames must be provided.")

#             self.pages = list(map(int, pages_input.split()))
#             num_frames = int(frames_input)

#             if num_frames <= 0:
#                 raise ValueError("Number of frames must be greater than 0.")

#             algorithm = self.algorithm_var.get()

#             if algorithm == "LRU":
#                 self.steps, faults, self.memory_states = self.simulate_lru(self.pages, num_frames)
#             elif algorithm == "FIFO":
#                 self.steps, faults, self.memory_states = self.simulate_fifo(self.pages, num_frames)
#             elif algorithm == "Optimal":
#                 self.steps, faults, self.memory_states = self.simulate_optimal(self.pages, num_frames)
#             elif algorithm == "LFU":
#                 self.steps, faults, self.memory_states = self.simulate_lfu(self.pages, num_frames)
#             elif algorithm == "MFU":
#                 self.steps, faults, self.memory_states = self.simulate_mfu(self.pages, num_frames)

#             self.output_text.delete(1.0, tk.END)
#             self.output_text.insert(tk.END, f"Total Page Faults: {faults}\n")

#             self.current_step = 0
#             self.animate_steps()

#         except ValueError as ve:
#             messagebox.showerror("Input Error", str(ve))
#         except Exception as e:
#             messagebox.showerror("Error", f"Unexpected error:\n{e}")

#     def animate_steps(self):
#         if self.current_step >= len(self.memory_states):
#             return
#         self.draw_step()
#         self.current_step += 1
#         self.root.after(1000, self.animate_steps)  # 1000 ms = 1 second delay

#     def draw_step(self):
#         if not self.memory_states:
#             return

#         memory, page, step_type = self.memory_states[self.current_step]

#         self.ax.clear()

#         colors = []
#         for i, val in enumerate(memory):
#             if val == page and step_type == 'Fault' and i == len(memory) - 1:
#                 colors.append('lightcoral')
#             else:
#                 colors.append('lightgreen')

#         self.ax.barh(range(len(memory)), [1]*len(memory), color=colors, edgecolor='black', height=0.6)

#         for i, val in enumerate(memory):
#             self.ax.text(0.5, i, str(val), ha='center', va='center', fontsize=12, color='black')

#         self.ax.set_yticks(range(len(memory)))
#         self.ax.set_yticklabels([f'Frame {i+1}' for i in range(len(memory))])
#         self.ax.set_xticks([])
#         self.ax.set_xlim(0, 1)
#         self.ax.set_title(f"Step {self.current_step + 1}: Page {page} ({step_type})")

#         self.ax.legend(handles=[
#             Patch(facecolor='lightgreen', edgecolor='black', label='Hit'),
#             Patch(facecolor='lightcoral', edgecolor='black', label='Page Fault')
#         ], loc='upper right')

#         self.canvas.draw()

#         self.step_text.set(self.steps[self.current_step])
#         self.output_text.insert(tk.END, self.steps[self.current_step] + "\n")
#         self.output_text.see(tk.END)

#     # ----------------- Algorithms -------------------

#     def simulate_lru(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 memory.remove(page)
#                 memory.append(page)
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory.pop(0)
#                     memory.append(page)
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_fifo(self, pages, num_frames):
#         memory = []
#         pointer = 0
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     memory[pointer] = page
#                     pointer = (pointer + 1) % num_frames
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_optimal(self, pages, num_frames):
#         memory = []
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if not hit:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                 else:
#                     future_use = []
#                     for mem_page in memory:
#                         try:
#                             idx = pages[i+1:].index(mem_page)
#                         except ValueError:
#                             idx = float('inf')
#                         future_use.append(idx)
#                     replace_index = future_use.index(max(future_use))
#                     memory[replace_index] = page
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_lfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 freq[page] += 1
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     min_freq = min(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == min_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

#     def simulate_mfu(self, pages, num_frames):
#         memory = []
#         freq = {}
#         faults = 0
#         steps = []
#         states = []
#         for i, page in enumerate(pages):
#             hit = page in memory
#             if hit:
#                 freq[page] += 1
#             else:
#                 faults += 1
#                 if len(memory) < num_frames:
#                     memory.append(page)
#                     freq[page] = 1
#                 else:
#                     max_freq = max(freq[p] for p in memory)
#                     candidates = [p for p in memory if freq[p] == max_freq]
#                     to_replace = candidates[0]
#                     memory[memory.index(to_replace)] = page
#                     del freq[to_replace]
#                     freq[page] = 1
#             step_type = "Hit" if hit else "Fault"
#             steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
#             states.append((memory.copy(), page, step_type))
#         return steps, faults, states

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PageReplacementSimulator(root)
#     root.mainloop()






import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Patch

class PageReplacementSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Visual Simulator")
        self.root.geometry("1200x750")

        self.pages = []
        self.steps = []
        self.memory_states = []
        self.current_step = 0

        # Algorithm Descriptions
        self.algo_descriptions = {
            "LRU": "LRU (Least Recently Used): Replaces the page that hasn't been used for the longest time.",
            "FIFO": "FIFO (First-In-First-Out): Replaces the oldest loaded page in memory.",
            "Optimal": "Optimal: Replaces the page that will not be used for the longest period in the future.",
            "LFU": "LFU (Least Frequently Used): Replaces the page with the lowest access frequency.",
            "MFU": "MFU (Most Frequently Used): Replaces the page with the highest access frequency.",
        }

        # Algorithm Description Label
        self.algo_description_text = tk.StringVar()
        ttk.Label(root, textvariable=self.algo_description_text,
                  font=("Arial", 12, "italic"), foreground="blue",
                  anchor="w", wraplength=1100, justify="left").pack(fill='x', padx=10, pady=(10, 0))

        # Input Frame
        input_frame = ttk.Frame(root)
        input_frame.pack(fill='x', pady=10)

        ttk.Label(input_frame, text="Pages (space-separated):").pack(side='left', padx=5)
        self.pages_entry = ttk.Entry(input_frame, width=30)
        self.pages_entry.pack(side='left', padx=8)

        ttk.Label(input_frame, text="Frames:").pack(side='left', padx=8)
        self.frames_entry = ttk.Entry(input_frame, width=5)
        self.frames_entry.pack(side='left', padx=8)

        ttk.Label(input_frame, text="Algorithm:").pack(side='left', padx=8)
        self.algorithm_var = tk.StringVar(value="LRU")
        algo_combo = ttk.Combobox(input_frame, textvariable=self.algorithm_var,
                                  values=list(self.algo_descriptions.keys()),
                                  state="readonly", width=20)
        algo_combo.pack(side='left', padx=8)
        algo_combo.bind("<<ComboboxSelected>>", self.update_description)

        ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation).pack(side='left', padx=8)

        # Step Text
        self.step_text = tk.StringVar()
        self.step_label = ttk.Label(root, textvariable=self.step_text, font=("Arial", 14), anchor="w")
        self.step_label.pack(fill='x', padx=10)

        # Output and Graph
        main_frame = ttk.Frame(root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))

        self.output_text = tk.Text(left_frame, height=20, font=("Arial", 12))
        self.output_text.pack(fill='both', expand=True)

        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', expand=True)

        self.figure, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=right_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        # Set initial description
        self.update_description()

    def update_description(self, event=None):
        selected_algo = self.algorithm_var.get()
        description = self.algo_descriptions.get(selected_algo, "No description available.")
        self.algo_description_text.set(description)

    def run_simulation(self):
        try:
            pages_input = self.pages_entry.get().strip()
            frames_input = self.frames_entry.get().strip()

            if not pages_input or not frames_input:
                raise ValueError("Both pages and frames must be provided.")

            self.pages = list(map(int, pages_input.split()))
            num_frames = int(frames_input)

            if num_frames <= 0:
                raise ValueError("Number of frames must be greater than 0.")

            algorithm = self.algorithm_var.get()

            if algorithm == "LRU":
                self.steps, faults, self.memory_states = self.simulate_lru(self.pages, num_frames)
            elif algorithm == "FIFO":
                self.steps, faults, self.memory_states = self.simulate_fifo(self.pages, num_frames)
            elif algorithm == "Optimal":
                self.steps, faults, self.memory_states = self.simulate_optimal(self.pages, num_frames)
            elif algorithm == "LFU":
                self.steps, faults, self.memory_states = self.simulate_lfu(self.pages, num_frames)
            elif algorithm == "MFU":
                self.steps, faults, self.memory_states = self.simulate_mfu(self.pages, num_frames)

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Total Page Faults: {faults}\n")

            self.current_step = 0
            self.animate_steps()

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error:\n{e}")

    def animate_steps(self):
        if self.current_step >= len(self.memory_states):
            return
        self.draw_step()
        self.current_step += 1
        self.root.after(1000, self.animate_steps)

    def draw_step(self):
        if not self.memory_states:
            return

        memory, page, step_type = self.memory_states[self.current_step]

        self.ax.clear()

        colors = []
        for i, val in enumerate(memory):
            if val == page and step_type == 'Fault' and i == len(memory) - 1:
                colors.append('lightcoral')
            else:
                colors.append('lightgreen')

        self.ax.barh(range(len(memory)), [1]*len(memory), color=colors, edgecolor='black', height=0.6)

        for i, val in enumerate(memory):
            self.ax.text(2, i, str(val), ha='center', va='center', fontsize=12, color='black')

        self.ax.set_yticks(range(len(memory)))
        self.ax.set_yticklabels([f'Frame {i+1}' for i in range(len(memory))])
        self.ax.set_xticks([])
        self.ax.set_xlim(0, 1)
        self.ax.set_title(f"Step {self.current_step + 1}: Page {page} ({step_type})")

        self.ax.legend(handles=[
            Patch(facecolor='lightgreen', edgecolor='black', label='Hit'),
            Patch(facecolor='lightcoral', edgecolor='black', label='Page Fault')
        ], loc='upper right')

        self.canvas.draw()

        self.step_text.set(self.steps[self.current_step])
        self.output_text.insert(tk.END, self.steps[self.current_step] + "\n")
        self.output_text.see(tk.END)

    def simulate_lru(self, pages, num_frames):
        memory = []
        faults = 0
        steps = []
        states = []
        for i, page in enumerate(pages):
            hit = page in memory
            if hit:
                memory.remove(page)
                memory.append(page)
            else:
                faults += 1
                if len(memory) < num_frames:
                    memory.append(page)
                else:
                    memory.pop(0)
                    memory.append(page)
            step_type = "Hit" if hit else "Fault"
            steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
            states.append((memory.copy(), page, step_type))
        return steps, faults, states

    def simulate_fifo(self, pages, num_frames):
        memory = []
        pointer = 0
        faults = 0
        steps = []
        states = []
        for i, page in enumerate(pages):
            hit = page in memory
            if not hit:
                faults += 1
                if len(memory) < num_frames:
                    memory.append(page)
                else:
                    memory[pointer] = page
                    pointer = (pointer + 1) % num_frames
            step_type = "Hit" if hit else "Fault"
            steps.append(f"Step {i+1} - Page: {page} -> {step_type}, Memory: {memory}")
            states.append((memory.copy(), page, step_type))
        return steps, faults, states

    def simulate_optimal(self, pages, num_frames):
        # Placeholder for actual Optimal simulation
        return [], 0, []

    def simulate_lfu(self, pages, num_frames):
        # Placeholder for actual LFU simulation
        return [], 0, []

    def simulate_mfu(self, pages, num_frames):
        # Placeholder for actual MFU simulation
        return [], 0, []

if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementSimulator(root)
    root.mainloop()

