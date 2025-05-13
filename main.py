import tkinter as tk # GUI 애플리케이션을 만들기 위한 모듈
from tkinter import font # 폰트 설정을 위한 모듈
from tkinter import filedialog # 파일 대화상자를 위한 모듈

root = tk.Tk() # root 윈도우 생성
root.title("백업 폴더 생성") # 윈도우 제목 설정

font = font.Font(family="Malgun Gothic", size=10) # 폰트 설정


# ===== 윈도우 창 크기 및 위치 설정 =====
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


# ===== 버튼 생성 =====
def create_button(text, command):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=font,
        width=13,
        overrelief="sunken",
        cursor="hand2",
        activebackground="#d9d9d9"
    )

confirmButton = create_button(text="확인", command=lambda: print("확인")) # 확인 버튼
confirmButton.grid(row=0, column=0, padx=10, pady=10)

closeButton = create_button(text="닫기", command=root.quit) # 닫기 버튼
closeButton.grid(row=0, column=1, padx=10, pady=10)


root.mainloop() # tkinter 이벤트 루프 시작