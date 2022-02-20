import sqlite3


def get_all_title_show():
    connect = sqlite3.connect("Data/shows.db")
    datas = connect.execute("select title from shows").fetchall()
    result = []
    for d in datas:
        result.append(d[0])
    connect.close()
    return result

def get_information_show():
    connect = sqlite3.connect("Data/shows.db")
    datas = connect.execute("select title from shows").fetchall()
    result = []
    for d in datas:
        result.append(d[0])
    connect.close()
    return result

if __name__ == "__main__":
    print(get_all_title_show())