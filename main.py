import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="2026 월드컵 예측기",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ 2026 북중미 월드컵 순위 예측기")

st.markdown("""
FIFA 랭킹, 최근 성적, 선수층 등을 반영한
가상 월드컵 예측 모델입니다.
""")

# ---------------------------
# 예측 데이터
# ---------------------------

data = {
    "국가":[
        "아르헨티나","프랑스","브라질","스페인","잉글랜드",
        "독일","포르투갈","네덜란드","대한민국","일본",
        "우루과이","벨기에","콜롬비아","미국","멕시코"
    ],
    "우승확률":[
        16,14,13,11,10,
        8,7,5,3,3,
        3,2,2,2,1
    ]
}

df = pd.DataFrame(data)

# ---------------------------
# TOP10 순위
# ---------------------------

st.subheader("🏆 예상 최종 순위 TOP 10")

ranking = pd.DataFrame({
    "순위":[1,2,3,4,5,6,7,8,9,10],
    "국가":[
        "아르헨티나",
        "프랑스",
        "브라질",
        "스페인",
        "잉글랜드",
        "독일",
        "포르투갈",
        "네덜란드",
        "대한민국",
        "일본"
    ]
})

st.dataframe(
    ranking,
    use_container_width=True
)

# ---------------------------
# 우승확률 그래프
# ---------------------------

st.subheader("📊 우승 확률")

fig = px.bar(
    df,
    x="국가",
    y="우승확률",
    text="우승확률",
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------
# 국가 선택
# ---------------------------

st.subheader("🔍 국가 분석")

country = st.selectbox(
    "국가 선택",
    df["국가"]
)

info = {
    "아르헨티나":"메시 이후 세대교체 성공",
    "프랑스":"최강 선수층",
    "브라질":"공격력 우수",
    "스페인":"점유율 축구 강세",
    "잉글랜드":"프리미어리그 기반",
    "독일":"전통 강호",
    "포르투갈":"균형 잡힌 전력",
    "네덜란드":"조직력 우수",
    "대한민국":"손흥민 세대 이후 유망주 성장",
    "일본":"아시아 최강권",
    "우루과이":"남미 강호",
    "벨기에":"황금세대 마무리",
    "콜롬비아":"공격 전개 우수",
    "미국":"개최국 프리미엄",
    "멕시코":"홈 이점"
}

st.success(info[country])

# ---------------------------
# 대한민국 예측
# ---------------------------

st.subheader("🇰🇷 대한민국 예상 성적")

st.metric(
    "예상 최고 성적",
    "8강"
)

# ---------------------------
# 워드클라우드
# ---------------------------

st.subheader("☁️ 월드컵 키워드 워드클라우드")

text = """
대한민국 대한민국 대한민국
손흥민 손흥민 손흥민
김민재 김민재
이강인 이강인 이강인
아르헨티나
프랑스 프랑스
브라질 브라질
스페인
독일
포르투갈
우승 우승 우승
월드컵 월드컵 월드컵 월드컵
축구 축구 축구 축구 축구
"""

# 나눔고딕 폰트
font_path = "NanumGothic.ttf"

wc = WordCloud(
    font_path=font_path,
    width=1000,
    height=500,
    background_color="white"
).generate(text)

fig2, ax = plt.subplots(figsize=(12,6))

ax.imshow(wc)
ax.axis("off")

st.pyplot(fig2)

# ---------------------------
# 전체 데이터
# ---------------------------

with st.expander("전체 데이터 보기"):
    st.dataframe(df)
