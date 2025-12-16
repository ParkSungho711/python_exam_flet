# Flet 라이브러리를 불러오고 ft라는 이름으로 사용한다
import flet as ft


# 앱이 시작될 때 가장 먼저 실행되는 함수
def main(page: ft.Page):

    # 화면에 이미지를 추가한다
    page.add(

        # Image 객체는 사진이나 그림을 화면에 보여주는 역할을 한다
        ft.Image(

            # 인터넷에 있는 이미지 주소(URL)
            # picsum.photos는 실행할 때마다 다른 이미지를 보여준다
            src="https://picsum.photos/200",

            # 이미지의 가로 크기를 200으로 설정한다
            width=200
        )
    )


# main 함수를 실행해서 Flet 앱을 시작한다
ft.app(main)
