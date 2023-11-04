##  리팩토리 및 시스템 최적화
- 기존의 프로젝트의 소스코드를 유지보수가 용이한 소스코드로 변경
- 불필요한 기능을 삭제함으로써 시스템 최적화

### 리팩토링
#### 서버
- Djangorestframework를 사용한 RESTFulAPI 구축
- AI팀의 코드를 Django 프레임워크로 이식

#### 클라이언트
- UI: XML -> Jetpackcompose로 전환 선언형 UI 구현
- MVVM패턴적용과 Hilt를 활용한 의존성 주입으로 코드의 결합도를 낮춤.

### 시스템 최적화
#### Push알림 기능을 제거(MQTT 및 Firebase)
- Push알림: 혼잡도가 높은 지역에 도착하면 위험을 알리는 알림
- 기능이 제거된 이유: 이미 도착한 후의 Push알림은 대처가 늦으며 이를 위해 사용된 기술들이 서버의 효율성을 저하시킨다. 
- MQTT프로토콜을 사용한 통신제거 효과:위치와 토큰을 전송하던 MQTT프로토콜을 제거함으로써 다수의 사용자가 연결될 경우 발생할 수 있는 성능 문제예방
- Firebase를 제거한 효과: 자체 서버 인프라를 활용하는 현재의 시스템 구조에서 Firebase의 사용은 중복적인 기능을 제공함으로써 비용적 측면과 유지보수성의 부담을 증가시키므로 제거
