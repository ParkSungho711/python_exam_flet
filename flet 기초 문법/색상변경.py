# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 네모 박스를 만들기 위한 Container 객체
    # width와 height는 가로, 세로 크기
    # bgcolor는 배경 색깔을 의미한다
    box = ft.Container(
        width=100,
        height=100,
        bgcolor="blue"
    )

    # "색 변경" 버튼을 눌렀을 때 실행되는 함수
    def change(e):

        # 박스의 배경 색깔을 파란색에서 빨간색으로 바꾼다
        box.bgcolor = "red"

        # 변경된 색깔이 화면에 보이도록 화면을 다시 그린다
        page.update()

    # 화면에 박스와 버튼을 추가한다
    page.add(

        # 색이 바뀔 네모 박스
        box,

        # 클릭하면 change 함수가 실행되는 버튼
        ft.ElevatedButton("색 변경", on_click=change)
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
