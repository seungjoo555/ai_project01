import pickle
from xgboost import XGBClassifier

BEST_MODE = 2  # 예시: 실험 결과 2단계가 가장 좋았을 경우

# 1. 저장했던 TfidfVectorizer 하나만 로드
with open(f"./model/tfidf_vec_mode_{BEST_MODE}.pkl", "rb") as f:
    loaded_tfidf_vec = pickle.load(f)

# 2. XGBoost 모델 로드
loaded_model = XGBClassifier()
loaded_model.load_model(f"./model/xgb_mode_{BEST_MODE}.json")

print(f"{BEST_MODE}단계 모델 및 통합 전처리기 로드 완료!")