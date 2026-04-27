# 🧠 Automated Deadlock Detection Tool

[![Streamlit App](https://static.streamlit.io/badges/using-streamlit_app_badges.svg)](https://share.streamlit.io/)

## 🎯 Project Overview

**Advanced OS Project** demonstrating deadlock detection using:
- **Wait-For Graphs** & Cycle Detection
- **Banker's Algorithm** (simplified heuristic)
- **Interactive Visualization** with NetworkX + Matplotlib
- **Professional Streamlit Dashboard**

Detects circular waits, visualizes resource dependencies, suggests resolutions.

## 🚀 Features

- 🔍 **Real-time Deadlock Detection** via graph cycles
- 📊 **Interactive Dashboard** with KPIs
- 🎨 **Graph Visualization** (red edges = cycle)
- 💡 **6 Resolution Strategies**
- 📂 **CSV Data Upload**
- 🧪 **Sample Data** (Deadlock + Safe cases)
- 📥 **Report Download**
- 🔬 **Banker's Safe State Check**

## 🏗️ Architecture

```
app.py (Streamlit UI)
├── logic/
│   ├── graph.py (Wait-For Graph)
│   ├── detection.py (Cycle Detection)
│   ├── resolution.py (Suggestions)
│   └── bankers.py (Safe State)
├── utils/
│   └── sample_data.py
└── requirements.txt
```

## 📦 Setup & Run (Step by Step)

### From OS PROJECT root directory:

```
1. cd deadlock_detector
2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. python -m streamlit run app.py
```

### Copy-Paste Commands (run each separately):

1. `cd "c:/Users/mohit kumar/OneDrive/Desktop/OS PROJECT/deadlock_detector"`
2. `python -m venv venv`
3. `venv\Scripts\activate` *(prompt shows (venv))*
4. `pip install -r requirements.txt`
5. `python -m streamlit run app.py` → **Opens http://localhost:8501**

### Quick Re-run (venv exists):
```
cd "c:/Users/mohit kumar/OneDrive/Desktop/OS PROJECT/deadlock_detector"
venv\Scripts\activate
python -m streamlit run app.py
```

**✅ Success:** Browser opens dashboard automatically.

---

## 🐛 Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| `streamlit : The term 'streamlit' is not recognized...` | PowerShell does not add the venv `Scripts` folder to PATH on activation. | Use `python -m streamlit run app.py` instead of `streamlit run app.py`. |
| `ModuleNotFoundError: No module named 'streamlit'` | Dependencies not installed in the active venv. | Run `pip install -r requirements.txt` after activating the venv. |

> **Why `python -m streamlit`?**<br>
> It tells Python to execute the Streamlit package directly, bypassing the need for the `streamlit` command to be on your system PATH. This is the most reliable method on Windows with PowerShell virtual environments.

## 🎮 Demo Usage

1. **Load Sample:**
   - `🔄 Deadlock Sample` → P1(R1→R2), P2(R2→R1) → **DETECTED**
   - `✅ Safe Sample` → No cycle → **SAFE**

2. **Manual Input:**
   ```
   Processes: P1,P2,P3
   Resources: R1,R2,R3
   
   P1 Alloc: R1   Req: R2
   P2 Alloc: R2   Req: R1
   ```

3. **CSV Upload:**
   ```
   Process,Allocation,Request
   P1,R1,R2
   P2,R2,R1
   ```

## 🔬 How It Works

### 1. Wait-For Graph
```
P1 holds R1, requests R2 (held by P2) → P1 → P2
P2 holds R2, requests R1 (held by P1) → P2 → P1
→ CYCLE = DEADLOCK
```

### 2. Cycle Detection
```python
nx.simple_cycles(graph)  # NetworkX
```

### 3. Resolution Strategies
- Process termination
- Resource preemption
- Resource ordering
- Banker's Algorithm
- Timeouts

### 4. Banker's (Demo Heuristic)
Safe if no process allocates >2 resources.

## 📈 Screenshot

![Dashboard](screenshots/dashboard.png)
*(Add your screenshot here)*

## 🎓 OS Concepts Covered

- **Deadlock Conditions** (Mutual Exclusion, Hold-Wait, No Preemption, Circular Wait)
- **Wait-For Graph Theory**
- **Cycle Detection Algorithms**
- **Banker's Algorithm Principles**
- **Prevention Strategies**

## 🛠️ Tech Stack

- **Backend:** Python 3.12
- **UI:** Streamlit 1.36+
- **Graphs:** NetworkX 3.6
- **Viz:** Matplotlib 3.10
- **Data:** Pandas 3.0

## 🔮 Future Enhancements

- [ ] Full Banker's (numeric matrix)
- [ ] Graph Animation
- [ ] Real-time Simulation
- [ ] Streamlit Cloud Deploy
- [ ] Docker Container

## 📝 Report Sections

1. Deadlock Theory
2. System Design
3. Algorithm Implementation
4. Results & Screenshots
5. VIVA Presentation

---

**Built for OS Course | Advanced Deadlock Analysis Tool** 🚀



