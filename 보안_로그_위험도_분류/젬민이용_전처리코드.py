import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion

# 1. 로그 일반화 함수 정의
def clean_log(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    # IP 주소 치환
    text = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '_IP_', text)
    # 시간 패턴 치환 (HH:MM:SS 또는 HH:MM)
    text = re.sub(r'\d{2}:\d{2}(:\d{2})?', '_TIME_', text)
    # PID 패턴 치환 ([12345])
    text = re.sub(r'\[\d+\]', '[_PID_]', text)
    # 일반 숫자 치환 (단, 마스킹된 토큰 안의 숫자는 제외)
    text = re.sub(r'\b\d+ \b', '_NUM_ ', text)
    # 공백 정리
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 데이터 로드
df = pd.read_csv('security_log_train_quarter.csv')

# 전처리 적용
df['cleaned_log'] = df['full_log'].apply(clean_log)

# [선택] 극소수 클래스(2, 4, 6) 데이터 증강 예시 (단순 복제 또는 샘플 유지를 위해)
# 여기서는 Stratified Split을 위해 최소 개수를 맞추는 목적으로 복제 예시를 듭니다.
rare_classes = df[df['level'].isin([2, 4, 6])]
# 필요에 따라 rare_classes를 복제하여 df에 concat 해줄 수 있습니다.

# 데이터 분할 (Stratified 분할 시 최소 샘플 수가 적으면 에러가 날 수 있으므로 주의)
X_train, X_val, y_train, y_val = train_test_split(
    df['cleaned_log'], df['level'], 
    test_size=0.2, 
    random_state=42,
    stratify=df['level']  # 불균형 데이터셋 필수 옵션
)

# 2. 단어 및 글자 결합형 TF-IDF 벡터라이저 설정
word_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), max_features=5000)
char_vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5), max_features=10000)

vectorizer = FeatureUnion([
    ('word', word_vectorizer),
    ('char', char_vectorizer)
])

# 벡터화 진행
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

print(f"전처리 및 벡터화 완료 대형 행렬 크기: {X_train_vec.shape}")