import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Advanced Orchestrator", layout="wide")

st.title("🚀 Smart Cluster Orchestrator")

if 'nodes' not in st.session_state:
    st.session_state.nodes = {"Node-A": 80, "Node-B": 90, "Node-C": 50}

# دالة ذكية لإعادة التوازن (Load Rebalancing)
def rebalance():
    # نجد السيرفر الأكثر ضغطاً ونوزع جزءاً من أحماله على السيرفرات الأخرى
    max_node = max(st.session_state.nodes, key=st.session_state.nodes.get)
    if st.session_state.nodes[max_node] > 100:
        st.session_state.nodes[max_node] -= 30
        for node in st.session_state.nodes:
            if node != max_node:
                st.session_state.nodes[node] += 10
        st.toast("تم إعادة التوزيع تلقائياً بسبب الضغط العالي!", icon="🔄")

st.sidebar.header("لوحة التحكم")
for node in st.session_state.nodes:
    if st.sidebar.button(f"رفع الحمل على {node}"):
        st.session_state.nodes[node] += np.random.randint(10, 30)
        rebalance() # استدعاء دالة التوازن بعد كل تحديث

col1, col2 = st.columns([1, 2])
with col1:
    st.table(pd.DataFrame.from_dict(st.session_state.nodes, orient='index', columns=['Connections']))

with col2:
    st.bar_chart(pd.DataFrame.from_dict(st.session_state.nodes, orient='index', columns=['Connections']))
