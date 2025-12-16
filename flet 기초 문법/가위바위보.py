# Flet 라이브러리를 불러오고 이름을 ft로 줄여서 사용한다
import flet as ft

# 랜덤 선택을 하기 위해 random 라이브러리를 불러온다
import random


# Flet 앱이 시작될 때 자동으로 실행되는 함수
# page는 화면 전체를 관리하는 도화지 같은 역할
def main(page: ft.Page):

    # 결과를 화면에 보여주기 위한 텍스트 객체
    # 처음에는 아무 글자도 없도록 빈 문자열로 만든다
    result = ft.Text("")

    # 버튼을 클릭했을 때 실행될 함수
    # e는 "이벤트(event)" 정보가 들어있는 변수
    def play(e):

        # 컴퓨터가 가위, 바위, 보 중에서 하나를 랜덤으로 고른다
        computer = random.choice(["가위", "바위", "보"])

        # 결과 텍스트에 컴퓨터가 고른 값을 표시한다
        result.value = f"컴퓨터: {computer}"

        # 화면을 다시 그려서 변경된 내용이 보이게 한다
        page.update()

    # 화면(page)에 버튼과 텍스트를 추가한다
    page.add(

        # "가위" 버튼을 만들고, 클릭하면 play 함수가 실행되게 한다
        ft.ElevatedButton("가위", on_click=play),

        # "바위" 버튼을 만들고, 클릭하면 play 함수가 실행되게 한다
        ft.ElevatedButton("바위", on_click=play),

        # "보" 버튼을 만들고, 클릭하면 play 함수가 실행되게 한다
        ft.ElevatedButton("보", on_click=play),

        # 컴퓨터 결과를 보여줄 텍스트를 화면에 추가한다
        result
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
