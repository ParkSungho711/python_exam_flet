# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤 숫자를 만들기 위해 random 라이브러리를 불러온다
import random


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 1부터 20 사이의 숫자 중 하나를 랜덤으로 선택해서 정답으로 저장한다
    answer = random.randint(1, 20)

    # 사용자가 숫자를 입력할 수 있는 입력창을 만든다
    # 아무 값도 넣지 않으면 기본 입력창이 생성된다
    input_num = ft.TextField()

    # UP, DOWN, 정답 결과를 화면에 보여줄 텍스트
    msg = ft.Text()

    # "확인" 버튼을 눌렀을 때 실행되는 함수
    def check(e):

        # 입력창에 적힌 값을 정수(int)로 바꿔서 n에 저장한다
        n = int(input_num.value)

        # 입력한 숫자가 정답보다 크면 DOWN 표시
        if n > answer:
            msg.value = "DOWN"

        # 입력한 숫자가 정답보다 작으면 UP 표시
        elif n < answer:
            msg.value = "UP"

        # 입력한 숫자와 정답이 같으면 정답 표시
        else:
            msg.value = "정답!"

        # 변경된 메시지가 화면에 보이도록 화면을 다시 그린다
        page.update()

    # 화면에 입력창, 버튼, 결과 메시지를 추가한다
    page.add(
        input_num,
        ft.ElevatedButton("확인", on_click=check),
        msg
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
