import streamlit as st
import psutil
import plotly.graph_objects as go
import time

st.set_page_config(page_title="RAM Usage Monitor", layout="centered")
st.markdown("""
    <style>
        .glow {
            font-size: 42px;
            color: #10dafa;
            text-align: center;
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #10dafa, 0 0 20px #10dafa;
            }
            to {
                text-shadow: 0 0 20px #1ff0f0, 0 0 30px #1ff0f0;
            }
        }
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="glow">💻 Read the RAM using Python</h1>', unsafe_allow_html=True)
st.markdown('<p class="center-text">Click the start button below to view live RAM usage 📊</p>', unsafe_allow_html=True)

if st.button("🚀 Start RAM Monitor"):
    st.success("Monitoring started!")

    placeholder = st.empty()
    chart_placeholder = st.empty()

    try:
        while True:
            memory = psutil.virtual_memory()
            total = memory.total / (1024 ** 3)
            available = memory.available / (1024 ** 3)
            used = memory.used / (1024 ** 3)
            percent_used = memory.percent
            percent_free = 100 - percent_used

            with placeholder.container():
                st.markdown("### 🧠 Real-Time RAM Stats")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total RAM", f"{total:.2f} GB")
                col2.metric("Available RAM", f"{available:.2f} GB")
                col3.metric("Used RAM", f"{used:.2f} GB")
                col4.metric("RAM Usage", f"{percent_used:.1f}%")

            with chart_placeholder.container():
                
                fig = go.Figure(data=[go.Pie(
                    labels=['Used RAM', 'Free RAM'],
                    values=[percent_used, percent_free],
                    hole=0.5,
                    marker=dict(colors=["#ff4b4b", "#10dafa"]),
                    textinfo='label+percent'
                )])
                fig.update_layout(
                    title="🧩 RAM Usage Classification",
                    width=500,
                    height=400,
                    showlegend=True
                )
                st.plotly_chart(fig)

            time.sleep(3)
    except KeyboardInterrupt:
        st.warning("Monitoring stopped.")