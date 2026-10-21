import tkinter as tk
from tkinter import messagebox
from collections import deque
import random


# ==========================
# GRAPH DATA STRUCTURE
# ==========================
class Graph:
    def __init__(self):
        self.graph = {}
        self.description = {}

    def add_node(self, node_id, description):
        if node_id not in self.graph:
            self.graph[node_id] = []
            self.description[node_id] = description

    def add_link(self, source_node, destination_node):
        if source_node in self.graph and destination_node in self.graph:
            if destination_node not in self.graph[source_node]:
                self.graph[source_node].append(destination_node)

    def search(self, query_term):
        visited = set()
        queue = deque()
        matches = []

        for node in self.graph:
            if node not in visited:
                queue.append(node)
                visited.add(node)

                while queue:
                    current = queue.popleft()
                    if query_term.lower() in self.description[current].lower():
                        matches.append(current)

                    for neighbor in self.graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

        return matches


# ==========================
# GUI APPLICATION
# ==========================
class SearchEngineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Split Neon Graph Search Engine")
        self.root.geometry("1200x700")

        self.graph_data = Graph()

        # ================= LEFT GRAPH AREA =================
        self.canvas = tk.Canvas(root, bg="#050510", width=800, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # ================= RIGHT CONTROL PANEL =================
        self.panel = tk.Frame(root, bg="#111122", width=400)
        self.panel.pack(side="right", fill="y")

        tk.Label(
            self.panel,
            text="Neon Graph Engine",
            font=("Arial", 20, "bold"),
            fg="#00ffff",
            bg="#111122"
        ).pack(pady=15)

        # Oval Inputs
        self.node_entry = self.create_oval_entry("Node ID")
        self.description_entry = self.create_oval_entry("Node Description")
        self.source_entry = self.create_oval_entry("Source Node")
        self.destination_entry = self.create_oval_entry("Destination Node")
        self.query_entry = self.create_oval_entry("Query Term")

        self.create_button("Add Node", self.add_node)
        self.create_button("Add Link", self.add_link)
        self.create_button("Search", self.search)

        # Result box
        self.result_box = tk.Listbox(
            self.panel,
            width=35,
            height=8,
            bg="#000000",
            fg="#00ffff",
            font=("Consolas", 11),
            bd=0
        )
        self.result_box.pack(pady=15)

        # Graph storage
        self.node_positions = {}
        self.edge_particles = []

        # Background network
        self.create_background_network()
        self.animate_particles()

    # ==========================
    # OVAL ENTRY FIELD
    # ==========================
    def create_oval_entry(self, placeholder):
        frame = tk.Frame(self.panel, bg="#111122")
        frame.pack(pady=8)

        c = tk.Canvas(frame, width=320, height=45, bg="#111122", highlightthickness=0)
        c.pack()

        c.create_oval(5, 5, 315, 45, fill="#000000", outline="#00ffff", width=2)

        entry = tk.Entry(
            frame,
            bd=0,
            font=("Consolas", 11),
            bg="#000000",
            fg="#00ffff",
            insertbackground="#00ffff",
            justify="center"
        )

        entry.place(x=40, y=12, width=240)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, placeholder))

        return entry

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    # ==========================
    # BUTTON
    # ==========================
    def create_button(self, text, command):
        tk.Button(
            self.panel,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            bg="#00ffff",
            fg="black",
            bd=0,
            padx=10,
            pady=5
        ).pack(pady=5)

    # ==========================
    # BACKGROUND NETWORK
    # ==========================
    def create_background_network(self):
        width = 800
        height = 700

        self.bg_nodes = []
        self.bg_edges = []

        for _ in range(30):
            x = random.randint(50, width - 50)
            y = random.randint(50, height - 50)
            self.bg_nodes.append((x, y))

        for i in range(len(self.bg_nodes)):
            for j in range(i + 1, len(self.bg_nodes)):
                if random.random() < 0.08:
                    x1, y1 = self.bg_nodes[i]
                    x2, y2 = self.bg_nodes[j]
                    color = random.choice(
                        ["#00ffff", "#ff00ff", "#00ff88", "#ff8800"]
                    )
                    self.canvas.create_line(x1, y1, x2, y2, fill=color)
                    self.bg_edges.append((x1, y1, x2, y2, color))

        for (x, y) in self.bg_nodes:
            self.canvas.create_oval(
                x - 5, y - 5, x + 5, y + 5,
                fill="#ffffff",
                outline="#00ffff"
            )

        # Create particles
        for edge in self.bg_edges:
            self.edge_particles.append({
                "edge": edge,
                "t": random.random(),
                "speed": random.uniform(0.01, 0.03)
            })

    # ==========================
    # PARTICLE ANIMATION
    # ==========================
    def animate_particles(self):
        self.canvas.delete("particle")

        for p in self.edge_particles:
            x1, y1, x2, y2, color = p["edge"]

            p["t"] += p["speed"]
            if p["t"] > 1:
                p["t"] = 0

            x = x1 + (x2 - x1) * p["t"]
            y = y1 + (y2 - y1) * p["t"]

            self.canvas.create_oval(
                x - 3, y - 3, x + 3, y + 3,
                fill=color,
                outline="",
                tags="particle"
            )

        self.root.after(30, self.animate_particles)

    # ==========================
    # FUNCTIONAL METHODS
    # ==========================
    def add_node(self):
        node_id = self.node_entry.get()
        description = self.description_entry.get()

        if node_id and description:
            self.graph_data.add_node(node_id, description)
            messagebox.showinfo("Success", "Node Added")

    def add_link(self):
        source = self.source_entry.get()
        dest = self.destination_entry.get()

        if source and dest:
            self.graph_data.add_link(source, dest)
            messagebox.showinfo("Success", "Link Added")

    def search(self):
        query = self.query_entry.get()
        self.result_box.delete(0, tk.END)

        matches = self.graph_data.search(query)

        if matches:
            for m in matches:
                self.result_box.insert(tk.END, m)
        else:
            self.result_box.insert(tk.END, "No matching nodes")


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchEngineApp(root)
    root.mainloop()
