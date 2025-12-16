# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 오늘의 한 줄 일기를 입력받기 위한 입력창
    # label은 입력창 위에 보이는 안내 문구이다
    diary = ft.TextField(label="오늘 한 줄 일기")

    # 기록된 감정과 일기를 차례대로 보여주기 위한 Column 객체
    logs = ft.Column()

    # 감정 버튼을 눌렀을 때 실행되는 함수
    def save(e):

        # e.control.text는 눌린 버튼에 적혀 있는 이모지(감정)
        # 감정과 입력한 일기를 합쳐서 하나의 문장으로 만든다
        logs.controls.append(
            ft.Text(f"{e.control.text} : {diary.value}")
        )

        # 일기를 저장했으므로 입력창을 다시 비운다
        diary.value = ""

        # 새로 추가된 기록이 화면에 보이도록 화면을 다시 그린다
        page.update()

    # 화면에 제목, 입력창, 감정 버튼들, 기록 목록을 추가한다
    page.add(

        # 앱의 제목을 보여주는 텍스트
        ft.Text("😊 감정 기록 앱", size=25),

        # 한 줄 일기를 입력하는 입력창
        diary,

        # 감정 버튼들을 가로로 배치하기 위한 Row
        ft.Row([
            ft.ElevatedButton("😀", on_click=save),
            ft.ElevatedButton("😐", on_click=save),
            ft.ElevatedButton("😢", on_click=save),
        ]),

        # 저장된 감정 기록들이 표시될 영역
        logs
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
