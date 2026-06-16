import streamlit as st
import pandas as pd
import numpy as np
import time

# إعداد واجهة النظام
st.set_page_config(page_title="Advanced Orchestrator", layout="wide")
st.title("🌐 Smart Cluster Management Center")

# تهيئة بيانات السيرفرات
if 'nodes' not in st.session_state:
    st.session_state.nodes = {
        "Node-A": {"conns": 10, "latency": 1, "status": "Active"},
        "Node-B": {"conns": 25, "latency": 2, "status": "Active"},
        "Node-C": {"conns": 5, "latency": 4, "status": "Active"}
    }

# القائمة الجانبية (لوحة التحكم)
st.sidebar.header("⚙️ لوحة الإعدادات")
algo = st.sidebar.selectbox("اختر خوارزمية التوزيع:", ["Round Robin", "Least Connections"])
st.sidebar.markdown("---")

# محاكاة إرسال طلب
if st.sidebar.button("إرسال طلب (Request Simulation)"):
    # Circuit Breaker Logic
    active_nodes = {k: v for k, v in st.session_state.nodes.items() if v["latency"] < 3}
    
    if not active_nodes:
        st.error("🚨 خطر: جميع العقد غير مستقرة! (Circuit Open)")
    else:
        # اختيار العقدة بناءً على الخوارزمية
        if algo == "Least Connections":
            target = min(active_nodes, key=lambda x: active_nodes[x]["conns"])
        else:
            target = np.random.choice(list(active_nodes.keys()))
            
        st.session_state.nodes[target]["conns"] += 1
        st.toast(f"تم توجيه الطلب إلى {target} بنجاح!", icon="✅")

# العرض الرئيسي
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 حالة العقد (Nodes Status)")
    df = pd.DataFrame.from_dict({k: v["conns"] for k, v in st.session_state.nodes.items()}, orient='index', columns=['Connections'])
    st.table(df)

with col2:
    st.subheader("📈 تحليل الأداء لحظياً")
    st.bar_chart(df)

# نظام التنبيهات الاحترافي
st.subheader("🛡️ نظام الحماية (Circuit Breaker Status)")
for name, data in st.session_state.nodes.items():
    if data["latency"] >= 3:
        st.error(f"⚠️ {name} معزول (Circuit Open) بسبب بطء الاستجابة: {data['latency']}s")
    else:
        st.success(f"✅ {name} يعمل بشكل طبيعي (Status: Closed)")

st.markdown("---")
st.caption("نظام إدارة عناقيد السيرفرات المتطور - مادة الأنظمة الموزعة")
