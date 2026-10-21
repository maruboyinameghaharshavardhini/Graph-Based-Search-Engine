# Graph-Based-Search-Engine
**A Python-Based Search Engine Using Graph Data Structures and BFS**

## 1. Project Overview

The Graph Based Search Engine is a Python application that searches for relevant information using graph data structures and the Breadth-First Search (BFS) algorithm. It represents information as nodes and relationships as edges.

The application allows users to enter node IDs and descriptions, connect nodes using source and destination IDs, and search for information using a query term. A Tkinter graphical user interface (GUI) provides an interactive way to use the search engine.

## 2. Design Theme

**Theme:** Modern Graph Explorer

- Background: Dark blue or gradient-inspired theme.
- Colors: Blue, cyan, purple, and complementary accents.
- Font: Segoe UI.
- Input fields: Node ID, Node Description, Source Node, Destination Node, and Query Term.
- Buttons: Add Node, Add Link, and Search.
- Results section: Displays matching node IDs and descriptions.

## 3. Application Pages and Sections

The application can be organized into five logical sections within the Tkinter window.

### Page 1: Main Dashboard
- Project title.
- Main interface.
- Access to node creation, connections, and search.

### Page 2: Add Node
- Node ID input.
- Node Description input.
- Add Node button.

### Page 3: Manage Connections
- Source Node input.
- Destination Node input.
- Add Link button.

### Page 4: Search
- Query Term input.
- Search button.
- BFS-based traversal.

### Page 5: Search Results
- Matching Node ID.
- Matching Node Description.
- No-results message when applicable.

*These are logical sections, not necessarily five separate windows or pages in the current implementation.*

## 4. Authentication

The current application is designed as a local Python desktop application.

- Login: Not required for the basic version.
- Registration: Not included in the basic version.
- User accounts: Can be added in a future version.
- Password protection: Can be introduced if authentication is implemented.

## 5. Technical Requirements

### Hardware
- Computer or laptop.
- Minimum 4 GB RAM recommended.
- Sufficient free storage for Python and project files.

### Software
- Python 3.
- Tkinter.
- Python IDLE or another Python editor.
- Git and GitHub for version control and project hosting.

### Technologies
- Python.
- Graph Data Structures.
- Adjacency List.
- Breadth-First Search (BFS).
- Queue and Visited Set.
- Tkinter GUI.

## 6. Example Project File Structure

Use the following example file names for your repository. Change them to match your actual files.

```text
Graph-Based-Search-Engine/
│
├── graph_based_search_engine.py
├── graph_search.py
├── dataset/
│   └── sample_dataset.csv
├── assets/
│   └── screenshots/
│       └── search_engine_output.png
├── README.md
├── requirements.txt
└── LICENSE
```

### File Descriptions

- **`graph_based_search_engine.py`** – Main Python application and Tkinter graphical interface.
- **`graph_search.py`** – Graph implementation, node and edge management, and BFS search logic.
- **`dataset/sample_dataset.csv`** – Example dataset used by the application, if CSV data is supported.
- **`assets/screenshots/search_engine_output.png`** – Screenshot demonstrating the application interface.
- **`README.md`** – Project overview, features, setup, and documentation.
- **`requirements.txt`** – Python package dependencies, if any external packages are used.
- **`LICENSE`** – Defines the permissions for others to reuse the project.

**Important:** These are suggested names. If your code is currently in one Python file, you can use just `graph_based_search_engine.py` and `README.md`, together with any actual dataset or supporting files.

## 7. Core Features

- Add nodes with unique IDs and descriptions.
- Connect nodes using source and destination IDs.
- Store graph relationships using an adjacency list.
- Search descriptions using a query term.
- Traverse connected nodes using BFS.
- Display matching results in the Tkinter interface.
- Handle empty queries and invalid connections appropriately.

## 8. Development Process

1. **Requirement Analysis:** Identify the search requirements and user inputs.
2. **Graph Development:** Implement nodes, edges, and adjacency lists.
3. **Algorithm Development:** Implement BFS using a queue and visited set.
4. **GUI Development:** Build the interface with Tkinter.
5. **Integration:** Connect the GUI with the graph and search logic.
6. **Testing:** Test node creation, links, search results, and invalid inputs.
7. **Documentation:** Prepare the README and upload the source code to GitHub.

## 9. System Workflow

User Input → Tkinter Interface → Graph Data Structure → BFS Algorithm → Matching Results → Display Results

## 10. Algorithm and Complexity

Breadth-First Search traverses a graph level by level.

- Time complexity: \(O(V+E)\) for graph traversal, where \(V\) is the number of vertices and \(E\) is the number of edges.
- Additional space complexity: \(O(V)\) for the queue and visited set.

The overall search time also depends on the length of the descriptions being checked.

## 11. Installation and Execution

1. Install Python 3.
2. Download or clone the repository.
3. Open the project folder in Python IDLE.
4. Open `graph_based_search_engine.py`, or whichever file contains your main application.
5. Run the Python file.
6. Enter node details and create connections.
7. Enter a query term and view the search results.

## 12. Testing

| Test Case | Expected Result |
|---|---|
| Add a valid node | Node is added |
| Create a valid link | Connection is established |
| Search an existing keyword | Matching nodes are displayed |
| Search an unknown keyword | No-results message is displayed |
| Enter an invalid node ID | Invalid input is handled |
| Search a graph containing cycles | Visited tracking prevents repeated traversal |

## 13. Future Enhancements

- Voice-based search using speech recognition.
- Visual representation of nodes and edges.
- Improved keyword matching and relevance ranking.
- Persistent storage of graph data.
- Support for multiple search terms.
- Optional login and registration.
- Search history and saved queries.

## 14. Learning Outcomes

This project demonstrates practical knowledge of Python programming, graph data structures, BFS traversal, adjacency lists, queues, visited sets, Tkinter GUI development, and basic software testing.

## 15. Conclusion

The Graph Based Search Engine demonstrates how graph data structures and BFS can be used to search connected information. It combines algorithmic concepts with a graphical interface to provide a practical learning project in Python and Data Structures and Algorithms.

## Author

**Megha Harsha Vardhini**

Data Science Student | Python Learner | Exploring Data Structures and Algorithms

## License

Add an appropriate open-source license if you want others to reuse or modify this project.
