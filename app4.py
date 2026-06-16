import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="System Orchestrator", layout="wide")

st.title("🚀 Advanced System Orchestrator & Monitor")

# تهيئة حالة السيرفرات
if 'nodes' not in st.session_state:
    st.session_state.nodes = {"Node-A": 10, "Node-B": 25, "Node-C": 5}

# لوحة التحكم الجانبية
st.sidebar.header("تحكم النظام")
for node in st.session_state.nodes:
    if st.sidebar.button(f"رفع الحمل على {node}"):
        st.session_state.nodes[node] += np.random.randint(5, 15)

# العرض الرئيسي
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("حالة السيرفرات (Raw Data)")
    st.table(pd.DataFrame.from_dict(st.session_state.nodes, orient='index', columns=['Connections']))

with col2:
    st.subheader("تحليل الأداء اللحظي (Visualization)")
    chart_data = pd.DataFrame.from_dict(st.session_state.nodes, orient='index', columns=['Connections'])
    st.bar_chart(chart_data)

st.markdown("---")
st.success("نظام التوزيع الذكي يعمل حالياً على مراقبة الضغط وتوجيه المسارات.")