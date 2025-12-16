# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작되면 가장 먼저 실행되는 함수
# page는 화면 전체를 관리하는 객체이다
def main(page: ft.Page):

    # 설문 결과를 화면에 보여줄 텍스트 객체
    # 처음에는 아무 내용도 없도록 빈 문자열로 만든다
    result = ft.Text("")

    # 버튼을 클릭했을 때 실행되는 함수
    # e는 어떤 버튼이 눌렸는지에 대한 정보를 담고 있다
    def vote(e):

        # e.control.text는 눌린 버튼에 적혀 있는 글자
        # 예: "👍 좋음" 또는 "👎 나쁨"
        result.value = f"{e.control.text} 선택!"

        # 화면을 다시 그려서 변경된 결과가 보이게 한다
        page.update()

    # 화면에 버튼과 텍스트를 추가한다
    page.add(

        # "👍 좋음" 버튼을 만들고 클릭하면 vote 함수가 실행된다
        ft.ElevatedButton("👍 좋음", on_click=vote),

        # "👎 나쁨" 버튼을 만들고 클릭하면 vote 함수가 실행된다
        ft.ElevatedButton("👎 나쁨", on_click=vote),

        # 선택 결과를 보여줄 텍스트를 화면에 추가한다
        result
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
