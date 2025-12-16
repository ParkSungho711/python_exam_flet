# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft

# 랜덤 기능(숫자, 가위바위보)을 위해 random 모듈을 불러온다
import random


# 앱이 실행되면 가장 먼저 호출되는 메인 함수
def main(page: ft.Page):

    # 현재 화면에 있는 모든 UI 요소를 지우는 함수
    def clear():
        # page에 추가된 컨트롤들을 모두 제거한다
        page.controls.clear()

    # 메인 메뉴 화면을 구성하는 함수
    def menu():
        # 기존 화면을 초기화
        clear()

        # 메뉴 화면에 표시할 UI 추가
        page.add(
            # 앱 제목 텍스트
            ft.Text("🎮 미니 게임 센터", size=25),

            # 숫자 맞추기 게임으로 이동하는 버튼
            ft.ElevatedButton(
                "숫자 맞추기",
                on_click=lambda e: guess()  # 클릭 시 guess 함수 실행
            ),

            # 가위바위보 게임으로 이동하는 버튼
            ft.ElevatedButton(
                "가위바위보",
                on_click=lambda e: rps()  # 클릭 시 rps 함수 실행
            )
        )

        # 화면 갱신
        page.update()

    # 숫자 맞추기 게임 화면 함수
    def guess():
        # 기존 화면을 초기화
        clear()

        # 1부터 10 사이의 정답 숫자를 랜덤으로 생성
        answer = random.randint(1, 10)

        # 숫자를 입력받을 텍스트 필드
        tf = ft.TextField(label="1~10")

        # 결과 메시지를 출력할 텍스트
        msg = ft.Text()

        # 확인 버튼을 눌렀을 때 실행되는 함수
        def check(e):
            # 입력한 숫자가 정답이면 "정답!", 아니면 "틀림!" 표시
            msg.value = "정답!" if int(tf.value) == answer else "틀림!"
            # 화면 갱신
            page.update()

        # 숫자 맞추기 화면에 UI 요소 추가
        page.add(
            # 게임 제목
            ft.Text("숫자 맞추기"),

            # 숫자 입력 필드
            tf,

            # 확인 버튼
            ft.ElevatedButton("확인", on_click=check),

            # 결과 메시지
            msg,

            # 메뉴로 돌아가는 버튼
            ft.ElevatedButton("⬅ 메뉴", on_click=lambda e: menu())
        )

        # 화면 갱신
        page.update()

    # 가위바위보 게임 화면 함수
    def rps():
        # 기존 화면을 초기화
        clear()

        # 결과를 출력할 텍스트
        msg = ft.Text()

        # 가위/바위/보 버튼을 눌렀을 때 실행되는 함수
        def play(e):
            # 컴퓨터가 가위, 바위, 보 중 하나를 랜덤 선택
            c = random.choice(["가위", "바위", "보"])

            # 컴퓨터의 선택 결과를 화면에 표시
            msg.value = f"컴퓨터: {c}"

            # 화면 갱신
            page.update()

        # 가위바위보 화면에 UI 요소 추가
        page.add(
            # 게임 제목
            ft.Text("가위바위보"),

            # 가위 버튼
            ft.ElevatedButton("가위", on_click=play),

            # 바위 버튼
            ft.ElevatedButton("바위", on_click=play),

            # 보 버튼
            ft.ElevatedButton("보", on_click=play),

            # 결과 메시지
            msg,

            # 메뉴로 돌아가는 버튼
            ft.ElevatedButton("⬅ 메뉴", on_click=lambda e: menu())
        )

        # 화면 갱신
        page.update()

    # 앱 시작 시 메인 메뉴 화면을 먼저 보여준다
    menu()


# main 함수를 실행하여 Flet 앱을 시작한다
ft.app(main)
