from tkinter import *
from tkinter import messagebox as mb


root = Tk()
root.geometry("800x500")
root.title("Quiz")

q = ['1.Which is the special symbol used in python to add comments?',
     '2.Syntax error in python is detected by _________at _______',
     '3.Which one of the following has the highest precedence in the expression?',
     '4.The format function, when applied on a string returns :',
     '5.Which statement is correct?',
     '6.Some test question?']

options = [['$', '//', '/*...*/', '#'],
           ['compiler/ compile time', 'interpreter/ run time', 'compiler/ run time', 'interpreter/ compile time'],
           ['Addition', 'Multiplication', 'Exponential', 'Parentheses'],
           ['list', 'bool', 'str', 'int'],
           ['List is mutable & Tuple is immutable', 'List is immutable & Tuple is mutable', 'Both are Mutable',
            'Both are Immutable'],
           ['a', 'b', 'c', 'd', 'e']
           ]

a = [4, 2, 4, 3, 1, 4]


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Academy Quiz", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))


quiz = Quiz()
root.mainloop()
