
import streamlit as st

st.set_page_config(
    page_title="NEON BREACH",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp {
    background-color: #080b12;
    color: #edf4ff;
}
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
}
h1 {
    font-weight: 900;
    letter-spacing: 3px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>NEON <span style='color:#d7ff55'>BREACH</span></h1>",
    unsafe_allow_html=True
)

st.caption("TACTICAL FPS · SINGLE PLAYER")
st.divider()

st.markdown("### 작전 브리핑")
st.write(
    "적이 점령한 전술 구역에 진입하세요. "
    "무기와 특수 능력을 활용해 적 봇을 제압하는 것이 목표입니다."
)

st.info("기본 화면이 준비되었습니다. 다음 단계에서 게임을 추가합니다.")

st.markdown("#### 조작 안내")
st.write("WASD 이동 · 마우스 조준 · 클릭 사격 · R 재장전 · Q 대시 · E 방어막")

st.divider()
st.caption("NEON BREACH | Original tactical FPS prototype")
