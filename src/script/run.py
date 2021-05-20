# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/4/15 16:41
# @Software    : PyCharm
# @Description : tomcat 启动script


import os
import sys
import time
import glob
import telnetlib

host = "127.0.0.1"
port = "8080"
tomcat_path = "/opt/apache-tomcat-8.5.55/"


# 清空tomcat所有日志
def clearlog():
    os.system("cat " + "/dev/null " + "> " + tomcat_path + "logs/catalina.out")
    map(os.remove, glob.glob(tomcat_path + "logs/*.log"))
    map(os.remove, glob.glob(tomcat_path + "logs/*.txt"))


# 关闭tomcat服务器----------------------------------------------------------
def shutdown():
    clearlog()
    print "tomcat正在关闭，请稍等..."
    os.system(tomcat_path + "bin/shutdown.sh")
    os.system("kill -9 $(ps -ef | grep java| awk '{print $2}')")
    time.sleep(5)
    try:
        tel = telnetlib.Telnet(host, port)
        print "关闭tomcat失败,请手动关闭"
        sys.exit()
    except:
        print "关闭tomcat成功"


# 启动tomcat服务器----------------------------------------------------------
def startup():
    clearlog()
    print"tomcat正在启动..."
    os.system(tomcat_path + "bin/startup.sh")
    time.sleep(3)
    for k in range(38, 0, -1):
        print k
        time.sleep(1)
        os.system("clear")
        # 判断是否启动成功
    rizhi = open(tomcat_path + "logs/catalina.out", 'r')
    try:
        telnet = telnetlib.Telnet(host, port)
        xinxi = rizhi.read()
        xinxi.index("Server startup in")
        print "让你久等了，5秒后揭晓答案"
        time.sleep(6)
        print "启动tomcat成功，这次算你运气好！"
        rizhi.close()
    except:
        print "启动tomcat失败，其实早在我预料之内！"
        rizhi.close()


# 重启tomcat服务器----------------------------------------------------------
def restart():
    os.system("service mysql restart")
    print("哈哈,数据库重启成功，6秒后重启tomcat!")
    time.sleep(6)
    # 关闭tomcat
    shutdown()
    # 启动tomcat
    startup()


# 查看或搜索tomcat日志-----------------------------------------------------
def viewlog():
    if sousuo == "":
        os.system("cat " + tomcat_path + "logs/catalina.out")
    else:
        os.system("grep -n " + sousuo + " " + tomcat_path + "logs/catalina.out")


# -----------------------------------------------------------
def main():
    print("|--------------------------------------------------------------------------|\n\
                    欢迎使用rmao!\n\
            rmao start    #启动tomcat服务器\n\
            rmao stop     #关闭tomcat服务器\n\
            rmao restart  #重启tomcat服务器\n\
            rmao log      #查看tomcat日志\n\
            rmao clear    #清空tomcat日志\n\
            \n\
|--------------------------------------------------------------------------|\n ")
    os.system("netstat -tnlp")
    print("-----------------------------------------------------------------------")
    os.system("df -h")
    print("-----------------------------------------------------------------------")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
        sys.exit()
    else:
        pass

    tihuan = sys.argv[1]
    sousuo = ""
    if len(sys.argv) == 3:
        sousuo = sys.argv[2]
    if tihuan == "restart":
        restart()
    elif tihuan == "start":
        startup()
    elif tihuan == "stop":
        shutdown()
    elif tihuan == "log":
        viewlog()
    elif tihuan == "clean":
        clearlog()
    else:
        main()
        sys.exit()
