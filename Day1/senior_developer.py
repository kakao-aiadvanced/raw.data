# 참고: https://www.feedough.com/ai-prompt-generator/
from openai import OpenAI
import yaml

# YAML 파일 로드
with open("../openai_key.yaml", "r") as file:
    config = yaml.safe_load(file)

# OpenAI API Key 설정
client = OpenAI(api_key=config.get("api_key"))


system_prompt = '''
You’re a seasoned senior developer with over 10 years of experience in software development, specializing in creating robust applications and leading technical teams. You excel in programming languages such as Java, Python, and JavaScript, and you have a deep understanding of software architecture and design patterns.

Your task is to provide detailed answers to questions about software development, best practices, and technology trends. Here are some parameters for your responses -
- Specific topic or technology:
- Experience level of the person asking:
- Type of question (e.g., coding challenge, architectural decision, debugging issue):
- Context or background information (if any) related to the question:

Keep in mind the importance of clarity and conciseness in your explanations, and make sure to include practical examples or analogies where applicable to enhance understanding.'''

prompt = "DDD에 대해서 자세히 설명해줘."

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
        {"role": "user", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
)

print(response.choices[0].message.content)

'''
### 결과 예시 ###
물론입니다! 도메인 주도 설계(DDD, Domain-Driven Design)는 복잡한 소프트웨어 시스템을 개발할 때 유용한 접근 방식입니다. 이 접근 방식은 소프트웨어의 핵심 도메인과 로직에 집중하고, 이를 기반으로 시스템을 설계하는 것을 목표로 합니다. DDD는 주로 대형 엔터프라이즈 애플리케이션이나 복잡한 비즈니스 로직을 다루는 시스템에서 많이 사용됩니다.

### DDD의 핵심 개념

1. **도메인 (Domain)**:
   - 도메인은 우리가 해결하고자 하는 문제 영역입니다. 예를 들어 은행 시스템에서는 '계좌', '거래', '고객' 등이 도메인이 될 수 있습니다.

2. **유비쿼터스 언어 (Ubiquitous Language)**:
   - 개발자, 도메인 전문가, 이해관계자 등이 공통으로 이해할 수 있는 언어입니다. 이는 도메인 전문가와 개발자 사이의 의사소통의 격차를 줄여줍니다.

3. **바운디드 컨텍스트 (Bounded Context)**:
   - 큰 도메인을 유사한 문제를 해결하는 작은 영역으로 나누는 방법입니다. 각각의 바운디드 컨텍스트는 독립적으로 모델링되고, 다른 바운디드 컨텍스트와 명확히 구분됩니다. 은행 시스템에서는 '고객 관리', '계좌 관리', '거래 처리' 등이 바운디드 컨텍스트가 될 수 있습니다.

4. **엔터프라이즈 패턴**:
   - 엔티티(Entity), 값 객체(Value Object), 집합체(Aggregate), 리포지토리(Repository), 서비스(Service) 등의 패턴을 사용하여 도메인을 모델링합니다.

### 실예

예를 들어, 은행 애플리케이션의 '계좌 관리' 바운디드 컨텍스트를 생각해봅시다.

- **유비쿼터스 언어**:
  - "계좌 개설", "예금", "출금", "잔액 확인" 등의 용어를 정의하고 도메인 전문가와 개발자가 이를 일관되게 사용합니다.

- **엔티티**:
  ```java
  public class Account {
      private String accountId;
      private Money balance;

      // 도메인 로직
      public void deposit(Money amount) {
          // 예금 로직
          this.balance = this.balance.add(amount);
      }

      public void withdraw(Money amount) throws InsufficientFundsException {
          if (this.balance.isLessThan(amount)) {
              throw new InsufficientFundsException();
          }
          this.balance = this.balance.subtract(amount);
      }
  }
  ```

- **값 객체**:
  ```java
  public class Money {
      private BigDecimal amount;
      // 불변 객체로 구현합니다
      public Money(BigDecimal amount) {
          this.amount = amount;
      }

      public Money add(Money other) {
          return new Money(this.amount.add(other.amount));
      }

      public Money subtract(Money other) {
          return new Money(this.amount.subtract(other.amount));
      }

      public boolean isLessThan(Money other) {
          return this.amount.compareTo(other.amount) < 0;
      }
  }
  ```

- **리포지토리**:
  ```java
  public interface AccountRepository {
      void save(Account account);
      Account findById(String accountId);
  }
  ```

### 장점과 단점

- **장점**:
  - 도메인 전문가와 개발자 사이의 의사소통이 원활해집니다.
  - 복잡한 비즈니스 로직을 체계적으로 관리할 수 있습니다.
  - 시스템의 유연성과 확장성이 높아집니다.

- **단점**:
  - 초기 학습 곡선이 높습니다.
  - 엔터프라이즈 환경에서는 과한 설계가 될 가능성도 있습니다.
  - 팀 내에서 DDD를 준수하는 문화가 필요합니다.

도메인 주도 설계는 시간과 노력이 많이 들지만, 특히 대규모 및 복잡한 시스템에서 많은 이점을 제공합니다. 문제를 도메인 관점에서 접근하고, 명확한 경계를 설정하는 것이 핵심입니다.
'''