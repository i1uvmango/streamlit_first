import streamlit as st

st.title('간단한 퀴즈 서비스')

# 객관식 퀴즈
st.header('객관식 퀴즈')
mc_question = '한국의 수도는 어디인가요?'
mc_options = ['서울', '부산', '대구', '인천']
mc_answer = '서울'
mc_user_answer = st.radio(mc_question, mc_options)

# 주관식 퀴즈
st.header('주관식 퀴즈')
sq_question = '파이썬의 창시자는 누구인가요?'
sq_answer = '귀도 반 로섬'
sq_user_answer = st.text_input(sq_question)

# 정답 확인 버튼
if st.button('정답 확인'):
    mc_result = '정답입니다!' if mc_user_answer == mc_answer else '틀렸습니다!'
    sq_result = '정답입니다!' if sq_user_answer.strip() == sq_answer else '틀렸습니다!'
    st.write(f'객관식 퀴즈 결과: {mc_result}')
    st.write(f'주관식 퀴즈 결과: {sq_result}')
