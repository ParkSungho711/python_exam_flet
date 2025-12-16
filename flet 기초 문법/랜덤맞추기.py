# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤 숫자를 만들기 위해 random 라이브러리를 불러온다
import random


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 1부터 10 사이의 숫자 중 하나를 랜덤으로 선택해서 정답으로 저장한다
    answer = random.randint(1, 10)

    # 사용자가 숫자를 입력할 수 있는 입력창을 만든다
    # label은 입력창 위에 보이는 안내 문구이다
    input_num = ft.TextField(label="1~10 입력")

    # 결과 메시지를 화면에 보여주기 위한 텍스트
    msg = ft.Text("")

    # "확인" 버튼을 눌렀을 때 실행되는 함수
    def check(e):

        # 입력창에 적은 값을 정수(int)로 바꿔서 정답과 비교한다
        if int(input_num.value) == answer:
            # 맞았을 때 화면에 보여줄 메시지
            msg.value = "🎉 정답!"
        else:
            # 틀렸을 때 화면에 보여줄 메시지
            msg.value = "❌ 틀림"

        # 변경된 내용을 화면에 반영한다
        page.update()

    # 화면에 입력창, 버튼, 결과 메시지를 추가한다
    page.add(
        input_num,
        ft.ElevatedButton("확인", on_click=check),
        msg
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
