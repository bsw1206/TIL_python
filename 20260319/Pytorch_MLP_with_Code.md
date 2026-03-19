[toc]

-----

## **MLP 모델링 실습: PyTorch로 나만의 신경망 만들기**

> 파이썬의 대표적인 딥러닝 라이브러리인 **PyTorch**를 사용해서, 딥러닝의 가장 기본 모델인 MLP(Multi-Layer Perceptron)를 직접 만들고 학습시키는 과정을 단계별로 진행해 보겠습니다.



### **Part 1. PyTorch와 친해지기**

#### **1-1. 왜 PyTorch를 사용할까요?**

PyTorch는 딥러닝 모델을 쉽고 유연하게 만들 수 있도록 도와주는 파이썬 라이브러리입니다. 
과학 계산에 널리 쓰이는 NumPy와 사용법이 매우 유사하지만, 딥러닝에 최적화된 두 가지 강력한 기능을 추가로 제공합니다.

  * **GPU를 활용한 연산 가속** : 단순 CPU 연산이 아닌, GPU의 병렬 처리 능력을 활용해 텐서(행렬) 연산을 매우 빠르게 처리할 수 있습니다.
  * **자동 미분 (AutoGrad)** : 딥러닝 모델이 학습하는 데 필수적인 '미분' 과정을 자동으로 계산해주는 엄청난 기능입니다.



#### **1-2. 기본 단위: 텐서(Tensor) 다루기**

**텐서(Tensor)**는 PyTorch의 가장 기본이 되는 데이터 구조로, 쉽게 말해 **'다차원 배열'**을 의미합니다.

  * 0차원 텐서: 스칼라 (숫자 하나)
  * 1차원 텐서: 벡터
  * 2차원 텐서: 행렬

NumPy의 `ndarray`와 거의 똑같지만, 위에서 언급한 GPU 가속과 자동 미분 기능을 탑재한 **NumPy의 파워 버전**이라고 생각하면 쉽습니다.

```python
import torch

# NumPy와 매우 유사하게 텐서를 생성하고 연산할 수 있습니다.
x = torch.rand(3, 3)
y = torch.ones(3, 3)

# 덧셈
print("x + y:\n", x + y)

# 행렬 곱셈 (@ 연산자 사용)
# y.T는 y의 전치 행렬을 의미합니다.
print("\nx @ y.T:\n", x @ y.T)
```



#### **1-3. PyTorch의 핵심: 자동 미분(AutoGrad)**

모델이 '학습'을 하려면, 예측이 틀렸을 때 각 부품(파라미터)을 어느 방향으로 얼마나 조절해야 할지 알아야 합니다. 이 '조절 방향과 양'을 **기울기(Gradient)**라고 하며, 기울기를 구하는 과정이 **미분**입니다.

**경사 하강법(Gradient Descent)**은 이 기울기를 이용해 손실(Loss)을 점진적으로 줄여나가는 최적화 알고리즘입니다.

> **경사 하강법 업데이트 공식**
> $$
> θ_new=θ_old−η∇_θL
> $$
>
>   * θ (세타): 모델의 파라미터 (가중치 W, 편향 b)
>   * η (에타): 학습률(Learning Rate). 기울기 방향으로 얼마나 크게 이동할지 결정하는 보폭
>   * L: 손실 함수(Loss Function). 모델의 예측이 얼마나 틀렸는지를 나타내는 지표
>   * ∇θL: **손실 함수 L을 파라미터 θ로 편미분한 기울기.** 손실이 가장 가파르게 **증가**하는 방향을 의미합니다. 우리는 손실을 줄이고 싶으므로 이 값에 **마이너스(-)를 붙여 빼주는 것**입니다.

PyTorch의 **AutoGrad**는 바로 이 복잡한 ∇θL 계산을 자동으로 처리해주는 놀라운 기능입니다. 텐서에 `requires_grad=True` 옵션을 주면, 해당 텐서에 가해지는 모든 연산을 추적하여 `backward()` 함수 호출 한 번으로 모든 기울기를 계산해냅니다.

```python
# requires_grad=True로 설정하여 이 텐서에 대한 모든 연산을 추적하도록 합니다.
x = torch.tensor([2.0, 3.0], requires_grad=True)

# x를 이용한 연산 수행
# y = x^2 + 3x + 1
y = x ** 2 + 3 * x + 1

# 최종 결과 z는 스칼라 값이어야 미분 가능합니다.
z = y.sum()

# z를 x에 대해 미분합니다 (역전파).
z.backward()

# x의 .grad 속성에 계산된 기울기가 저장됩니다.
# 수식 y를 미분하면 2x + 3 이므로,
# x=[2.0, 3.0]을 대입하면 기울기는 [2*2+3, 2*3+3] = [7.0, 9.0]이 됩니다.
print(x.grad)
```



---



### **Part 2. 신경망의 설계도: MLP 이해하기**

MLP는 여러 개의 선형 계층(Linear Layer) 사이에 비선형 활성화 함수(Activation Function)를 추가하여 층층이 쌓아 올린 모델입니다.

>   * **입력층 (Input Layer)**: 데이터가 처음 들어오는 입구입니다.
>   * **은닉층 (Hidden Layer)**: 데이터의 특징을 추출하고 변환하는 중간 처리 과정입니다. 이 층이 깊어질수록 모델은 더 복잡한 패턴을 학습할 수 있습니다.
>   * **출력층 (Output Layer)**: 최종 예측 결과를 내보내는 출구입니다.

#### **2-1. 신경망 모듈 `nn.Module`**

PyTorch에서 모든 신경망 모델은 `nn.Module` 클래스를 상속받아 만듭니다. `nn.Module`은 신경망의 여러 층(Layer)과 학습 가능한 파라미터(가중치, 편향)를 체계적으로 관리해주는 '설계도'와 같습니다.

  * `__init__()` 메서드: 모델에 필요한 부품(레이어, 활성화 함수 등)을 정의합니다.
  * `forward()` 메서드: 데이터가 `__init__`에서 정의된 부품들을 어떤 순서로 통과할지, 즉 '순전파' 과정을 정의합니다.



#### **2-2. 방법 1: 기본에 충실하게 (`nn.Module`)**

가장 기본적인 방법은 `__init__`에서 필요한 레이어를 하나씩 정의하고, `forward`에서 데이터의 흐름을 직접 코드로 작성하는 것입니다.

```python
import torch.nn as nn

class SimpleMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        # nn.Module의 생성자를 필수로 호출해야 합니다.
        super().__init__()

        # nn.Linear: y = xW^T + b 형태의 선형 변환을 수행하는 레이어입니다.
        # 내부적으로 가중치(W)와 편향(b) 텐서를 자동으로 생성하고 초기화합니다.
        self.fc1 = nn.Linear(input_dim, hidden_dim)

        # nn.ReLU: 대표적인 비선형 활성화 함수입니다.
        # ReLU(x) = max(0, x)로, 음수는 0으로 만들고 양수는 그대로 둡니다.
        # 모델이 선형적인 한계를 넘어 복잡한 패턴을 학습할 수 있게 해줍니다.
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # 데이터가 레이어를 순서대로 통과하는 과정을 정의합니다.
        x = self.fc1(x)  # 첫 번째 선형 레이어 통과
        x = self.relu(x) # ReLU 활성화 함수 통과
        x = self.fc2(x)  # 두 번째 선형 레이어 통과
        return x
```



#### **2-3. 방법 2: 똑똑하고 간결하게 (`nn.Sequential`)**

대부분의 모델처럼 데이터가 순차적으로 흐르는 경우, `nn.Sequential`을 사용하면 훨씬 간결하게 모델을 정의할 수 있습니다. `nn.Sequential`은 여러 레이어를 컨테이너처럼 묶어서 순서대로 실행해주는 편리한 도구입니다.

```python
import torch.nn as nn

class SequentialMLP(nn.Module):
    def __init__(self, input_dim, hidden_dims=(128, 64), output_dim=3, dropout=0.2):
        super().__init__()
        h1, h2 = hidden_dims

        self.net = nn.Sequential(
            # 입력층 -> 첫 번째 은닉층
            nn.Linear(input_dim, h1),
            nn.ReLU(),
            # nn.Dropout: 과적합을 방지하기 위한 규제 기법입니다.
            # p의 확률로 일부 뉴런을 학습 중에 랜덤하게 비활성화하여
            # 모델이 특정 뉴런에 과도하게 의존하는 것을 막아줍니다.
            nn.Dropout(p=dropout),

            # 첫 번째 은닉층 -> 두 번째 은닉층
            nn.Linear(h1, h2),
            nn.ReLU(),
            nn.Dropout(p=dropout),

            # 두 번째 은닉층 -> 출력층
            nn.Linear(h2, output_dim)
        )

    def forward(self, x):
        # Sequential 컨테이너를 한 번만 호출하면 데이터가 정의된 순서대로 모든 층을 통과합니다.
        return self.net(x)
```



---



### **Part 3. 실전. MLP 모델 만들고 학습시키기**

이제 위에서 설계한 `SequentialMLP`를 실제로 만들고, 데이터를 입력하여 순전파와 역전파를 실행해 보겠습니다.

#### **3-1. 모델 생성 및 순전파 실행**

먼저, 설계도를 바탕으로 실제 모델 객체를 생성하고, 임의의 더미(dummy) 데이터를 입력하여 예측값이 어떻게 나오는지 확인합니다.

```python
# 재현성을 위해 시드를 고정합니다. (항상 동일한 난수 -> 동일한 가중치 초기화)
torch.manual_seed(42)

# 입력 차원 20, 은닉층 차원 (128, 64), 출력 차원 3인 MLP 모델 생성
model = SequentialMLP(input_dim=20, hidden_dims=(128, 64), output_dim=3)
print("생성된 모델의 구조:\n", model)

# 모델에 입력할 임의의 더미 데이터 생성
# (배치 크기=4, 입력 특성=20)
dummy_input = torch.rand(4, 20)

# 순전파를 실행하여 모델의 예측값(logits)을 얻습니다.
# model(dummy_input)은 내부적으로 model.forward(dummy_input)를 호출합니다.
logits = model(dummy_input)

# 예측값의 크기를 확인합니다. (배치 크기, 출력 차원) 형태가 됩니다.
print("\n예측값(logits)의 크기:", logits.shape)
```



#### **3-2. 역전파(Backpropagation) 실행**

이제 순전파로 얻은 예측값을 실제 정답과 비교하여 **손실(Loss)**을 계산하고, 이 손실을 바탕으로 **역전파**를 실행하여 각 파라미터의 기울기가 계산되는 것을 확인해 보겠습니다.

**[학습 과정 요약]**

1.  **데이터 준비**: 모델에 입력할 데이터(`dummy_input`)와 정답(`dummy_labels`)을 만듭니다.
2.  **순전파**: `model(dummy_input)`을 통해 예측값(`logits`)을 얻습니다.
3.  **손실 계산**: 예측값과 정답을 손실 함수(`CrossEntropyLoss`)에 넣어 오차를 계산합니다.
4.  **역전파**: `loss.backward()`를 호출하여 모든 파라미터의 기울기를 자동으로 계산합니다.
5.  **결과 확인**: 역전파 전후로 파라미터의 `.grad` 속성값이 어떻게 변하는지 확인합니다.

```python
# 1. 고정된 입력 데이터와 정답 레이블을 생성합니다.
# (배치 크기=2, 입력 차원=20)
dummy_input = torch.rand(2, 20)
# (배치 크기=2), 각 샘플의 정답은 0, 1, 2 중 하나
dummy_labels = torch.tensor([1, 0]).long() # CrossEntropyLoss는 정수형(long) 레이블을 기대합니다.


# 2. 순전파를 통해 예측값(logits) 계산
logits = model(dummy_input)


# 다중 클래스 분류 문제에 주로 사용되는 교차 엔트로피 손실 함수
criterion = nn.CrossEntropyLoss()

# 3. 예측값과 정답으로 손실을 계산
loss = criterion(logits, dummy_labels)
print(f"\n계산된 손실(Loss): {loss.item():.4f}")


# 4. 역전파 실행 전, 첫 번째 레이어 가중치의 기울기 확인 (초기값은 None)
print("역전파 전, fc1 가중치의 기울기:", model.net[0].weight.grad)


# 5. 역전파 실행!
# 이 한 줄이 AutoGrad를 통해 모든 파라미터의 기울기를 계산합니다.
loss.backward()


# 6. 역전파 실행 후, .grad 속성에 기울기가 채워진 것을 확인
# 이 기울기 값을 이용해 옵티마이저가 모델의 가중치를 업데이트하게 됩니다.
print("역전파 후, fc1 가중치의 기울기:\n", model.net[0].weight.grad)
```