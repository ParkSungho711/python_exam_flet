# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤 선택을 위해 random 모듈을 불러온다
import random


# 앱이 실행되면 가장 먼저 호출되는 메인 함수
def main(page: ft.Page):

    # 결과를 화면에 보여줄 텍스트 객체
    result = ft.Text()

    # 점심 메뉴 후보 목록
    lunch = ["라면", "김밥", "피자", "햄버거"]

    # 할 일 후보 목록
    todo = ["운동하기", "책 읽기", "코딩하기"]

    # "점심 추천" 버튼을 눌렀을 때 실행되는 함수
    def pick_lunch(e):
        # 점심 목록 중 하나를 랜덤으로 선택해 결과 텍스트에 표시
        result.value = "점심: " + random.choice(lunch)
        # 화면을 새로 고쳐 변경 사항을 반영
        page.update()

    # "할 일 추천" 버튼을 눌렀을 때 실행되는 함수
    def pick_todo(e):
        # 할 일 목록 중 하나를 랜덤으로 선택해 결과 텍스트에 표시
        result.value = "할 일: " + random.choice(todo)
        # 화면을 새로 고쳐 변경 사항을 반영
        page.update()

    # 화면에 표시할 UI 요소들을 추가
    page.add(
        # 앱 제목 텍스트
        ft.Text("🎲 랜덤 추천 앱", size=25),

        # 점심 메뉴를 랜덤으로 추천하는 버튼
        ft.ElevatedButton("점심 추천", on_click=pick_lunch),

        # 할 일을 랜덤으로 추천하는 버튼
        ft.ElevatedButton("할 일 추천", on_click=pick_todo),

        # 결과를 보여주는 텍스트
        result
    )


# main 함수를 실행하여 Flet 앱을 시작한다
ft.app(main)
