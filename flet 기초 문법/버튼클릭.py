# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 현재 숫자 값을 저장할 변수
    # 처음 시작 값은 0이다
    count = 0

    # 현재 값을 화면에 보여줄 텍스트 객체
    # size는 글자 크기를 의미한다
    txt = ft.Text(f"현재 값: {count}", size=20)

    # "증가" 버튼을 눌렀을 때 실행되는 함수
    def plus(e):

        # 바깥에 있는 count 변수를 사용하겠다고 알려주는 키워드
        nonlocal count

        # count 값을 1 증가시킨다
        count += 1

        # 텍스트에 새로운 count 값을 반영한다
        txt.value = f"현재 값: {count}"

        # 화면을 다시 그려서 변경된 값이 보이게 한다
        page.update()

    # 화면에 텍스트와 버튼을 추가한다
    page.add(

        # 현재 값을 보여주는 텍스트
        txt,

        # "➕ 증가" 버튼을 만들고 클릭하면 plus 함수가 실행되게 한다
        ft.ElevatedButton("➕ 증가", on_click=plus)
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
