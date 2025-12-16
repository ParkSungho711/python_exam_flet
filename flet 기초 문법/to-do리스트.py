# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 할 일을 입력받기 위한 입력창
    # label은 입력창 위에 보이는 안내 문구이다
    todo = ft.TextField(label="할 일 입력")

    # 여러 개의 할 일을 세로로 쌓아서 보여주기 위한 Column 객체
    list_view = ft.Column()

    # "추가" 버튼을 눌렀을 때 실행되는 함수
    def add(e):

        # 입력창에 적힌 내용을 Text 객체로 만들어 리스트에 추가한다
        list_view.controls.append(ft.Text(todo.value))

        # 입력이 끝났으므로 입력창을 다시 비운다
        todo.value = ""

        # 변경된 리스트가 화면에 보이도록 화면을 다시 그린다
        page.update()

    # 화면에 입력창, 버튼, 할 일 목록을 추가한다
    page.add(

        # 할 일을 입력하는 입력창
        todo,

        # 클릭하면 add 함수가 실행되는 버튼
        ft.ElevatedButton("추가", on_click=add),

        # 추가된 할 일들이 표시될 영역
        list_view
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
