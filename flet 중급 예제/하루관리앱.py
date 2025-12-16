# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤으로 명언을 선택하기 위해 random 모듈을 불러온다
import random


# 앱이 실행되면 가장 먼저 호출되는 메인 함수
def main(page: ft.Page):

    # 할 일을 입력받는 텍스트 필드
    todo = ft.TextField(label="할 일")

    # 할 일 목록을 화면에 쌓아 보여줄 Column 컨테이너
    todos = ft.Column()

    # 명언을 출력할 텍스트
    quote = ft.Text("")

    # 랜덤으로 보여줄 명언 목록
    quotes = ["포기하지 마!", "넌 할 수 있어!", "오늘도 최고야"]

    # "할 일 추가" 버튼을 눌렀을 때 실행되는 함수
    def add(e):
        # 입력한 할 일을 텍스트로 만들어 목록에 추가
        todos.controls.append(
            ft.Text("✔ " + todo.value)
        )

        # 입력창을 비워서 다음 입력을 준비
        todo.value = ""

        # 변경된 내용을 화면에 반영
        page.update()

    # "오늘의 명언" 버튼을 눌렀을 때 실행되는 함수
    def show_quote(e):
        # 명언 목록 중 하나를 랜덤으로 선택
        quote.value = random.choice(quotes)

        # 화면을 새로 고쳐 변경 사항을 반영
        page.update()

    # 화면에 표시할 UI 요소들을 추가
    page.add(
        # 앱 제목
        ft.Text("📅 하루 관리 앱", size=25),

        # 할 일 입력창
        todo,

        # 할 일을 목록에 추가하는 버튼
        ft.ElevatedButton("할 일 추가", on_click=add),

        # 할 일 목록 영역
        todos,

        # UI를 구분하기 위한 구분선
        ft.Divider(),

        # 명언을 보여주는 버튼
        ft.ElevatedButton("오늘의 명언", on_click=show_quote),

        # 선택된 명언을 표시하는 텍스트
        quote
    )


# main 함수를 실행하여 Flet 앱을 시작한다
ft.app(main)
