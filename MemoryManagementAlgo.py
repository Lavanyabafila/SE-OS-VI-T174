import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import random

# ---------------- Memory Block Class ---------------- #
class MemoryBlock:
    def __init__(self, size, id=None, origin_id=None):
        self.size = size
        self.id = id
        self.origin_id = origin_id

# ---------------- Utility Functions ---------------- #
def generate_distinct_colors(n):
    random.seed(42)
    return [plt.cm.Set3(i % 12) for i in range(n)]

def draw_3d_block(ax, x, width, color):
    box = FancyBboxPatch((x, -0.25), width, 0.5,
                         boxstyle="round,pad=0.02",
                         ec="black", fc=color, linewidth=1.5)
    ax.add_patch(box)

def visualize_memory_live(ax, memory, title, footer):
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
    start = 0
    for oid in sorted(set(origins)):
        group_blocks = [b for b in memory if b.origin_id == oid]
        group_size = sum(b.size for b in group_blocks)
        ax.text(start + group_size / 2, 0.6, f"Block {oid + 1}", ha='center', fontsize=11, fontweight='bold', color='darkslategray')
        ax.axvline(x=start, color='gray', linestyle='dashed', linewidth=1)
        start += group_size
    ax.set_title(title, fontsize=15, fontweight='bold', pad=20)
    ax.figure.text(0.5, 0.01, footer, ha='center', fontsize=12, style='italic', color='gray')
    plt.draw()
    plt.pause(1.2)

# ---------------- Algorithms ---------------- #
def run_allocation(memory_sizes, process_sizes, algorithm, page_size=None):
    memory = [MemoryBlock(size, origin_id=i) for i, size in enumerate(memory_sizes)]
    fig, ax = plt.subplots(figsize=(18, 6))
    try:
        plt.get_current_fig_manager().window.state('zoomed')
    except:
        pass
    plt.ion()

    for pid, psize in enumerate(process_sizes):
        if algorithm == "First Fit":
            allocated = False
            for i, block in enumerate(memory):
                if block.id is None and block.size >= psize:
                    remaining = block.size - psize
                    block.id = pid
                    block.size = psize
                    if remaining > 0:
                        memory.insert(i + 1, MemoryBlock(remaining, None, block.origin_id))
                    break
        elif algorithm == "Best Fit":
            best_index = -1
            min_diff = float('inf')
            for i, block in enumerate(memory):
                if block.id is None and block.size >= psize and (block.size - psize) < min_diff:
                    best_index = i
                    min_diff = block.size - psize
            if best_index != -1:
                block = memory[best_index]
                remaining = block.size - psize
                block.id = pid
                block.size = psize
                if remaining > 0:
                    memory.insert(best_index + 1, MemoryBlock(remaining, None, block.origin_id))
        elif algorithm == "Worst Fit":
            worst_index = -1
            max_diff = -1
            for i, block in enumerate(memory):
                if block.id is None and block.size >= psize and (block.size - psize) > max_diff:
                    worst_index = i
                    max_diff = block.size - psize
            if worst_index != -1:
                block = memory[worst_index]
                remaining = block.size - psize
                block.id = pid
                block.size = psize
                if remaining > 0:
                    memory.insert(worst_index + 1, MemoryBlock(remaining, None, block.origin_id))
        elif algorithm == "Paging":
            if page_size is None or page_size <= 0:
                messagebox.showerror("Error", "Invalid page size for Paging.")
                return
            pages = (psize + page_size - 1) // page_size
            for _ in range(pages):
                for i, block in enumerate(memory):
                    if block.id is None and block.size >= page_size:
                        remaining = block.size - page_size
                        block.id = pid
                        block.size = page_size
                        if remaining > 0:
                            memory.insert(i + 1, MemoryBlock(remaining, None, block.origin_id))
                        break
        elif algorithm == "Segmentation":
            segments = [psize // 2, psize // 2]
            for seg in segments:
                for i, block in enumerate(memory):
                    if block.id is None and block.size >= seg:
                        remaining = block.size - seg
                        block.id = pid
                        block.size = seg
                        if remaining > 0:
                            memory.insert(i + 1, MemoryBlock(remaining, None, block.origin_id))
                        break

        visualize_memory_live(ax, memory, f"{algorithm}: Allocated P{pid} ({psize}K)", f"{algorithm} Allocation")

    plt.ioff()
    plt.show()

# ---------------- Tkinter UI ---------------- #
def start_visualization():
    try:
        algo = algo_var.get()
        memory_sizes = list(map(int, mem_entry.get().strip().split()))
        process_sizes = list(map(int, proc_entry.get().strip().split()))
        page_size = None
        if algo == "Paging":
            page_size = int(page_entry.get())
        if not memory_sizes or not process_sizes:
            raise ValueError
        run_allocation(memory_sizes, process_sizes, algo, page_size)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter space-separated integers only.")

def on_algo_change(event=None):
    if algo_var.get() == "Paging":
        page_frame.pack(pady=(5, 10))
    else:
        page_frame.pack_forget()

root = tk.Tk()
root.title("Memory Allocation Visualizer")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

algo_var = tk.StringVar()
tk.Label(root, text="Select Algorithm:", font=("Segoe UI", 12), bg="#f0f0f0").pack(pady=(10, 5))
algo_menu = tk.OptionMenu(root, algo_var, "First Fit", "Best Fit", "Worst Fit", "Paging", "Segmentation", command=on_algo_change)
algo_menu.config(font=("Segoe UI", 12), width=20)
algo_menu.pack()

tk.Label(root, text="Enter Memory Block Sizes (space-separated):", bg="#f0f0f0", font=("Segoe UI", 11)).pack(pady=(15, 5))
mem_entry = tk.Entry(root, font=("Segoe UI", 12), width=50)
mem_entry.pack()

tk.Label(root, text="Enter Process Sizes (space-separated):", bg="#f0f0f0", font=("Segoe UI", 11)).pack(pady=(10, 5))
proc_entry = tk.Entry(root, font=("Segoe UI", 12), width=50)
proc_entry.pack()

page_frame = tk.Frame(root, bg="#f0f0f0")
tk.Label(page_frame, text="Enter Page Size (for Paging only):", bg="#f0f0f0", font=("Segoe UI", 11)).pack()
page_entry = tk.Entry(page_frame, font=("Segoe UI", 12), width=30)
page_entry.pack()

tk.Button(root, text="Visualize Allocation", font=("Segoe UI", 12, "bold"),
          bg="#4CAF50", fg="white", command=start_visualization).pack(pady=(25, 15))

algo_var.set("First Fit")
on_algo_change()

root.mainloop()
