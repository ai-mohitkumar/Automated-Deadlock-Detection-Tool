import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import io

from logic.graph import create_wait_for_graph
from logic.detection import detect_deadlock
from logic.resolution import suggest_resolution
from logic.bankers import bankers_algorithm
from utils.sample_data import load_sample_deadlock, load_sample_safe

st.set_page_config(
    page_title="Deadlock Detector",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
# 🧠 Deadlock Detection System
### Real-Time OS Resource Analysis Dashboard

Detect deadlocks using Wait-For Graphs, Banker's Algorithm, and visualize system state.
""")

# Sidebar for inputs
st.sidebar.header("📊 System Configuration")

# Sample data buttons
if st.sidebar.button("🔄 Load Deadlock Sample"):
    processes, allocation, request = load_sample_deadlock()
    st.session_state.processes = processes
    st.session_state.allocation = allocation
    st.session_state.request = request
    st.rerun()

if st.sidebar.button("✅ Load Safe Sample"):
    processes, allocation, request = load_sample_safe()
    st.session_state.processes = processes
    st.session_state.allocation = allocation
    st.session_state.request = request
    st.rerun()

# Manual input
processes_input = st.sidebar.text_input("Processes (comma-separated)", value="P1,P2,P3", key="processes_input")
resources_input = st.sidebar.text_input("Resources (comma-separated)", value="R1,R2", key="resources_input")

processes = [p.strip() for p in processes_input.split(',') if p.strip()]
resources = [r.strip() for r in resources_input.split(',') if r.strip()]

st.sidebar.subheader("🔹 Allocation & Request")

allocation = {}
request_dict = {}

col1, col2 = st.sidebar.columns(2)
for i, p in enumerate(processes):
    with col1 if i % 2 == 0 else col2:
        alloc = st.text_input(f"{p} Alloc", value="", key=f"alloc_{p}")
        req = st.text_input(f"{p} Req", value="", key=f"req_{p}")
        allocation[p] = [r.strip() for r in alloc.split(',') if r.strip()]
        request_dict[p] = [r.strip() for r in req.split(',') if r.strip()]

# CSV Upload
st.sidebar.subheader("📂 Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'Process' in df.columns and 'Allocation' in df.columns and 'Request' in df.columns:
        for _, row in df.iterrows():
            p = row['Process']
            allocation[p] = [r.strip() for r in str(row['Allocation']).split(',') if r.strip()]
            request_dict[p] = [r.strip() for r in str(row['Request']).split(',') if r.strip()]
        processes = list(allocation.keys())
        st.sidebar.success("✅ CSV loaded!")
    else:
        st.sidebar.error("❌ CSV must have 'Process', 'Allocation', 'Request' columns")

request = request_dict

# Main analysis
if st.button("🚀 Analyze System", type="primary"):
    if processes:
        st.session_state.results = {}
        
        # Create graph
        graph = create_wait_for_graph(processes, allocation, request)
        
        # Deadlock detection
        has_deadlock, cycles = detect_deadlock(graph)
        
        # Banker's (resource name based demo)
        available_demo = {r: 1 for r in resources}
        max_need_demo = {p: request.get(p, []) + allocation.get(p, []) for p in processes}
        alloc_demo = allocation
        is_safe, safe_seq = bankers_algorithm(processes, available_demo, max_need_demo, alloc_demo)
        
        st.session_state.graph = graph
        st.session_state.has_deadlock = has_deadlock
        st.session_state.cycles = cycles
        st.session_state.is_safe = is_safe
        st.session_state.safe_seq = safe_seq
    else:
        st.warning("⚠️ Please enter processes")

# Display results
if 'graph' in st.session_state:
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Processes", len(processes))
    col2.metric("Resources", len(resources))
    col3.metric("Deadlock", "Detected" if st.session_state.has_deadlock else "None")
    col4.metric("Safe State", "Yes" if st.session_state.is_safe else "No")
    
    # Graph visualization
    st.subheader("📈 Wait-For Graph")
    graph = st.session_state.graph
    has_deadlock = st.session_state.has_deadlock
    cycles = st.session_state.cycles
    
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(graph, k=3, iterations=50)
    
    # Color edges in cycles red
    edge_colors = ['red' if any((u,v) in cycle or (v,u) in cycle for cycle in cycles) else 'black' for u,v in graph.edges()]
    
    nx.draw(
        graph, pos, ax=ax,
        with_labels=True,
        node_color='lightblue',
        edge_color=edge_colors,
        node_size=3000,
        font_size=12,
        font_weight='bold',
        arrows=True,
        arrowsize=20
    )
    plt.title("Wait-For Graph (Red edges indicate cycle)")
    st.pyplot(fig)
    
    # Results
    if has_deadlock:
        st.error("⚠️ Deadlock Detected!")
        st.write("**Cycles:**", st.session_state.cycles)
        
        suggestions = suggest_resolution(cycles)
        st.subheader("💡 Resolution Strategies")
        for i, suggestion in enumerate(suggestions, 1):
            st.write(f"{i}. {suggestion}")
    else:
        st.success("✅ No Deadlock Found")
    
    if st.session_state.is_safe:
        st.success(f"✅ System Safe - Execution order: {st.session_state.safe_seq}")
    else:
        st.warning("⚠️ Unsafe state - Potential for future deadlock")

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Enter processes and resources
    2. Fill allocation (currently held) and request (wanted)
    3. Click **Analyze System**
    4. View graph and results
    
    **Sample Deadlock:** P1 holds R1 wants R2, P2 holds R2 wants R1
    """)

# Download report
if 'has_deadlock' in st.session_state:
    report = f"""
Deadlock Analysis Report
=======================
Deadlock: {st.session_state.has_deadlock}
Safe: {st.session_state.is_safe}
Cycles: {st.session_state.cycles}
    """
    st.download_button(
        "📥 Download Report",
        data=report,
        file_name="deadlock_report.txt",
        mime="text/plain"
    )

