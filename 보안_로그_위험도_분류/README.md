# 🧠 Developer Burnout Monitoring Dashboard

> **GitHub 커밋 데이터를 활용한 개발자 번아웃 위험도 분석 및 AI 기반 진단 대시보드**

개발자의 GitHub 활동 데이터를 분석하여 **야간 커밋, 주말 커밋, 커밋 빈도 등의 행동 패턴을 기반으로 번아웃 위험 신호를 탐지​**하고, 이를 Streamlit 대시보드로 시각화한 데이터 마이닝 프로젝트입니다.

과거에 축적된 GitHub 활동 데이터를 분석하는 것뿐만 아니라, **GitHub Public Repository와 실시간으로 연동하여 최근 커밋 데이터를 가져오고 번아웃 위험도를 분석**할 수 있도록 구현했습니다.

또한 로컬 LLM을 활용하여 정량적인 지표뿐만 아니라 **커밋 메시지의 문맥을 분석하여 AI 기반 번아웃 진단 리포트**를 생성할 수 있습니다.

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|:---:|:---|
| 🎯 프로젝트명 | Developer Burnout Monitoring Dashboard |
| 📊 프로젝트 유형 | 데이터 마이닝 / 데이터 분석 / 머신러닝 |
| 🧠 핵심 주제 | GitHub 활동 데이터를 활용한 개발자 번아웃 위험도 분석 |
| 🖥️ Dashboard | Streamlit |
| 🐍 Language | Python |
| 📡 실시간 데이터 | GitHub Public Repository API |
| 🤖 AI 분석 | Local LLM (LM Studio / Gemma) |
| 📈 Visualization | Plotly |
| 📦 Data Processing | Pandas |
| 🧪 Anomaly Detection | Isolation Forest |
| 📁 저장소 | [GitHub Repository](https://github.com/seungjoo555/DataMining_project) |

---

# 🎯 프로젝트 목표

소프트웨어 개발자는 프로젝트 일정, 지속적인 코드 수정, 야간 작업, 주말 근무 등으로 인해 높은 업무 스트레스를 경험할 수 있습니다.

하지만 개발자의 번아웃은 단순히 **업무량만으로 판단하기 어렵고**, 업무를 수행하는 시간과 작업 패턴에서도 위험 신호가 나타날 수 있습니다.

따라서 이 프로젝트에서는 GitHub 커밋 데이터를 활용하여 다음과 같은 질문에 답하고자 했습니다.

> **"개발자의 GitHub 활동 패턴을 통해 번아웃 위험 신호를 정량적으로 확인할 수 있을까?"**

이를 위해 GitHub 활동 데이터를 기반으로 번아웃 관련 지표를 생성하고, 개발자별 위험도를 분석할 수 있는 대시보드를 구현했습니다.

---

# 🔍 핵심 분석 지표

프로젝트에서는 GitHub 커밋 데이터를 기반으로 개발자의 활동 패턴을 분석합니다.

### 🌙 야간 커밋 비율

```text
22:00 ~ 06:00
```

해당 시간대에 작성된 커밋의 비율을 계산하여 야간 작업 패턴을 확인합니다.

### 🗓️ 주말 커밋 비율

토요일과 일요일에 작성된 커밋의 비율을 계산합니다.

### 📦 커밋 빈도

개발자의 전체 커밋 활동량을 분석하여 평소보다 급격하게 증가하거나 감소하는 패턴을 확인합니다.

### 📈 번아웃 지수

과거 데이터에서는 커밋량, 야간 활동, 주말 활동 등을 기반으로 번아웃 관련 지표를 생성하여 개발자별 위험도를 분석합니다.

실시간 분석에서는 다음과 같이 계산합니다.

```text
실시간 번아웃 지수
= (야간 커밋 비율 + 주말 커밋 비율) / 2
```

---

# 🚦 위험도 분류

실시간 GitHub 데이터를 기반으로 다음과 같이 위험도를 분류합니다.

| 번아웃 지수 | 위험도 |
|:---:|:---:|
| `< 15` | 🟢 정상 (Stable) |
| `15 ~ 39.9` | 🟡 주의 (Warning) |
| `>= 40` | 🔴 위험 (Danger) |

> ⚠️ 본 지표는 의료적 진단이나 실제 번아웃 여부를 판단하기 위한 것이 아니라, **GitHub 활동 패턴에서 나타나는 업무 과부하 가능성을 탐지하기 위한 분석 지표**입니다.

---

# 🖥️ 주요 기능

## 1️⃣ 프로젝트 검색 및 필터링

GitHub 프로젝트별로 데이터를 필터링하여 특정 Repository의 개발자 활동을 분석할 수 있습니다.

```text
📂 프로젝트 선택
        ↓
Repository 필터링
        ↓
개발자 활동 분석
```

---

## 2️⃣ 팀 건강도 요약

대시보드에서 팀 전체의 상태를 한눈에 확인할 수 있습니다.

- 👨‍💻 총 참여 개발자 수
- 🔥 위험(Danger) 개발자 수
- ⚠️ 주의(Warning) 개발자 수
- 🗓️ 최신 분석 주차

이를 통해 팀 전체의 번아웃 위험 상태를 빠르게 파악할 수 있습니다.

---

## 3️⃣ 위험군 개발자 탐지

현재 분석 주차를 기준으로 번아웃 위험도가 높은 개발자를 자동으로 추출합니다.

```text
Developer
    ↓
Burnout Score 계산
    ↓
Risk Level 분류
    ↓
Danger / Warning 개발자 탐지
```

위험도가 높은 개발자는 별도의 목록으로 표시하여 관리자가 빠르게 확인할 수 있도록 구성했습니다.

---

## 4️⃣ 주차별 번아웃 변화 추이

개발자의 활동 패턴을 주 단위로 집계하여 번아웃 지수의 변화를 시각화합니다.

이를 통해 단순히 현재 상태뿐만 아니라,

> **"최근 번아웃 위험도가 지속적으로 증가하고 있는가?"**

를 확인할 수 있습니다.

---

## 5️⃣ 개별 개발자 심층 분석

개발자를 선택하면 해당 개발자의 활동 데이터를 상세하게 확인할 수 있습니다.

### 제공되는 분석

- 📊 주차별 번아웃 지수
- 🌙 야간 커밋 비율
- 🗓️ 주말 커밋 비율
- 📈 활동 패턴 변화
- 🚦 위험도 변화

개발자의 활동 패턴을 시계열 형태로 확인할 수 있도록 구성했습니다.

---

# 🌐 실시간 GitHub 분석

이 프로젝트의 핵심 기능 중 하나는 **GitHub Public Repository 실시간 연동**입니다.

사용자가 Repository 경로를 입력하면 GitHub API를 통해 최근 커밋 데이터를 가져옵니다.

```text
Repository 입력
        ↓
GitHub API
        ↓
최근 Commit 데이터 수집
        ↓
작성자 / 시간 / 메시지 추출
        ↓
야간·주말 활동 분석
        ↓
실시간 번아웃 지수 계산
        ↓
위험도 분류
```

현재 구현에서는 실시간 분석을 위해 최근 **50개의 커밋**을 수집합니다.

---

# 🤖 AI 기반 번아웃 진단

정량적인 활동 지표뿐만 아니라 **커밋 메시지의 텍스트 문맥**까지 분석할 수 있도록 AI 기능을 추가했습니다.

실시간 GitHub 분석에서는 다음 데이터를 AI에게 전달합니다.

```text
┌──────────────────────────────┐
│       정량적 활동 데이터       │
├──────────────────────────────┤
│ 총 커밋 수                   │
│ 야간 커밋 비율                │
│ 주말 커밋 비율                │
│ 위험도                       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Git Commit Message     │
├──────────────────────────────┤
│ 실제 개발자가 작성한 커밋 메시지 │
└──────────────┬───────────────┘
               │
               ▼
        🤖 Local LLM
               │
               ▼
┌──────────────────────────────┐
│      AI 번아웃 분석 리포트      │
├──────────────────────────────┤
│ • 활동 패턴 분석               │
│ • 스트레스 가능성 분석          │
│ • 커밋 문맥 분석               │
│ • 관리자 행동 가이드            │
└──────────────────────────────┘
```

AI 분석에는 **LM Studio에서 실행되는 Local LLM**을 사용하여 외부 API에 의존하지 않는 구조로 구현했습니다.

---

# 🧠 AI 분석 방식

AI에게 다음과 같은 정보를 전달하여 분석하도록 구성했습니다.

### 정량 데이터

```text
총 커밋 수
야간 커밋 비율
주말 커밋 비율
예측 위험 등급
```

### 정성 데이터

```text
실제 GitHub Commit Message
```

이를 함께 분석하여 단순히

> "야간 커밋이 많다."

에서 끝나는 것이 아니라,

> "최근 활동 패턴과 커밋 메시지에서 반복적인 오류 수정이나 긴급한 작업의 흔적이 나타나는가?"

와 같은 **문맥 기반 분석**을 시도했습니다.

---

# 🏗️ 시스템 구성

```text
                 ┌───────────────────┐
                 │   GitHub Public   │
                 │    Repository     │
                 └─────────┬─────────┘
                           │
                       GitHub API
                           │
                           ▼
┌─────────────────────────────────────────┐
│              Data Collection            │
│                                         │
│  Commit Date / Author / Message         │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│             Data Processing             │
│                                         │
│  • 야간 커밋 여부                        │
│  • 주말 커밋 여부                        │
│  • 커밋 빈도                            │
│  • 개발자별 집계                         │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          Burnout Risk Analysis          │
│                                         │
│       Burnout Score / Risk Level        │
└───────────────┬─────────────┬───────────┘
                │             │
                ▼             ▼
       ┌─────────────┐  ┌──────────────┐
       │ Streamlit   │  │   Local LLM  │
       │ Dashboard   │  │ LM Studio    │
       └──────┬──────┘  └──────┬───────┘
              │                │
              └───────┬────────┘
                      ▼
             📊 Burnout Dashboard
```

---

# 🧪 데이터 분석 및 모델링

프로젝트에는 다음과 같은 데이터 처리 및 모델링 과정이 포함되어 있습니다.

### 데이터 전처리

- GitHub Commit 데이터 정제
- 날짜 및 시간 데이터 변환
- 개발자별 데이터 집계
- 주차 단위 데이터 변환
- 야간 / 주말 활동 여부 파생변수 생성
- 지표 표준화

### 이상치 탐지

`Isolation Forest`를 활용하여 개발자의 활동 패턴에서 일반적인 범위를 벗어나는 데이터를 탐지할 수 있도록 구성했습니다.

### Scaling

`MinMaxScaler`를 사용하여 분석에 사용되는 지표를 정규화합니다.

---

# 🛠️ 기술 스택

| Category | Technology |
|:---:|:---|
| Language | 🐍 Python |
| Dashboard | 🎈 Streamlit |
| Data Analysis | 🐼 Pandas |
| Visualization | 📊 Plotly |
| GitHub API | 🐙 PyGithub |
| Machine Learning | 🤖 Scikit-learn |
| Anomaly Detection | Isolation Forest |
| Data Scaling | MinMaxScaler |
| AI / LLM | 🧠 LM Studio |
| LLM Model | Gemma |
| Development | Jupyter Notebook |

---

# 📂 프로젝트 구조

```text
DataMining_project/
│
└── DataMining_project/
    │
    ├── 📁 data/
    │   └── burnout_processed_data.csv
    │
    ├── 📁 models/
    │   ├── baseline_stats.csv
    │   ├── global_stats.pkl
    │   ├── isolation_forest_burnout.pkl
    │   └── minmax_scaler_burnout.pkl
    │
    ├── 📓 DataMining_github_commit.ipynb
    ├── 📓 데이터보기.ipynb
    │
    ├── 🖥️ git_streamlit.py
    ├── 🖥️ git_streamlit_v1.py
    └── 🖥️ git_streamlit_v2.py
```

---

# 🔄 데이터 분석 Pipeline

전체 프로젝트는 다음 단계로 진행됩니다.

### STEP 01. GitHub 데이터 수집

GitHub Repository의 Commit 데이터를 수집합니다.

### STEP 02. 데이터 전처리

수집한 데이터를 개발자 및 주차 단위로 정리합니다.

### STEP 03. Feature Engineering

다음과 같은 분석 변수를 생성합니다.

```text
Commit Count
Late Night Ratio
Weekend Ratio
Z-Score
Burnout Score
Risk Level
```

### STEP 04. 이상치 탐지

Isolation Forest를 활용하여 비정상적인 활동 패턴을 탐지합니다.

### STEP 05. 번아웃 지표 생성

개발자의 활동 패턴을 종합하여 번아웃 관련 지표를 생성합니다.

### STEP 06. Dashboard 구현

Streamlit과 Plotly를 이용하여 분석 결과를 시각화합니다.

### STEP 07. 실시간 GitHub 분석

사용자가 입력한 Public Repository에서 최신 커밋 데이터를 가져와 실시간 분석을 수행합니다.

### STEP 08. AI 진단

정량적 활동 지표와 실제 Commit Message를 Local LLM에 전달하여 AI 분석 리포트를 생성합니다.

---

# 🚀 실행 방법

## 1. Repository Clone

```bash
git clone https://github.com/seungjoo555/DataMining_project.git

cd DataMining_project/DataMining_project
```

## 2. 필요한 라이브러리 설치

```bash
pip install streamlit pandas plotly PyGithub openai scikit-learn
```

## 3. Streamlit 실행

```bash
streamlit run git_streamlit_v2.py
```

실행 후 브라우저에서 Streamlit 대시보드에 접속합니다.

---

# 🤖 Local LLM 설정

AI 분석 기능을 사용하기 위해 **LM Studio**가 실행되어 있어야 합니다.

현재 프로그램은 OpenAI 호환 API 형태로 Local LLM에 연결하도록 구성되어 있습니다.

```python
client = openai.OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)
```

즉,

```text
Streamlit
    ↓
OpenAI Compatible API
    ↓
LM Studio
    ↓
Local LLM
    ↓
AI 분석 결과
```

형태로 동작합니다.

> 💡 AI 기능을 사용하지 않는 경우에도 데이터 분석 및 Streamlit 대시보드 기능은 별도로 활용할 수 있습니다.

---

# 🌐 실시간 GitHub 사용 방법

Streamlit 실행 후 사이드바의

```text
🌐 실시간 GitHub 연동 (Public)
```

영역에 분석하고 싶은 Public Repository를 입력합니다.

예:

```text
python/cpython
```

그 다음

```text
🚀 실시간 커밋 메시지 가져오기
```

버튼을 클릭하면 GitHub API를 통해 커밋 데이터를 가져옵니다.

이후 다음 정보를 확인할 수 있습니다.

- 총 커밋 수
- 야간 커밋 비율
- 주말 커밋 비율
- 실시간 번아웃 지수
- 위험도
- 개발자별 활동 현황
- 실제 Commit Message
- AI 기반 분석 결과

---

# 📊 Dashboard 구성

```text
┌────────────────────────────────────────────┐
│ 📊 개발 팀 협업 건강도 및 번아웃 예측 대시보드 │
├────────────────────────────────────────────┤
│                                            │
│  👨‍💻 개발자 수   🔥 위험   ⚠️ 주의   🗓️ 주차   │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  🚨 위험군 목록       📈 번아웃 추이        │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  👤 개발자 상세 분석                         │
│                                            │
│  Burnout Score       Late Night / Weekend │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  🌐 LIVE GitHub 분석                        │
│                                            │
│  📊 실시간 지표       📝 데이터 명세         │
│                                            │
├────────────────────────────────────────────┤
│                                            │
│  🤖 AI 기반 실시간 커밋 문맥 분석             │
│                                            │
└────────────────────────────────────────────┘
```

---

# 💡 프로젝트에서 배운 점

### 1. 데이터 분석에서 Feature Engineering의 중요성

원본 GitHub Commit 데이터만으로는 번아웃을 직접적으로 판단하기 어렵기 때문에 분석 목적에 맞는 새로운 지표를 생성하는 과정이 중요했습니다.

특히 단순한 커밋 개수보다

```text
언제 커밋했는가?
```

를 분석하는 것이 중요하다고 판단했습니다.

---

### 2. 과거 데이터 분석과 실시간 데이터 분석의 차이

사전에 가공된 데이터셋을 분석하는 것과 실제 GitHub Repository에서 데이터를 가져와 즉시 분석하는 것은 데이터 처리 방식과 예외 상황에서 차이가 있었습니다.

이를 해결하기 위해

```text
Historical Data
+
Live GitHub Data
```

두 가지 분석 방식을 하나의 대시보드에서 제공하도록 구성했습니다.

---

### 3. 정량 데이터와 정성 데이터의 결합

단순한 수치 분석의 한계를 보완하기 위해 실제 Commit Message를 AI 분석에 활용했습니다.

```text
정량 데이터
+
텍스트 데이터
+
LLM
```

을 결합하여 보다 다양한 관점에서 개발자 활동 패턴을 분석할 수 있도록 구현했습니다.

---

# ⚠️ 한계점 및 주의사항

이 프로젝트에서 계산하는 번아웃 지수는 **의학적 또는 심리학적 번아웃 진단 도구가 아닙니다.**

GitHub 활동 데이터만으로 실제 개발자의 정신적 상태를 정확하게 판단할 수 없으며, 다음과 같은 한계가 존재합니다.

- GitHub를 사용하지 않는 업무 활동은 반영되지 않음
- 개인별 업무 방식의 차이를 완전히 반영하기 어려움
- 커밋 시간만으로 실제 근무 시간을 판단할 수 없음
- 커밋을 몰아서 작성하는 개발자의 패턴이 왜곡될 수 있음
- 개인적인 사정이나 프로젝트 특성을 반영하기 어려움
- Commit Message만으로 개발자의 심리 상태를 확정할 수 없음

따라서 본 프로젝트는 **실제 번아웃을 진단하는 시스템이 아니라, 개발자의 업무 패턴에서 나타나는 잠재적인 위험 신호를 조기에 확인하기 위한 데이터 분석 프로젝트​**로 보는 것이 적절합니다.

---

# 🔮 향후 개선 방향

### 📌 1. 다양한 개발 활동 데이터 추가

GitHub Commit 데이터뿐만 아니라 다음 데이터를 추가하면 보다 정교한 분석이 가능할 것으로 예상됩니다.

```text
GitHub
 ├── Commit
 ├── Pull Request
 ├── Issue
 └── Review

+

Slack / Jira / Calendar
```

---

### 📌 2. 개인별 Baseline 적용

모든 개발자에게 동일한 기준을 적용하는 대신,

```text
개인별 평소 활동량
        ↓
개인별 Baseline 생성
        ↓
현재 활동량과 비교
        ↓
급격한 변화 탐지
```

방식으로 개선할 수 있습니다.

---

### 📌 3. 시계열 기반 번아웃 예측

현재 상태를 판단하는 것에서 더 나아가,

```text
최근 1주
   ↓
최근 2주
   ↓
최근 4주
   ↓
활동 패턴 변화
   ↓
향후 위험도 예측
```

형태의 시계열 분석을 적용할 수 있습니다.

---

### 📌 4. 더욱 다양한 머신러닝 모델 적용

현재의 이상치 탐지 모델 외에도 다음과 같은 모델을 비교할 수 있습니다.

- Random Forest
- XGBoost
- LightGBM
- Logistic Regression
- Gradient Boosting
- Time Series Model

이를 통해 번아웃 위험도 예측 성능을 비교하고 개선할 수 있습니다.

---

# 🎓 프로젝트 의의

이 프로젝트의 핵심은 단순히 GitHub 데이터를 시각화하는 것에 있지 않습니다.

> **개발자의 업무 활동 데이터를 데이터 마이닝 관점에서 분석하고, 이를 실제 사용할 수 있는 모니터링 서비스 형태로 구현하는 것**

을 목표로 했습니다.

```text
GitHub Data
     ↓
Data Mining
     ↓
Feature Engineering
     ↓
Machine Learning
     ↓
Burnout Risk Detection
     ↓
Streamlit Dashboard
     ↓
Real-time GitHub Analysis
     ↓
AI-powered Diagnosis
```

데이터 수집부터 전처리, 모델링, 시각화, 웹 대시보드 구현, 실시간 API 연동, Local LLM 연동까지 **데이터 분석 프로젝트의 전체 흐름을 경험하는 것**을 목표로 개발했습니다.

---

# 👨‍💻 Developer

**이승주**

Data Mining Project

- 🐙 GitHub: [seungjoo555](https://github.com/seungjoo555)
- 📂 Repository: [DataMining_project](https://github.com/seungjoo555/DataMining_project)

---

<div align="center">

### 🧠 Developer Burnout Monitoring Dashboard

**"데이터로 개발자의 건강한 개발 문화를 고민하다."**

⭐ If you found this project interesting, please consider giving it a star!

</div>