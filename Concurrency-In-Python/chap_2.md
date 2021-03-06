# 병렬화

## 동시성 시스템의 특징
- 다영한 구성 : 여러 프로세서와 스레드가 각자 작업에 임하는 것
- 자원 공유 : 메모리, 디스크 등의 자원 구성 활용
- 규칙 : 락 획득, 메모리 접근, 상태 변경 등..

## I/O 문제
- 입출력에 많은 시간이 소모되는 장애 의미

## 병렬화
- 동시성: 여러 작업을 동시에 처리하는 구성
- 병렬화는 여러 작업을 동시에 실행하고 계산한다는 뜻으로 동시에 코드 실행할 멀티 프로세서가 필요

## CPU
### 단일코어 CPU
- 단일코어프로세서는 주어진 시간에 활용가능한 스레드가 1개
- 컨텍스트 스위치: 스레드간 스위칭
- 장점
    - 여러 코어간 복잡한 통신 프로토콜이 필요 없음
    - 작은 전력 소모
- 단점
    - 처리 속도의 한계
    - 방열 문제

- 클록 속도
    - 단일코어 애플리케이션의 가장 큰 제한
    - 초당 몇번의 클록 사이클이 일어나는지가 중요
    - *마르텔리 범용성 모델

- 시분할(작업 스케쥴러)
