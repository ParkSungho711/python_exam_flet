# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤으로 명언을 선택하기 위해 random 라이브러리를 불러온다
import random


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 여러 개의 명언을 리스트로 저장한다
    quotes = [
        "포기하지 마!",
        "넌 할 수 있어",
        "오늘도 최고야"
    ]

    # 화면에 명언을 보여줄 텍스트 객체
    # 처음에는 안내 문구를 표시한다
    text = ft.Text("버튼을 눌러봐")

    # "명언 보기" 버튼을 눌렀을 때 실행되는 함수
    def show(e):

        # 명언 리스트 중에서 하나를 랜덤으로 선택한다
        text.value = random.choice(quotes)

        # 바뀐 명언이 화면에 보이도록 화면을 다시 그린다
        page.update()

    # 화면에 텍스트와 버튼을 추가한다
    page.add(

        # 명언을 보여줄 텍스트
        text,

        # 클릭하면 show 함수가 실행되는 버튼
        ft.ElevatedButton("명언 보기", on_click=show)
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
