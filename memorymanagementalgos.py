import matplotlib.pyplot as plt
import random
from matplotlib.patches import FancyBboxPatch
import tkinter as tk
from tkinter import messagebox

# ---------------- Memory Allocation Classes ---------------- #

class MemoryBlock:
    def __init__(self, size, id=None, origin_id=None):
        self.size = size
        self.id = id  # Process ID; None means free
        self.origin_id = origin_id  # Original memory block index

def generate_distinct_colors(n):
    random.seed(42)
    return [plt.cm.Set3(i % 12) for i in range(n)]

def draw_3d_block(ax, x, width, color):
    box = FancyBboxPatch((x, -0.25), width, 0.5,
                         boxstyle="round,pad=0.02",
                         ec="black", fc=color, linewidth=1.5)
    ax.add_patch(box)

def visualize_memory_live(ax, memory, title="Memory State"):
    ax.clear()

    sizes = [block.size for block in memory]
    origins = [block.origin_id for block in memory]
    origin_colors = generate_distinct_colors(len(set(origins)))
    origin_color_map = {oid: origin_colors[i] for i, oid in enumerate(sorted(set(origins)))}

    labels = []
    colors = []

    for block in memory:
        base_color = origin_color_map[block.origin_id]
        colors.append(base_color)
        if block.id is None:
            labels.append(f"Free\n{block.size}K")
        else:
            labels.append(f"P{block.id}\n{block.size}K")

    ax.set_xlim(0, sum(sizes))
    ax.set_ylim(-1, 1)
    ax.axis('off')

    start = 0
    for size, color, label in zip(sizes, colors, labels):
        draw_3d_block(ax, start, size, color)
        ax.text(start + size / 2, 0, label, va='center', ha='center', fontsize=10, fontweight='bold')
        start += size

    # Draw group labels
    start = 0
    for oid in sorted(set(origins)):
        group_blocks = [b for b in memory if b.origin_id == oid]
        group_size = sum(b.size for b in group_blocks)
        ax.text(start + group_size / 2, 0.6, f"Block {oid + 1}", ha='center', fontsize=11, fontweight='bold', color='darkslategray')
        ax.axvline(x=start, color='gray', linestyle='dashed', linewidth=1)
        start += group_size

    ax.set_title(title, fontsize=15, fontweight='bold', pad=20)
    ax.figure.text(0.5, 0.01, "First Fit Allocation", ha='center', fontsize=12, style='italic', color='gray')  # Footer added
    plt.draw()
    plt.pause(1.2)

def first_fit_dynamic_live(memory, processes):
    fig, ax = plt.subplots(figsize=(18, 6))  # Large figure

    try:
        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')  # Maximize (Windows)
    except:
        pass  # Safe fallback for non-Windows

    plt.ion()  # Interactive mode on

    for pid, psize in enumerate(processes):
        allocated = False
        for i, block in enumerate(memory):
            if block.id is None and block.size >= psize:
                remaining_size = block.size - psize
                block.id = pid
                block.size = psize
                if remaining_size > 0:
                    memory.insert(i + 1, MemoryBlock(remaining_size, None, block.origin_id))
                allocated = True
                break

        visualize_memory_live(ax, memory, f"After Allocating P{pid} ({psize}K)")

    plt.ioff()
    plt.show()

def run_first_fit_visualization(memory_sizes, process_sizes):
    memory = [MemoryBlock(size, origin_id=i) for i, size in enumerate(memory_sizes)]
    first_fit_dynamic_live(memory, process_sizes)

# ---------------- Tkinter UI Setup ---------------- #

def start_visualization():
    try:
        mem_input = mem_entry.get()
        proc_input = proc_entry.get()
        memory_sizes = list(map(int, mem_input.strip().split()))
        process_sizes = list(map(int, proc_input.strip().split()))

        if not memory_sizes or not process_sizes:
            raise ValueError

        run_first_fit_visualization(memory_sizes, process_sizes)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter space-separated integers for both fields.")

# Create main window
root = tk.Tk()
root.title("First Fit Memory Allocation Visualizer")
root.geometry("500x250")
root.configure(bg="#f4f4f4")

# Labels
tk.Label(root, text="Enter Memory Block Sizes:", bg="#f4f4f4", font=("Arial", 11)).pack(pady=(20, 5))
mem_entry = tk.Entry(root, font=("Arial", 12), width=40)
mem_entry.pack(pady=(0, 10))

tk.Label(root, text="Enter Process Sizes:", bg="#f4f4f4", font=("Arial", 11)).pack()
proc_entry = tk.Entry(root, font=("Arial", 12), width=40)
proc_entry.pack(pady=(0, 15))

# Button
tk.Button(root, text="Visualize Allocation", command=start_visualization,
          bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack()

root.mainloop()
