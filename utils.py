import sqlite3


def get_all_words():
    connect = sqlite3.connect("Data/shows.db")
    data = connect.execute("Select * from shows").fetchall()
    connect.close()
    return data


def get_words_by_id(word_id):
    connect = sqlite3.connect("Data/wordsdb.db")
    query = '''
            Select * from words where id = ?
            '''
    data = connect.execute(query, (word_id,)).fetchone()
    connect.close()
    return data


def get_meaning_of_word(word):
    connect = sqlite3.connect("Data/wordsdb.db")
    query = '''
            Select meaning from words where word = ?
            '''
    data = connect.execute(query, (word,)).fetchone()
    connect.close()
    return data


def get_list_suggestions_of_search(text):
    connect = sqlite3.connect("Data/wordsdb.db")
    query = '''
            Select meaning from words where word %STARTSWITH 'u'
            '''
    text_convert = "'" + text + "'"
    print(text_convert)
    print(query)
    data = connect.execute(query).fetchone()
    connect.close()
    return data



if __name__ == "__main__":
    print(get_all_words())
