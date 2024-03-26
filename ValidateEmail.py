import re


def validateEmail(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        print("成功")
        return True
    else:
        print("失败")
        return True


validateEmail('123 @xo.com')
