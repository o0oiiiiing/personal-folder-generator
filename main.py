import tkinter as tk # GUI 애플리케이션을 만들기 위한 모듈
from tkinter import font # 폰트 설정을 위한 모듈
from tkinter import filedialog # 파일 대화상자를 위한 모듈
from tkcalendar import DateEntry # 날짜 선택을 위한 모듈

class BackupFolderApp:
    # ───────────────────── 초기 설정 및 실행 ─────────────────────
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("백업 폴더 생성")

        self.app_font = font.Font(family="Malgun Gothic", size=10)

        self.setup_window()
        self.create_widgets()

        self.root.mainloop()
    
    # ───────────────────── 윈도우 크기 및 위치 설정 ─────────────────────
    def setup_window(self):
        # 윈도우 창 크기 설정
        window_width = 500
        window_height = 400

        # 화면 크기 구하기
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 윈도우 창의 위치를 계산 (가운데로)
        position_top = int((screen_height - window_height) / 2)
        position_left = int((screen_width - window_width) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    # ───────────────────── 위젯 생성 ─────────────────────
    def create_widgets(self):
        # 프레임
        select_frame = tk.Frame(self.root)
        select_frame.pack(pady=(15, 0))

        # 폴더 선택
        folder_label = tk.Label(select_frame, text="생성할 위치 : ", font=self.app_font)
        folder_label.grid(row=0, column=0, sticky=tk.E, padx=5)

        self.folder_entry = tk.Entry(select_frame, font=self.app_font, width=30)
        self.folder_entry.config(relief="sunken")
        self.folder_entry.insert(0, "폴더를 선택하세요")
        self.folder_entry.grid(row=0, column=1, padx=5, sticky=tk.EW)

        folder_btn = self.create_btn("폴더 찾기", self.select_folder, master=select_frame)
        folder_btn.grid(row=0, column=2, padx=5)

        # 날짜 선택
        date_label = tk.Label(select_frame, text="날짜 : ", font=self.app_font)
        date_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.calendar = DateEntry(select_frame, font=self.app_font, foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.calendar.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # 생성할 폴더 영역
        target_folder_label = tk.Label(select_frame, text="생성할 폴더 : ", font=self.app_font)
        target_folder_label.grid(row=2, column=0, sticky=tk.NE, padx=5, pady=5)
        
        target_folder_frame = tk.Frame(select_frame)
        target_folder_frame.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        target_folder_frame.rowconfigure(0, weight=1)
        target_folder_frame.columnconfigure(0, weight=1)
        
        self.scrollbar = tk.Scrollbar(target_folder_frame, width=20)
        
        self.listbox = tk.Listbox(target_folder_frame, yscrollcommand=self.scrollbar.set, font=self.app_font, height=6)
        self.listbox.grid(row=0, column=0, sticky=tk.EW)
        
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.scrollbar.config(command=self.listbox.yview)
        
        listbox_btn_frame = tk.Frame(target_folder_frame)
        listbox_btn_frame.grid(row=1, column=0, sticky=tk.EW)
        listbox_btn_frame.columnconfigure(0, weight=1)
        listbox_btn_frame.columnconfigure(1, weight=1)
        
        add_btn = self.create_btn("추가", self.add_to_listbox, master=listbox_btn_frame)
        add_btn.grid(row=0, column=0, sticky=tk.EW)
        
        remove_btn = self.create_btn("삭제", lambda: print("remove"), master=listbox_btn_frame)
        remove_btn.grid(row=0, column=1, sticky=tk.EW)
        
        # 확인, 닫기 버튼
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=(30, 0))

        confirm_btn = self.create_btn("확인", lambda: print("confirm"), master=btn_frame)
        confirm_btn.pack(side=tk.LEFT, padx=20)

        close_btn = self.create_btn("닫기", self.root.quit, master=btn_frame)
        close_btn.pack(side=tk.LEFT, padx=20)
    
    # ───────────────────── 버튼 생성 ─────────────────────
    def create_btn(self, text, command, master=None):
        if master is None:
            master = self.root
        return tk.Button(
            master,
            text=text,
            command=command,
            font=self.app_font,
            width=13,
            overrelief="sunken",
            cursor="hand2",
            activebackground="#d9d9d9"
        )
    
    # ───────────────────── 폴더 선택 ─────────────────────
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("선택한 폴더 경로:", folder_path)
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
            
    # ───────────────────── 리스트박스에 항목 추가 ─────────────────────
    def add_to_listbox(self):
        value = tk.simpledialog.askstring("추가", "추가할 폴더 이름을 입력하세요.")
        if value:
            self.listbox.insert(tk.END, value)


# 앱 실행
if __name__ == "__main__":
    app = BackupFolderApp()