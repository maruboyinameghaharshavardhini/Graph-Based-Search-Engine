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
            return True
        return False

    def add_link(self, source_node, destination_node):
        if source_node in self.graph and destination_node in self.graph:
            if destination_node not in self.graph[source_node]:
                self.graph[source_node].append(destination_node)
                return True
        return False

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
        self.root.title("Live Neon Graph Search Engine")
        self.root.geometry("1200x700")

        self.graph_data = Graph()
        self.node_coords = {}  # Stores {node_id: (x, y)}
        self.edge_particles = [] # Particles for animation

        # ================= LEFT GRAPH AREA =================
        self.canvas = tk.Canvas(root, bg="#050510", width=800, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # ================= RIGHT CONTROL PANEL =================
        self.panel = tk.Frame(root, bg="#111122", width=400)
        self.panel.pack(side="right", fill="y")

        tk.Label(
            self.panel, text="Neon Graph Engine",
            font=("Arial", 20, "bold"), fg="#00ffff", bg="#111122"
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

        self.result_box = tk.Listbox(
            self.panel, width=35, height=8, bg="#000000",
            fg="#00ffff", font=("Consolas", 11), bd=0
        )
        self.result_box.pack(pady=15)

        # Start animation loop
        self.animate_particles()

    def create_oval_entry(self, placeholder):
        frame = tk.Frame(self.panel, bg="#111122")
        frame.pack(pady=5)
        c = tk.Canvas(frame, width=300, height=40, bg="#111122", highlightthickness=0)
        c.pack()
        c.create_oval(5, 5, 295, 35, fill="#000000", outline="#00ffff", width=1)
        entry = tk.Entry(frame, bd=0, font=("Consolas", 10), bg="#000000",
                         fg="#00ffff", insertbackground="#00ffff", justify="center")
        entry.place(x=30, y=10, width=240)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, placeholder))
        return entry

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def create_button(self, text, command):
        tk.Button(
            self.panel, text=text, command=command, font=("Arial", 10, "bold"),
            bg="#00ffff", fg="black", bd=0, width=20, pady=5
        ).pack(pady=5)

    # ==========================
    # GRAPH LOGIC & DRAWING
    # ==========================
    def add_node(self):
        node_id = self.node_entry.get()
        desc = self.description_entry.get()

        if not node_id or node_id == "Node ID":
            return

        if self.graph_data.add_node(node_id, desc):
            # Generate random position on canvas
            x = random.randint(50, 750)
            y = random.randint(50, 650)
            self.node_coords[node_id] = (x, y)
            
            self.draw_graph() # Redraw to show new node
        else:
            messagebox.showwarning("Warning", "Node already exists!")

    def add_link(self):
        u = self.source_entry.get()
        v = self.destination_entry.get()

        if u in self.node_coords and v in self.node_coords:
            if self.graph_data.add_link(u, v):
                # Add a particle for this specific link
                x1, y1 = self.node_coords[u]
                x2, y2 = self.node_coords[v]
                color = random.choice(["#00ffff", "#ff00ff", "#00ff88"])
                
                self.edge_particles.append({
                    "coords": (x1, y1, x2, y2),
                    "t": 0.0,
                    "speed": random.uniform(0.01, 0.03),
                    "color": color
                })
                self.draw_graph()
            else:
                messagebox.showwarning("Warning", "Link already exists or invalid!")
        else:
            messagebox.showerror("Error", "Both nodes must exist first!")

    def draw_graph(self):
        """Clears and redraws all lines and nodes based on actual data"""
        self.canvas.delete("graph_element")

        # 1. Draw Links (Edges) first so they are behind nodes
        for node_id, neighbors in self.graph_data.graph.items():
            x1, y1 = self.node_coords[node_id]
            for neighbor in neighbors:
                x2, y2 = self.node_coords[neighbor]
                self.canvas.create_line(
                    x1, y1, x2, y2, fill="#222244", width=2, 
                    tags="graph_element", capstyle=tk.ROUND
                )

        # 2. Draw Nodes
        for node_id, (x, y) in self.node_coords.items():
            # Outer Glow
            self.canvas.create_oval(
                x-12, y-12, x+12, y+12, outline="#00ffff", 
                width=1, tags="graph_element"
            )
            # Main Node
            self.canvas.create_oval(
                x-8, y-8, x+8, y+8, fill="#000000", 
                outline="#00ffff", width=2, tags="graph_element"
            )
            # Node Label
            self.canvas.create_text(
                x, y+20, text=node_id, fill="#ffffff", 
                font=("Arial", 9, "bold"), tags="graph_element"
            )

    def animate_particles(self):
        self.canvas.delete("particle")

        for p in self.edge_particles:
            x1, y1, x2, y2 = p["coords"]
            p["t"] += p["speed"]
            if p["t"] > 1: p["t"] = 0

            # Linear Interpolation
            cur_x = x1 + (x2 - x1) * p["t"]
            cur_y = y1 + (y2 - y1) * p["t"]

            self.canvas.create_oval(
                cur_x-3, cur_y-3, cur_x+3, cur_y+3,
                fill=p["color"], outline="", tags="particle"
            )

        self.root.after(30, self.animate_particles)

    def search(self):
        query = self.query_entry.get()
        self.result_box.delete(0, tk.END)
        matches = self.graph_data.search(query)

        if matches:
            for m in matches:
                self.result_box.insert(tk.END, f"Found: {m}")
                # Highlight matching node on canvas
                x, y = self.node_coords[m]
                self.canvas.create_oval(
                    x-15, y-15, x+15, y+15, outline="#ff00ff", 
                    width=2, tags="particle" # tags particle so it clears automatically
                )
        else:
            self.result_box.insert(tk.END, "No matching nodes")

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchEngineApp(root)
    root.mainloop()
