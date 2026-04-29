# Automated Deadlock Detection Tool

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-FF4B4B.svg)](https://streamlit.io/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.6-green.svg)](https://networkx.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An interactive **Operating Systems course project** that demonstrates real-time deadlock detection using **Wait-For Graphs**, **Cycle Detection**, and **Banker's Algorithm** with a professional Streamlit dashboard.

---

## About

**Automated Deadlock Detection Tool** is an interactive dashboard built for Operating Systems coursework. It implements core OS concepts like Wait-For Graphs, cycle detection for deadlocks, Banker's Algorithm safety checks, and provides 6 practical resolution strategies. The professional Streamlit interface allows real-time analysis, graph visualization, CSV import, and downloadable reports.

## Features

- **Real-time Deadlock Detection** — Identifies circular waits in resource allocation graphs using NetworkX cycle detection.
- **Interactive Visualization** — Renders Wait-For Graphs with red edges highlighting deadlock cycles.
- **Banker's Safe State Check** — Simplified heuristic to determine if the system is in a safe state.
- **6 Resolution Strategies** — Suggests actionable solutions when deadlocks are detected.
- **CSV Data Upload** — Import process allocation and request data from CSV files.
- **Sample Data** — Built-in deadlock and safe-state examples for instant testing.
- **Downloadable Reports** — Export analysis results as text reports.
- **KPI Dashboard** — View key metrics (process count, resource count, deadlock status, safety status) at a glance.

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| UI Framework | Streamlit 1.36+ |
| Graph Processing | NetworkX 3.6 |
| Visualization | Matplotlib 3.10 |
| Data Handling | Pandas 3.0 |

---

## Project Structure

```
OS PROJECT/
├── README.md                      # Project documentation (this file)
├── TODO.md                        # Development task tracker
├── deadlock_detector/
│   ├── app.py                     # Main Streamlit application
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # Subfolder documentation
│   ├── logic/
│   │   ├── graph.py               # Wait-For Graph construction
│   │   ├── detection.py           # Deadlock cycle detection
│   │   ├── resolution.py          # Resolution strategy suggestions
│   │   └── bankers.py             # Banker's Algorithm (safe-state check)
│   └── utils/
│       └── sample_data.py         # Sample deadlock and safe-state data
```

---

## Getting Started

### Prerequisites

- Python 3.12 or higher installed on your system.
- Windows PowerShell or Command Prompt.

### Installation & Setup

1. **Navigate to the project directory:**
   ```cmd
   cd "c:/Users/mohit kumar/OneDrive/Desktop/OS PROJECT/deadlock_detector"
   ```

2. **Create a virtual environment:**
   ```cmd
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```cmd
   venv\Scripts\activate
   ```
   *(Your prompt should now show `(venv)`)*

4. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app:**
   ```cmd
   python -m streamlit run app.py
   ```
   The dashboard will automatically open in your browser at **`http://localhost:8501`**.

### Quick Re-run (after initial setup)

```cmd
cd "c:/Users/mohit kumar/OneDrive/Desktop/OS PROJECT/deadlock_detector"
venv\Scripts\activate
python -m streamlit run app.py
```

---

## Usage Guide

### 1. Load Sample Data
- Click **`🔄 Load Deadlock Sample`** to see a classic deadlock scenario:
  - **P1** holds **R1** and requests **R2**
  - **P2** holds **R2** and requests **R1**
  - Result: **Deadlock Detected** with a cycle highlighted in red.
- Click **`✅ Load Safe Sample`** to see a safe-state scenario with no cycles.

### 2. Manual Input
- Enter **Processes** (e.g., `P1,P2,P3`) and **Resources** (e.g., `R1,R2,R3`) in the sidebar.
- For each process, specify:
  - **Alloc** — Resources currently held by the process.
  - **Req** — Resources the process is requesting.
- Click **`🚀 Analyze System`** to view the graph and results.

### 3. CSV Upload
Upload a CSV file with the following columns:
```csv
Process,Allocation,Request
P1,R1,R2
P2,R2,R1
```

### 4. Interpreting Results
- **Red edges** in the graph indicate deadlock cycles.
- The dashboard displays **KPIs** including deadlock status and safe-state status.
- If a deadlock is found, **6 resolution strategies** are suggested.
- Download a text report using the **`📥 Download Report`** button.

---

## How It Works

### Wait-For Graph
A directed graph where:
- **Nodes** represent processes.
- **Edges** represent wait dependencies (P1 → P2 means P1 is waiting for a resource held by P2).

### Cycle Detection
Deadlock is detected when a cycle exists in the Wait-For Graph:
```python
nx.simple_cycles(graph)  # NetworkX finds all simple cycles
```
If any cycle is found, a deadlock condition is confirmed.

### Banker's Algorithm (Simplified)
A heuristic safe-state check: the system is considered safe if no process holds more than 2 resources simultaneously.

### Resolution Strategies
When deadlocks are detected, the tool suggests:
1. Terminate the lowest-priority process involved.
2. Preempt resources from a selected process.
3. Rollback transactions to a previous checkpoint.
4. Implement resource ordering to prevent circular waits.
5. Use Banker's Algorithm for safe resource allocation.
6. Apply timeout mechanisms for resource requests.

---

## OS Concepts Demonstrated

- **Deadlock Necessary Conditions**
  - Mutual Exclusion
  - Hold and Wait
  - No Preemption
  - Circular Wait
- **Wait-For Graph Theory**
- **Cycle Detection Algorithms**
- **Banker's Algorithm Principles**
- **Deadlock Prevention & Recovery Strategies**

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `streamlit : The term 'streamlit' is not recognized...` | PowerShell does not add the venv `Scripts` folder to PATH on activation. | Use `python -m streamlit run app.py` instead of `streamlit run app.py`. |
| `ModuleNotFoundError: No module named 'streamlit'` | Dependencies not installed in the active venv. | Run `pip install -r requirements.txt` after activating the venv. |

> **Why `python -m streamlit`?**  
> It executes the Streamlit package directly via Python, bypassing the need for the `streamlit` command to be on your system PATH. This is the most reliable method on Windows with PowerShell virtual environments.

---

## Future Enhancements

- [ ] Full Banker's Algorithm with numeric allocation matrices
- [ ] Graph animation for step-by-step cycle visualization
- [ ] Real-time simulation mode
- [ ] Streamlit Cloud deployment
- [ ] Docker containerization

---

## Acknowledgments

Built as an **Advanced Operating Systems Course Project** to demonstrate practical understanding of deadlock theory, graph algorithms, and interactive Python application development.

---

**Automated Deadlock Detection Tool** — *Detect. Visualize. Resolve.*

