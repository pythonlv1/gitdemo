# coding=ut-8
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("hello git")


class Sings:
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self,name):
        if self.__init_flag:
            self.name = name
            Sings.__init_flag = False

app = lask(__name__)
@app.route("/student/")
def index():
    return "hello"
app.run()

con = pymysql.connect("localhost","root","root","dbname")
cur = con.curser()
sql = "insertinto student(sname,sno,sex) values(%s%s%s) "