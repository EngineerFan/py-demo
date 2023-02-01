import pymysql


class dbApi:

    @staticmethod
    def connect(dataSource: str):
        return pymysql.connect(host='10.130.253.67', user='root', password='0JZ^YQHxjII!p1Qf', database=dataSource)

    @staticmethod
    def close(db):
        db.close()
