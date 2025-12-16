# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 첫 번째 숫자를 입력받기 위한 입력창
    # label은 입력창 위에 표시되는 안내 문구이다
    a = ft.TextField(label="숫자 1")

    # 두 번째 숫자를 입력받기 위한 입력창
    b = ft.TextField(label="숫자 2")

    # 계산 결과를 화면에 보여주기 위한 텍스트
    # 처음에는 "결과:" 라는 글자만 표시한다
    result = ft.Text("결과:")

    # "더하기" 버튼을 눌렀을 때 실행되는 함수
    def calc(e):

        # 입력창 a와 b에 들어있는 값을 정수(int)로 바꿔서 더한다
        # 계산한 결과를 텍스트에 다시 넣어준다
        result.value = f"결과: {int(a.value) + int(b.value)}"

        # 변경된 내용을 화면에 반영한다
        page.update()

    # 화면에 입력창, 버튼, 결과 텍스트를 차례대로 추가한다
    page.add(
        a,
        b,
        ft.ElevatedButton("더하기", on_click=calc),
        result
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
