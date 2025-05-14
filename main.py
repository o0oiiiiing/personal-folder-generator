import tkinter as tk # GUI 애플리케이션을 만들기 위한 모듈
from tkinter import font # 폰트 설정을 위한 모듈
from tkinter import filedialog # 파일 대화상자를 위한 모듈

root = tk.Tk() # root 윈도우 생성
root.title("백업 폴더 생성") # 윈도우 제목 설정

app_font = font.Font(family="Malgun Gothic", size=10) # 폰트 설정

# ========== 함수 정의 ==========
# 폴더 선택 대화상자를 열고 선택한 폴더 경로를 출력하는 함수
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("선택한 폴더 경로:", folder_path)
        folder_path_entry.delete(0, tk.END)  # 기존 텍스트 삭제
        folder_path_entry.insert(0, folder_path)  # 새 경로 삽입

# 버튼을 생성하는 함수
def create_btn(text, command):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=app_font,
        width=13,
        overrelief="sunken",
        cursor="hand2",
        activebackground="#d9d9d9"
    )


# ----- 윈도우 창 크기 및 위치 설정 -----
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


# ----- GUI 구성 -----
folder_path_frame = tk.Frame(root)
folder_path_frame.pack(pady=30)

label = tk.Label(text="생성할 위치 : ", font=app_font)
label.pack(in_=folder_path_frame, side=tk.LEFT, padx=5)

# 경로 출력용 Entry
folder_path_entry = tk.Entry(root, text="경로가 여기에 표시됩니다", font=app_font, width=35)
folder_path_entry.config(relief="sunken") # 라벨의 테두리 스타일 설정
folder_path_entry.pack(in_=folder_path_frame, side=tk.LEFT, padx=5)

# 폴더 선택 버튼
folder_choose_btn = create_btn(text="폴더 찾기", command=select_folder)
folder_choose_btn.pack(in_=folder_path_frame, side=tk.LEFT, padx=5)

# 버튼들을 담을 프레임 생성
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # root에 프레임을 가운데 배치

# 확인 버튼
confirm_btn = create_btn(text="확인", command=lambda: print("confirm"))
confirm_btn.pack(in_=button_frame, side=tk.LEFT, padx=20)

# 닫기 버튼
close_btn = create_btn(text="닫기", command=root.quit)
close_btn.pack(in_=button_frame, side=tk.LEFT, padx=20)


root.mainloop() # tkinter 이벤트 루프 시작