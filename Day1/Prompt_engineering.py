from openai import OpenAI
import yaml

# YAML 파일 로드
with open("../openai_key.yaml", "r") as file:
    config = yaml.safe_load(file)

# OpenAI API Key 설정
client = OpenAI(api_key=config.get("api_key"))


######## Auto Prompting 1 ########
# gpt-4o 모델을 사용하여 아래 예시 프롬프트를 생성하게
example_prompt = '''I need to triage support requests that come in via SMS. I can route to Tier 1, Tier 2, or Tier 3 support - or in rare cases I can page our on-call engineer.

Please write a prompt that review inbound messages, then proposes a triage decision along with a separate one sentence justification.'''

# response = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#         {"role": "user", "content": example_prompt},
#     ]
# )
#
# print(response.choices[0].message.content)
'''
### 결과 예시 ###
Certainly! Below is a prompt you can use to triage support requests coming in via SMS, propose a triage decision, and provide a one-sentence justification:

---

**SMS Analysis and Triage Assistant**

**Inbound Message:**
"{SMS Text}"

**Triage Decision:**
[ ] Tier 1
[ ] Tier 2
[ ] Tier 3
[ ] Page On-Call Engineer

**Justification:**
"{One-sentence justification for decision}"

---

**Example:**

**Inbound Message:**
"I can't login to my account and keep getting an error message."

**Triage Decision:**
[X] Tier 1
[ ] Tier 2
[ ] Tier 3
[ ] Page On-Call Engineer

**Justification:**
"Basic login issues are typically handled by Tier 1 support."

---

You can replace the placeholders with the actual content of each SMS and your decision, which will help streamline the triage process efficiently.
'''


######## Auto Prompting 2 ########
# 위에 같은 예시 프로프트를 구글 번역결과를 통해서 모델에게 자동으로 프롬프트를 생성하게
example_prompt='''
SMS를 통해 들어오는 지원 요청을 분류해야 합니다. Tier 1, Tier 2 또는 Tier 3 지원팀으로 라우트할 수 있습니다. 또는 드물지만 대기 중인 엔지니어에게 호출할 수도 있습니다.

인바운드 메시지를 검토한 다음 별도의 한 문장 근거와 함께 분류 결정을 제안하는 프롬프트를 작성하세요.'''

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
        {"role": "user", "content": example_prompt},
    ]
)

print(response.choices[0].message.content)
'''
### 결과 예시 ###
물론입니다. 다음은 인바운드 지원 요청을 검토하고, 그 요청을 적절한 지원 팀(Tier 1, Tier 2, Tier 3)이나 대기 중인 엔지니어에게 라우트하도록 도움을 주는 프롬프트 예시입니다.

---

**인바운드 메시지**: "저희 시스템에서 로그인할 수 없으며, 자격 증명이 계속 거부됩니다."

**분류 결정**: Tier 1

**근거**: 로그인 문제는 일반적으로 Tier 1 지원팀에서 해결할 수 있는 기본적인 자격 증명 문제에 해당합니다.

---

**인바운드 메시지**: "서버가 다운되어 모든 내부 애플리케이션에 액세스할 수 없습니다."

**분류 결정**: Tier 3

**근거**: 서버 다운과 관련된 문제는 고급 기술 지원이 필요하며, 이는 일반적으로 Tier 3 지원팀의 영역입니다.

---

**인바운드 메시지**: "최근 소프트웨어 업데이트 이후 시스템이 불규칙하게 작동합니다."

**분류 결정**: Tier 2

**근거**: 소프트웨어 업데이트로 인한 시스템 불규칙성 문제는 중간 수준의 기술 지원이 필요할 수 있으며, 이는 Tier 2 팀이 적합합니다.

---

**인바운드 메시지**: "전사적인 서비스 장애 발생, 고객 데이터에 접근 불가"

**분류 결정**: 엔지니어 호출

**근거**: 전사적인 서비스 장애 및 고객 데이터 접근 문제는 긴급한 상황이며 즉각적인 해결이 필요하므로 대기 중인 엔지니어를 호출해야 합니다.

---

이 프롬프트를 사용하면 인바운드 메시지를 고려하여 적절한 지원 경로를 결정하고 그 결정의 근거를 명확하게 제시할 수 있습니다.
'''