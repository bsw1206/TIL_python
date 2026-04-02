# 🚀 [프로젝트 기록] VLM 파인튜닝 데이터 파이프라인 설계 및 고도화 (Baseline → Ver.6)
## 👤 담당 역할: Member 1 (Data Pipeline Engineer)
목표: 대용량 시각-언어 데이터셋의 전처리 병목(Bottleneck) 현상을 해결하여 GPU 학습 처리량(Throughput)을 극대화하고, 데이터 무결성 및 증강 기법을 도입하여 모델의 최종 예측 성능을 향상시킨다.

# 🛠️ 핵심 기여 및 기술적 성과 (Key Contributions)
### 1. 전처리 연산 오프라인화 및 캐싱 (Pre-computation & Caching)
AS-IS (Baseline): __getitem__ 내에서 매 에폭(Epoch)마다 이미지 리사이징 및 패딩 연산(letterbox_image)이 반복 실행되어 심각한 CPU 연산 병목 및 디스크 I/O 지연 발생.

TO-BE (Ver.6): * 학습 루프 진입 전, 전체 이미지 데이터셋에 대해 1회성으로 전처리를 완료하고 로컬에 저장하는 precompute_images 파이프라인 구축.

성과: 매 Step마다 발생하던 무거운 이미지 변환 연산 비용을 O(N)에서 O(1) 단순 로드 수준으로 단축하여, GPU Starvation(데이터 대기 현상)을 완벽히 해소하고 학습 속도 비약적 상승.

### 2. 다수결 기반 노이즈 데이터 필터링 (High-Quality Validation Setup)
AS-IS (Baseline): 단순히 train_test_split을 사용하여 검증셋을 구성하거나, 라벨러 간 의견 불일치(Noise)가 존재하는 dev.csv 데이터를 그대로 사용.

TO-BE (Ver.6): * 5인의 라벨러 응답을 분석하여 다수결(Majority Voting)로 Hard Label을 추출하고, 4인 이상이 동의한 확실한 정답만을 필터링하는 filter_high_quality_dev 로직 구현.

성과: 검증(Validation) 지표의 신뢰도를 대폭 향상시켜, Early Stopping 및 Best Model 저장 시 과적합을 방지하는 견고한 기준선 마련.

### 3. GPU 가동률 100%를 위한 멀티프로세싱 최적화
AS-IS (Baseline): DataLoader가 단일 프로세스(num_workers=0)로 동작하며, 페이저블 메모리 사용으로 인해 CPU-GPU 간 데이터 전송 지연 발생.

TO-BE (Ver.6): * num_workers=4 할당 및 pin_memory=True 옵션을 적용하여 데이터 로딩 병렬화 및 VRAM 직통 고속도로 개통.

성과: 데이터 준비와 모델 전파(Forward)를 비동기적으로 처리하여 학습 시간(Epoch 런타임) 단축.

### 4. 동적 프롬프트 증강 (Dynamic Prompt Augmentation)
AS-IS (Baseline): 모든 학습 단계에서 고정된 텍스트 템플릿 사용.

TO-BE (Ver.6): * OptimizedVQADataset 클래스 내에 is_train=True 플래그를 도입하여, 질문의 어투와 구조를 랜덤하게 변형(2가지 버전)하여 제공하는 동적 프롬프트 생성기 구현.

성과: 별도의 외부 데이터 수집 없이 텍스트 다양성을 확보하여, VLM이 특정 텍스트 패턴에 과적합(Overfitting)되는 현상 방지.

### 5. Advanced 파이프라인: K-Fold & TTA 통합 환경 구축
클래스 균형 및 K-Fold 파이프라인 (create_kfold_dataloaders): * 제한된 데이터를 100% 활용하기 위해 정답 비율을 유지하는 5-Fold 교차 검증 제너레이터 구축.

WeightedRandomSampler를 장착하여 정답 클래스 간의 데이터 불균형 완벽 해소.

추론 안정화 TTA 파이프라인 (TTAVQADataset): * 추론 시 1장의 원본 이미지 요청을 받아 [원본, 좌우 반전, 밝기 조절] 총 3장의 변형된(Augmented) 배치 데이터로 묶어 반환하는 클래스 독자 개발.

Member 2(추론 담당)와 Member 3(학습 담당)가 코드 구조를 크게 바꾸지 않고도 앙상블 및 예측 신뢰도 향상을 이뤄낼 수 있도록 인프라 제공.

### 6. 트러블슈팅 및 파이프라인 무결성 방어 (Troubleshooting)
성과: 파이프라인 통합 과정에서 발생한 핵심 전처리 함수(letterbox_image) 누락 및 주피터 노트북 환경 특유의 메모리 상태 꼬임(Execution Order) 에러를 주도적으로 추적하고 해결하여 정상적인 전체 데이터 흐름(Data Flow) 복구.

# 📈 최종 요약 (Impact)
데이터 엔지니어로서 학습과 추론의 **'길'**을 닦는 데 집중했습니다. 모델의 파라미터나 학습 알고리즘을 직접 건드리지 않고도, 입력 데이터의 무결성을 정제하고 병목 구간을 하드웨어(CPU/RAM) 수준에서 최적화함으로써 전체 프로젝트의 학습 처리량과 최종 성능(Accuracy)을 견인하는 핵심적인 역할을 수행했습니다.