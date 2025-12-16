# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤 숫자를 만들기 위해 random 모듈을 불러온다
import random


# 앱이 실행되면 가장 먼저 호출되는 메인 함수
def main(page: ft.Page):

    # 점수를 저장할 변수 (처음 점수는 0)
    score = 0

    # 1부터 10 사이의 랜덤 숫자 두 개를 생성
    a, b = random.randint(1, 10), random.randint(1, 10)

    # 사용자에게 문제를 보여줄 입력창
    # label에 계산 문제를 표시한다
    tf = ft.TextField(label=f"{a} + {b} = ?")

    # 결과(정답/오답, 점수)를 보여줄 텍스트
    result = ft.Text()

    # 확인 버튼을 눌렀을 때 실행되는 함수
    def check(e):
        # 바깥(main 함수)의 변수들을 수정하겠다는 선언
        nonlocal score, a, b

        # 입력한 값이 정답인지 확인
        if int(tf.value) == a + b:
            # 정답이면 점수를 1 증가
            score += 1
            # 정답 메시지와 현재 점수 표시
            result.value = f"정답! 점수: {score}"
        else:
            # 오답이면 점수는 그대로 두고 메시지만 변경
            result.value = f"틀림! 점수: {score}"

        # 새로운 문제를 만들기 위해 다시 랜덤 숫자 생성
        a, b = random.randint(1, 10), random.randint(1, 10)

        # 입력창의 문제(label)를 새 문제로 변경
        tf.label = f"{a} + {b} = ?"

        # 이전에 입력한 값을 지운다
        tf.value = ""

        # 변경된 내용을 화면에 반영
        page.update()

    # 화면에 보여줄 요소들을 추가
    page.add(
        # 앱 제목
        ft.Text("🧠 계산 퀴즈", size=25),

        # 숫자를 입력하는 텍스트 필드
        tf,

        # 정답 확인 버튼
        ft.ElevatedButton("확인", on_click=check),

        # 결과 출력 텍스트
        result
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
