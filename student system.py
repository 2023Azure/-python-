import sys
import tkinter as tk

sys.stdout.reconfigure(encoding='utf-8')
student_list = []
users = 'Admin'
passwords = '123456'

class Student:
    def __init__(self, name, chinese, math, english, score):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.score = score
    
    def display(self):
        return f"{self.name}\t{self.chinese}\t{self.math}\t{self.english}\t{self.score}"

class Login_page:
    def __init__(self, root):
        self.root1 = root
        self.root1.title('学生管理系统1.0')
        self.root1.geometry('300x180')
        self.login_frame = tk.Frame(self.root1)
        self.login_frame.pack()  # 确保登录界面正确显示
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.login_frame, text='账号: ').grid(row=1, column=0)
        tk.Label(self.login_frame, text='密码: ').grid(row=2, column=0)
        tk.Entry(self.login_frame, textvariable=self.username).grid(row=1, column=1)
        tk.Entry(self.login_frame, textvariable=self.password, show='*').grid(row=2, column=1)
        tk.Button(self.login_frame, text='登录', command=self.login).grid(row=3, column=0)
        tk.Button(self.login_frame, text='退出', command=self.root1.quit).grid(row=3, column=1)

    def login(self):
        if self.username.get() == users and self.password.get() == passwords:
            self.login_frame.destroy()  # 登录成功后销毁登录界面
            Main_page(self.root1)
        else:
            tk.Label(self.login_frame, text='账号或密码错误!').grid(row=4, column=1)

class Main_page:
    def __init__(self, root):
        self.root2 = root
        self.root2.geometry('600x500')
        
        self.register_frame = tk.Frame(self.root2)
        self.search_frame = tk.Frame(self.root2)
        self.delete_frame = tk.Frame(self.root2)
        self.amend_frame = tk.Frame(self.root2)
        self.about_frame = tk.Frame(self.root2)

        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()

        self.menubar = tk.Menu(self.root2)
        self.root2.config(menu=self.menubar)
        self.create_menu()

        self.show_register_frame()  # 默认显示录入页面

    def create_menu(self):
        self.menubar.add_command(label='录入', command=self.show_register_frame)
        self.menubar.add_command(label='查询', command=self.show_search_frame)
        self.menubar.add_command(label='删除', command=self.show_delete_frame)
        self.menubar.add_command(label='修改', command=self.show_amend_frame)
        self.menubar.add_command(label='关于', command=self.show_about_frame)

    def register_page(self):
        tk.Label(self.register_frame, text='姓名: ').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.register_frame, text='语文: ').grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.register_frame, text='数学: ').grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.register_frame, text='英语: ').grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self.register_frame, textvariable=self.name).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(self.register_frame, textvariable=self.chinese).grid(row=2, column=1, padx=5, pady=5)
        tk.Entry(self.register_frame, textvariable=self.math).grid(row=3, column=1, padx=5, pady=5)
        tk.Entry(self.register_frame, textvariable=self.english).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.register_frame, text='录入', command=self.register).grid(row=5, column=0, padx=5, pady=5)

    def register(self):
        try:
            chinese_score = float(self.chinese.get())
            math_score = float(self.math.get())
            english_score = float(self.english.get())
            score = chinese_score + math_score + english_score
            student = Student(self.name.get(), chinese_score, math_score, english_score, score)
            student_list.append(student)
            tk.Label(self.register_frame, text="学生录入成功！").grid(row=6, column=0)
        except ValueError:
            tk.Label(self.register_frame, text="分数必须是数字！").grid(row=6, column=0)

    def search_page(self):
        for widget in self.search_frame.winfo_children():
            widget.destroy()  # 清除之前的查询结果

        for student in student_list:
            tk.Label(self.search_frame, text=student.display()).pack()

    def delete_page(self):
        def delete_student():
            name_to_delete = self.name.get()
            index = search(student_list, name_to_delete)
            if index == -1:
                tk.Label(self.delete_frame, text="该学生不存在!").grid(row=3, column=0)
            else:
                del student_list[index]
                tk.Label(self.delete_frame, text="学生已删除!").grid(row=3, column=0)

        tk.Label(self.delete_frame, text='请输入要删除的学生姓名:').grid(row=1, column=0)
        tk.Entry(self.delete_frame, textvariable=self.name).grid(row=1, column=1)
        tk.Button(self.delete_frame, text='删除', command=delete_student).grid(row=2, column=0)

    def amend_page(self):
        def amend_student():
            name_to_amend = self.name.get()
            index = search(student_list, name_to_amend)
            if index == -1:
                tk.Label(self.amend_frame, text="该学生不存在!").grid(row=5, column=0)
            else:
                try:
                    student = student_list[index]
                    student.chinese = float(self.chinese.get())
                    student.math = float(self.math.get())
                    student.english = float(self.english.get())
                    student.score = student.chinese + student.math + student.english
                    tk.Label(self.amend_frame, text="学生信息已修改！").grid(row=6, column=0)
                except ValueError:
                    tk.Label(self.amend_frame, text="分数必须是数字！").grid(row=6, column=0)

        tk.Label(self.amend_frame, text='姓名: ').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.amend_frame, text='语文: ').grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.amend_frame, text='数学: ').grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.amend_frame, text='英语: ').grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self.amend_frame, textvariable=self.name).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(self.amend_frame, textvariable=self.chinese).grid(row=2, column=1, padx=5, pady=5)
        tk.Entry(self.amend_frame, textvariable=self.math).grid(row=3, column=1, padx=5, pady=5)
        tk.Entry(self.amend_frame, textvariable=self.english).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.amend_frame, text='修改', command=amend_student).grid(row=5, column=0)

    def about_page(self):
        tk.Label(self.about_frame, text='Azure的个人练习').pack()

    def show_register_frame(self):
        self.hide_all_frames()
        self.register_frame.pack()
        self.register_page()

    def show_search_frame(self):
        self.hide_all_frames()
        self.search_frame.pack()
        self.search_page()

    def show_delete_frame(self):
        self.hide_all_frames()
        self.delete_frame.pack()
        self.delete_page()

    def show_amend_frame(self):
        self.hide_all_frames()
        self.amend_frame.pack()
        self.amend_page()

    def show_about_frame(self):
        self.hide_all_frames()
        self.about_frame.pack()
        self.about_page()

    def hide_all_frames(self):
        self.register_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.amend_frame.pack_forget()
        self.about_frame.pack_forget()

def search(student_list, name):
    for index, student in enumerate(student_list):
        if student.name == name:
            return index
    return -1



root = tk.Tk()
login_page = Login_page(root)
root.mainloop()

