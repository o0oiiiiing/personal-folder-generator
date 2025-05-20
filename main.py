import os # 파일 및 폴더 경로 조작을 위한 모듈
import json # JSON 파일 읽기 및 쓰기를 위한 모듈
import tkinter as tk # GUI 애플리케이션을 만들기 위한 모듈
from tkinter import font # 폰트 설정을 위한 모듈
from tkinter import filedialog # 파일 대화상자를 위한 모듈
from tkcalendar import DateEntry # 날짜 선택을 위한 모듈

class BackupFolderApp:
    # ───────────────────── 초기 설정 및 실행 ─────────────────────
    def __init__(self):
        """
        GUI 애플리케이션을 초기화하고 실행합니다.

        주요 작업:
            - Tkinter 루트 윈도우 생성 및 제목 설정
            - 기본 폰트 지정
            - 윈도우 레이아웃 및 위젯 생성
            - 저장된 폴더 이름 로드
            - GUI 메인 루프 실행
        """
        self.root = tk.Tk()
        self.root.title("백업 폴더 생성")

        self.app_font = font.Font(family="Malgun Gothic", size=10)

        self.setup_window()
        self.create_widgets()
        self.load_saved_folder_names()

        self.root.mainloop()
    
    
    # ───────────────────── 윈도우 크기 및 위치 설정 ─────────────────────
    def setup_window(self):
        """
        애플리케이션 창의 크기와 위치를 설정합니다.

        창 크기:
            - 너비: 500px
            - 높이: 400px

        화면 해상도 기준으로 창을 화면 중앙에 배치합니다.
        """
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
        """
        GUI의 주요 위젯들을 생성하고 배치합니다.
        
        위젯 구성:
            - 생성할 위치를 선택하는 입력창과 버튼
            - 날짜 선택 캘린더 위젯
            - 하위 폴더명을 추가/삭제할 수 있는 리스트박스와 관련 버튼
            - 생성 및 닫기 기능 버튼
        """
        # 전체 영역 프레임
        select_frame = tk.Frame(self.root)
        select_frame.pack(pady=(15, 0))

        # ─────────────── [1] 생성 위치 선택 영역 ───────────────
        # 사용자로부터 파일 생성 경로를 입력받는 UI 구성
        folder_label = tk.Label(select_frame, text="생성할 위치 : ", font=self.app_font)
        folder_label.grid(row=0, column=0, sticky=tk.E, padx=5)

        self.folder_entry = tk.Entry(select_frame, font=self.app_font, width=30)
        self.folder_entry.config(relief="sunken")
        self.folder_entry.insert(0, "폴더를 선택하세요")
        self.folder_entry.grid(row=0, column=1, padx=5, sticky=tk.EW)

        folder_btn = self.create_btn("폴더 찾기", self.select_folder, master=select_frame)
        folder_btn.grid(row=0, column=2, padx=5)

        # ─────────────── [2] 날짜 선택 영역 ───────────────
        # 상위 폴더 이름으로 사용할 날짜 입력 위젯
        date_label = tk.Label(select_frame, text="날짜 : ", font=self.app_font)
        date_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.calendar = DateEntry(select_frame, font=self.app_font, foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.calendar.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # ─────────────── [3] 하위 폴더명 입력 및 리스트 관리 ───────────────
        # 리스트박스를 사용해 하위 폴더명을 추가/삭제할 수 있는 UI 구성
        subfolder_label = tk.Label(select_frame, text="생성할 폴더 : ", font=self.app_font)
        subfolder_label.grid(row=2, column=0, sticky=tk.NE, padx=5, pady=5)
        
        subfolder_frame = tk.Frame(select_frame)
        subfolder_frame.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        subfolder_frame.rowconfigure(0, weight=1)
        subfolder_frame.columnconfigure(0, weight=1)
        
        self.scrollbar = tk.Scrollbar(subfolder_frame, width=20)
        
        self.listbox = tk.Listbox(subfolder_frame, yscrollcommand=self.scrollbar.set, font=self.app_font, height=6, selectmode="extended")
        self.listbox.grid(row=0, column=0, sticky=tk.EW)
        
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.scrollbar.config(command=self.listbox.yview)
        
        listbox_btn_frame = tk.Frame(subfolder_frame)
        listbox_btn_frame.grid(row=1, columnspan=2, sticky=tk.EW)
        listbox_btn_frame.columnconfigure(0, weight=1)
        listbox_btn_frame.columnconfigure(1, weight=1)
        
        add_btn = self.create_btn("추가", self.add_to_listbox, master=listbox_btn_frame)
        add_btn.grid(row=0, column=0, sticky=tk.EW)
        
        remove_btn = self.create_btn("삭제", self.remove_selected_items, master=listbox_btn_frame)
        remove_btn.grid(row=0, column=1, sticky=tk.EW)
        
        # ─────────────── [4] 실행 및 종료 버튼 ───────────────
        # 폴더 생성 실행 및 종료 버튼
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=(30, 0))

        create_btn = self.create_btn("생성", self.create_backup_folders, master=btn_frame)
        create_btn.pack(side=tk.LEFT, padx=20)

        close_btn = self.create_btn("닫기", self.root.quit, master=btn_frame)
        close_btn.pack(side=tk.LEFT, padx=20)
        
        
    # ────────────── 저장된 폴더 이름 불러오기 ──────────────
    def load_saved_folder_names(self):
        """
        이전에 저장된 폴더 이름들을 JSON 파일에서 불러와 리스트박스에 표시합니다.

        동작:
            - 'folder_log.json' 파일이 존재할 경우 열어서 폴더 이름 목록을 불러옵니다.
            - 'folder_names' 키를 기준으로 리스트를 가져와 리스트박스에 항목으로 추가합니다.
            - JSON 형식 오류가 있을 경우 예외를 무시하고 종료합니다.
        """ 
        log_file = "folder_log.json"
        if os.path.exists(log_file):
            try:
                with open(log_file, "r") as f:
                    data = json.load(f)
                    folder_names = data.get("folder_names", [])
                    for name in folder_names:
                        self.listbox.insert(tk.END, name)
            except json.JSONDecodeError:
                pass
    
    
    # ───────────────────── 버튼 생성 ─────────────────────
    def create_btn(self, text, command, master=None):
        """
        텍스트와 명령을 지정하여 Tkinter 버튼을 생성합니다.

        Args:
            text (str): 버튼에 표시될 텍스트.
            command (function): 버튼 클릭 시 실행할 함수.
            master (tk.Widget, optional): 버튼이 속할 부모 위젯. 기본값은 self.root.

        Returns:
            tk.Button: 생성된 Tkinter 버튼 위젯
        """ 
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
        """
        폴더 선택 대화상자를 열어 사용자가 선택한 경로를 입력창에 표시합니다.

        동작:
            - 폴더 선택 창을 띄워 사용자가 폴더를 선택하도록 합니다.
            - 선택된 경로가 있을 경우, 폴더 경로 입력창을 갱신합니다.
        """
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
            
            
    # ───────────────────── 리스트박스에 항목 추가 ─────────────────────
    def add_to_listbox(self):
        """
        사용자에게 폴더 이름을 입력받아 리스트박스에 추가하고 로그 파일을 갱신합니다.

        동작:
            - 입력 대화상자를 띄워 추가할 폴더 이름을 입력받습니다.
            - 입력된 값이 있으면 리스트박스에 추가합니다.
            - 폴더명 추가 후, 변경 사항을 로그 파일에 저장하기 위해 갱신 함수를 호출합니다.
        """
        value = tk.simpledialog.askstring("추가", "추가할 폴더 이름을 입력하세요.")
        
        if value:
            self.listbox.insert(tk.END, value)
            
        self.update_log_file() # 추가 후 로그 파일 갱신 함수 호출
     
            
    # ───────────────────── 리스트박스의 항목 삭제 ─────────────────────
    def remove_selected_items(self):
        """
        리스트박스에서 선택된 항목들을 삭제하고 로그 파일을 갱신합니다.

        동작:
            - 리스트박스에서 선택된 항목의 인덱스를 가져옵니다.
            - 선택된 항목이 없으면 알림 메시지를 표시하고 함수를 종료합니다.
            - 선택된 항목들을 뒤에서부터 삭제하여 인덱스 밀림 현상을 방지합니다.
            - 삭제 후 변경 사항을 로그 파일에 저장하기 위해 갱신 함수를 호출합니다.
        """
        selected_indices = self.listbox.curselection()  # 선택된 항목들의 인덱스 얻기
        
        if not selected_indices:
            tk.messagebox.showinfo("알림", "삭제할 항목을 선택하세요.")
            return
        
        for index in reversed(selected_indices): # 뒤에서부터 삭제 (인덱스 밀림 방지)
            self.listbox.delete(index)
            
        self.update_log_file() # 삭제 후 로그 파일 갱신 함수 호출
    
    
    # ───────────────────── 로그 파일 갱신 ─────────────────────
    def update_log_file(self):
        """
        리스트박스에 있는 폴더 이름 목록을 JSON 파일에 저장합니다.

        동작:
            - 리스트박스에 있는 모든 폴더 이름을 읽어 리스트로 만듭니다.
            - 'folder_log.json' 파일에 폴더 이름 리스트를 JSON 형식으로 기록합니다.
        """
        folder_names = [self.listbox.get(i) for i in range(self.listbox.size())]
        log_file = "folder_log.json"
        
        with open(log_file, "w") as f:
            json.dump({"folder_names": folder_names}, f, indent=4)
    
    
    # ───────────────────── 백업 폴더 생성 ─────────────────────        
    def create_backup_folders(self):
        """
        사용자가 지정한 위치에 선택한 날짜를 상위 폴더로 하여 하위 폴더들을 생성합니다.

        동작:
            - 입력된 기본 경로(base_path)가 유효한 폴더인지 검사합니다.
            - 유효하지 않으면 오류 메시지를 출력하고 함수를 종료합니다.
            - 선택한 날짜를 이름으로 하는 상위 폴더를 생성합니다.
            - 리스트박스에 있는 폴더 이름들을 하위 폴더로 생성합니다.
            - 폴더 생성 완료 후 사용자에게 완료 메시지를 표시합니다.
            - 모든 작업 완료 후 애플리케이션을 종료합니다.
        """
        base_path = self.folder_entry.get() # 생성할 위치
        date_str = self.calendar.get_date().strftime("%Y-%m-%d") # 선택한 날짜

        # 폴더 경로가 유효한지 확인
        if not os.path.isdir(base_path):
            tk.messagebox.showerror("오류", "유효한 폴더 경로를 선택하세요.")
            return
        
        # 상위 폴더 생성
        date_folder_path = os.path.join(base_path, date_str)
        os.makedirs(date_folder_path, exist_ok=True)

        for i in range(self.listbox.size()):
            folder_name = self.listbox.get(i)
            full_path = os.path.join(date_folder_path, folder_name)
            os.makedirs(full_path, exist_ok=True)
        
        tk.messagebox.showinfo("완료", "폴더 생성이 완료되었습니다.")
        
        self.root.quit()


# 앱 실행
if __name__ == "__main__":
    app = BackupFolderApp()