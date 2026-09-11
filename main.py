import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 여행지 추천 ✈️",
    page_icon="💖",
    layout="centered"
)

# MBTI별 추천 데이터
mbti_data = {
    "ISTJ": {"place": "전국 정갈한 한옥마을 (전주, 경주)", "desc": "계획대로 착착! 고즈넉하고 질서정연한 풍경 속에서 완벽한 휴식을 즐겨보세요 🏯"},
    "ISFJ": {"place": "아기자기한 제주도 동쪽 마을", "desc": "따뜻한 감성과 조용한 카페에서 소중한 사람과 오붓한 추억을 만들어봐요 🌸"},
    "INFJ": {"place": "고요한 강원도 오대산 숲길", "desc": "깊은 생각과 함께 마음을 충전할 수 있는 평화롭고 신비로운 숲속 산책 🌲"},
    "INTJ": {"place": "역사와 스토리가 가득한 박물관 투어", "desc": "지적 호기심을 지극해 줄 유서 깊은 유적지와 전시회 탐방 🏛️"},
    "ISTP": {"place": "액티비티 가득한 제주 해안도로 라이딩", "desc": "바람을 가르며 느끼는 자유로운 모험과 여유로운 즉흥 여행 🏍️"},
    "ISFP": {"place": "예술적 감성의 감성 캠핑장", "desc": "자연 속에서 아무것도 안 하고 멍때리기, 감성 사진 찍기 딱 좋은 곳 ⛺"},
    "INFP": {"place": "서정적인 남해 다랭이마을", "desc": "동화 속 한 장면 같은 바다와 들판을 바라보며 감성 다이어리 적기 🌊"},
    "INTP": {"place": "신기한 과학관 및 천문대", "desc": "밤하늘의 별을 보며 우주의 신비를 탐구하는 지적 유희 🔭"},
    "ESTP": {"place": "짜릿한 가평 수상레저 & 루지", "desc": "지루할 틈이 없다! 온몸으로 즐기는 스릴 만점 익스트림 스포츠 🏄‍♂️"},
    "ESFP": {"place": "화려한 부산 해운대 & 광안리", "desc": "신나는 음악, 맛있는 음식, 핫한 밤바다까지 완벽한 흥 폭발 여행 🎆"},
    "ENFP": {"place": "알록달록한 부산 감천문화마을", "desc": "골목마다 새로운 즐거움과 만남이 기다리는 러블리한 탐험 🎨"},
    "ENTP": {"place": "다채로운 서울 핫플레이스 탐방", "desc": "매번 새로운 팝업스토어와 트렌디한 공간에서 얻는 신선한 자극 힙함 그 자체 ✨"},
    "ESTJ": {"place": "알찬 동해안 단체 투어 코스", "desc": "동선까지 완벽하게 짜여진 동해 바다 힐링 로드 travel 🚌"},
    "ESFJ": {"place": "정이 넘치는 여수 밤바다 포차거리", "desc": "좋은 사람들과 맛있는 음식을 나누며 하하호호 웃음짓는 시간 낭만 가득 🥳"},
    "ENFJ": {"place": "모두가 행복해지는 에버랜드 & 롯데월드", "desc": "사랑하는 이들의 웃음소리로 가득한 환상의 나라 🎈"},
    "ENTJ": {"place": "성장과 힐링을 함께하는 워케이션 명소", "desc": "일도 휴식도 스마트하고 완벽하게 해내는 성공적인 리프레시 💼"}
}

# 타이틀 영역
st.title("💖 엠비티아이별 찰떡 여행지 찾기 💖")
st.write("당신의 MBTI를 선택하면 어울리는 러블리한 여행지를 추천해드려요!")

st.divider()

# 선택 박스
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택해주세요!",
    list(mbti_data.keys())
)

# 결과 출력 버튼
if st.button("✨ 추천 여행지 확인하기 ✨", use_container_width=True):
    result = mbti_data[selected_mbti]
    
    st.balloons()
    st.success(f"**[{selected_mbti}]** 님을 위한 추천 여행지!")
    st.markdown(f"### 📍 {result['place']}")
    st.info(result['desc'])

st.caption("제작: 귀여운 MBTI 여행 추천 앱 🎈")
