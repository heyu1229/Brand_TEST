import pymysql


#数据连接信息
database_host = '172.18.10.21'  # 因为您将通过SSH隧道连接，所以这里是本地主机
database_port = 3306
database_username = 'developer'
database_password = 'developer'
database_name = 'brands_elfbar'



# 尝试连接到 SSH 服务器
try:

    db_connection = pymysql.connect(host=database_host, port=database_port, user=database_username,
                                    password=database_password, database=database_name)
    print("Connected to database.")
    print("db_connection:", db_connection)
except  pymysql.MySQLError as e:
    print("failed to connect to MySQL:", e)


