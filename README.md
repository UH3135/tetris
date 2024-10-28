## 프로젝트 설명

- pygame을 이용하여 Teteris 게임 구현

## SPRINT 전략 적용

## 목표

블록 생성, 블록 제거 조건, GUI, 게임 시작 및 오버 만 구현

## 목적

테트리스 게임이 돌아가도록

## 마일스톤

- GUI 화면 출력 (모든 board 값 0 으로 초기화)
- Piece 구현(piece.js)
  - piece 화면에 출력
  - piece 움직임 구현 (왼쪽, 오른쪽, 다운, 기본적인 다운 움직임)
  - 충돌 조건 추가(움직이기 전에 확인) : piece가 밖으로 못나가게 설정 -> 하드 드롭 설정
  - piece 회전 구현 : 행렬 활용
  - piece 랜덤화 : 랜덤하게 piece가 나오도록
- 게임 루프 구현(main.js / board.js)
  - 시간에 따라 내려오도록
  - 보드에 고정된 piece와 충돌감지 추가
  - 블럭이 멈추면 다음 블록 생성
  - piece 제거 조건 구현
  - 게임 오버 조건 구현 : 남아있는 행이 없으면 멈추도록

참조: https://github.com/melcor76/js-tetris

make with pygame
constants는 규칙
board는 보드 클래스
piece는 테트리스 미노 클래스
main에는 게임 초기화와 종료 로직
