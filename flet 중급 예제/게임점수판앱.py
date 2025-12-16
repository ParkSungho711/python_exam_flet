# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 실행되면 가장 먼저 호출되는 메인 함수
def main(page: ft.Page):

    # 점수를 저장할 변수 (처음 값은 0)
    score = 0

    # 현재 점수를 화면에 보여줄 텍스트 위젯
    # size는 글자 크기이다
    txt = ft.Text("점수: 0", size=20)

    # + 버튼을 눌렀을 때 실행되는 함수
    def plus(e):
        # 바깥(main 함수)의 score 변수를 수정하겠다는 선언
        nonlocal score

        # 점수를 1 증가
        score += 1

        # 텍스트 내용을 현재 점수로 변경
        txt.value = f"점수: {score}"

        # 변경된 내용을 화면에 반영
        page.update()

    # - 버튼을 눌렀을 때 실행되는 함수
    def minus(e):
        # 바깥(main 함수)의 score 변수를 수정하겠다는 선언
        nonlocal score

        # 점수를 1 감소
        score -= 1

        # 텍스트 내용을 현재 점수로 변경
        txt.value = f"점수: {score}"

        # 변경된 내용을 화면에 반영
        page.update()

    # 리셋 버튼을 눌렀을 때 실행되는 함수
    def reset(e):
        # 바깥(main 함수)의 score 변수를 수정하겠다는 선언
        nonlocal score

        # 점수를 0으로 초기화
        score = 0

        # 텍스트도 초기 상태로 변경
        txt.value = "점수: 0"

        # 변경된 내용을 화면에 반영
        page.update()

    # 화면에 보여줄 요소들을 추가
    page.add(

        # 앱의 제목 텍스트
        ft.Text("🏆 점수판", size=25),

        # 현재 점수를 보여주는 텍스트
        txt,

        # 버튼들을 가로로 배치하기 위한 Row
        ft.Row([

            # 점수 증가 버튼
            ft.ElevatedButton("+", on_click=plus),

            # 점수 감소 버튼
            ft.ElevatedButton("-", on_click=minus),

            # 점수 초기화 버튼
            ft.ElevatedButton("리셋", on_click=reset)
        ])
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
