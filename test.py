 import pandas as pd

# 데이터 읽기
data_path = '/mnt/data/ChatbotData.csv'
data = pd.read_csv(data_path)

# 레벤슈타인 거리 함수
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

# 유사도 계산 및 가장 유사한 질문 찾기
def find_most_similar_question(chat_question, questions):
    min_distance = float('inf')
    min_index = -1
    
    for i, question in enumerate(questions):
        distance = levenshtein_distance(chat_question, question)
        if distance < min_distance:
            min_distance = distance
            min_index = i
    
    return min_index

# 예제 chat의 질문
chat_question = "오늘 날씨 어때?"

# 학습 데이터의 질문들
questions = data['Q'].tolist()

# 가장 유사한 질문의 인덱스 찾기
most_similar_index = find_most_similar_question(chat_question, questions)

# 해당 인덱스의 답변 출력
answer = data['A'][most_similar_index]
print(f"Chat 질문: {chat_question}")
print(f"가장 유사한 학습 데이터의 질문: {questions[most_similar_index]}")
print(f"답변: {answer}")
      