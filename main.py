import tkinter as tk # GUI 애플리케이션을 만들기 위한 모듈

root = tk.Tk() # root 윈도우 생성
root.title("백업 폴더 생성") # 윈도우 제목 설정

# 윈도우 창 크기 설정
window_width = 500
window_height = 400

# 화면의 크기 구하기
screen_width = root.winfo_screenwidth()  # 화면의 가로 크기
screen_height = root.winfo_screenheight()  # 화면의 세로 크기

# 윈도우 창의 위치를 계산 (가운데로)
position_top = int((screen_height - window_height) / 2)  # 세로 방향
position_left = int((screen_width - window_width) / 2)  # 가로 방향

# 윈도우 창을 가운데로 위치시킴
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

root.mainloop() # Tkinter 이벤트 루프 시작