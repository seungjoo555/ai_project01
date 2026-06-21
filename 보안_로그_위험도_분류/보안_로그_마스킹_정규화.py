import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

# 1. 단계별 마스킹 처리를 위한 함수 정의
def mask_log_text(text, mode_num):
    if mode_num == 0:  # Baseline: 마스킹 없음
        return text
        
    # [수정 및 추가된 정규표현식 패턴]
    # 1. 날짜+시간 (소수점 자리에 콤마[,]도 인식하도록 수정)
    p_datetime = r'\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:[.,]\d+)?(?:Z|[+-]\d{2}:?\d{2})?'
    
    # 2. 날짜 (Syslog의 'Sep 24', 'Mar  2' [공백 1~2개 포함] 형태 완벽 대응 추가)
    p_date     = r'\d{4}-\d{2}-\d{2}|\d{2}/[A-Za-z]{3}/\d{4}|\d{2}/\d{2}/\d{4}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\b'
    
    # 3. 시간
    p_time     = r'\d{2}:\d{2}:\d{2}(?:[.,]\d+)?'
    
    # 4. IP 주소
    p_ip       = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    
    # 5. 포트 번호 (re 모듈 에러 방지용 고정 폭 분리 형태)
    p_port     = r'(?<=\b):\d{2,5}\b|(?<=<IP>):\d{2,5}\b|port\s*\d+'
    
    # 6. 16진수 (proctitle=736C656570003630 같은 긴 해시값 대응)
    p_hex      = r'\b0x[0-9a-fA-F]+\b|\b[0-9a-fA-F]{8,}\b'
    
    # 7. 시리얼 번호 / UUID 형태
    p_sn       = r'\b[A-Za-z0-9]{4,}-[A-Za-z0-9]{4,}-[A-Za-z0-9]{4,}\b'
    
    # 8. 일반 숫자 (소수점을 포함하도록 수정하여 1611892806.457 등이 분절되는 것 방지)
    p_num      = r'\b\d+(?:\.\d+)?\b'

    # 1단계 ~ 8단계: 단일 마스킹 테스트
    if mode_num == 1:
        text = re.sub(p_ip, '<IP>', text)
    elif mode_num == 2:
        text = re.sub(p_date, '<DATE>', text)
    elif mode_num == 3:
        text = re.sub(p_time, '<TIME>', text)
    elif mode_num == 4:
        text = re.sub(p_datetime, '<DATETIME>', text)
    elif mode_num == 5:
        text = re.sub(p_port, '<PORT>', text)
    elif mode_num == 6:
        text = re.sub(p_num, '<NUM>', text)
    elif mode_num == 7:
        text = re.sub(p_hex, '<HEX>', text)
    elif mode_num == 8:
        text = re.sub(p_sn, '<SN>', text)
        
    # 9단계: 전체 마스킹 종합 (순서가 매우 중요합니다)
    elif mode_num == 9:
        text = re.sub(p_datetime, '<DATETIME>', text)
        text = re.sub(p_date, '<DATE>', text)
        text = re.sub(p_time, '<TIME>', text)
        text = re.sub(p_ip, '<IP>', text)
        text = re.sub(p_port, '<PORT>', text)
        text = re.sub(p_hex, '<HEX>', text)
        text = re.sub(p_sn, '<SN>', text)
        text = re.sub(p_num, '<NUM>', text)
        
    return text

# 단계별 이름 매핑 (결과 표 출력용)
mode_names = {
    0: "Baseline (순정 상태)",
    1: "1단계: IP만 마스킹 (<IP>)",
    2: "2단계: 날짜만 마스킹 (<DATE>)",
    3: "3단계: 시간만 마스킹 (<TIME>)",
    4: "4단계: 날짜+시간만 마스킹 (<DATETIME>)",
    5: "5단계: 포트만 마스킹 (<PORT>)",
    6: "6단계: 일반 숫자만 마스킹 (<NUM>)",
    7: "7단계: 16진수만 마스킹 (<HEX>)",
    8: "8단계: 시리얼 번호만 마스킹 (<SN>)",
    9: "9단계: 전체 토큰 마스킹 (종합)"
}

# 실험 결과를 누적 저장할 리스트
experiment_results = []

# 정답 라벨 및 클래스 정보 고정 (노트북 기존 변수 활용)
labels_sorted = sorted(train["level"].unique())
num_classes = len(labels_sorted)

print("시작: 0단계(Baseline)부터 9단계(전체 종합)까지 자동 Ablation Study를 실행합니다.")
print("※ GPU(CUDA) 가속을 활용하여 단계별 약 수십 초 내외가 소요됩니다.")

# 0단계부터 9단계까지 자동 루프 실행
for mode in range(0, 10):
    print(f"\n[진행 중] {mode_names[mode]} 실험 처리 중...")
    
    # 1) 원본 train 데이터 보존을 위해 copy 후 마스킹 적용
    df_temp = train.copy()
    df_temp["full_log"] = df_temp["full_log"].fillna("").apply(lambda x: mask_log_text(x, mode))
    
    # 2) Train / Valid 분 분리 (노트북 기존 설정 시드 고정하여 데이터 일관성 유지)
    X_text = df_temp["full_log"]
    y_labels = df_temp["level"]
    X_train_t, X_valid_t, y_train_t, y_valid_t = train_test_split(
        X_text, y_labels,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y_labels
    )
    
    # 3) TF-IDF 벡터화 및 특수문자(< >) 보존 패턴 적용
    cv = CountVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        min_df=3,
        max_df=0.95,
        token_pattern=r"(?u)<\w+>|\b\w\w+\b"  # <IP>, <DATE> 등이 분해되지 않도록 규칙 수정
    )
    tfidf_trans = TfidfTransformer()
    
    X_train_cv = cv.fit_transform(X_train_t)
    X_train_tfidf = tfidf_trans.fit_transform(X_train_cv).astype('float32')
    
    X_valid_cv = cv.transform(X_valid_t)
    X_valid_tfidf = tfidf_trans.transform(X_valid_cv).astype('float32')
    
    # 4) XGBoost 모델 재정의 및 GPU 학습 진행
    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="multi:softprob",
        num_class=num_classes,
        eval_metric="mlogloss",
        random_state=RANDOM_STATE,
        tree_method="hist",
        device="cuda"
    )
    model.fit(X_train_tfidf, y_train_t)
    
    # 5) 검증 데이터 예측 및 Macro F1 스코어 계산
    valid_pred = model.predict(X_valid_tfidf)
    macro_f1 = f1_score(y_valid_t, valid_pred, labels=labels_sorted, average="macro", zero_division=0)
    
    print(f"-> 완료! 검증 Macro F1: {macro_f1:.4f}")
    
    # 6) 결과 저장
    experiment_results.append({
        "실험 단계": "Baseline" if mode == 0 else f"{mode}단계",
        "마스킹 대상": "없음 (순정 상태)" if mode == 0 else mode_names[mode].split(": ")[1],
        "검증 성능 (Macro F1)": round(macro_f1, 4),
        "Public Score (제출 점수)": "-"  # 데이콘 제출 후 직접 채워넣을 수 있도록 공란 처리
    })

# 7) 전체 실험 결과를 판다스 데이터프레임으로 변환하여 이쁘게 출력
df_ablation_summary = pd.DataFrame(experiment_results)
print("\n========================= [최종 Ablation Study 결과 요약 리포트] =========================")
display(df_ablation_summary)