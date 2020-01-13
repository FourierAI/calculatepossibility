import main
import traceback
import pymysql

if __name__ == "__main__":

    # # ngram_1
    # try:
    #     db = pymysql.connect(host='127.0.0.1',
    #                         port=3306,
    #                         user='root',
    #                         password='root',
    #                         db='n_grams',
    #                         charset='utf8')
    #     cursor = db.cursor()

    #     ngram_stop = 622009+5
    #     count = 0
    #     with open(
    #             '/home/fourier/Data/processed_file/data/GoogleWbi-Direct_Filtered'
    #     ) as file:
    #         for line in file:
    #             count = count + 1
    #             if count > (622009+5):
    #                 break

    #             if count >=6 and count <= (622009+5):
                    
    # ngram_2
    try:
        db = pymysql.connect(host='127.0.0.1',
                            port=3306,
                            user='root',
                            password='root',
                            db='n_grams',
                            charset='utf8')
        cursor = db.cursor()
        count =0
        with open('/home/fourier/Data/processed_file/data/GoogleWbi-Direct_Filtered') as file:
            for line in file:
                count = count +1
                if count >=622017 and count <= 213054597:
                    content = line.split('\t')
                    possibility = content[0]
                    words = content[1]
                    content = words.split(' ')
                    under_word = content[0]
                    after_word = content[1]
                    punishment = '-99'
                    
                    sql = 'insert into ngram_2 ( ngram2_under_word, ngram2_after_word, ngram2_possibility,punishment ) VALUES ("%s","%s","%s","%s");'%(under_word, after_word, possibility, punishment)
                    cursor.execute(sql)
    except Exception as ex:
        db.rollback()
        traceback.print_exc()
    finally:
        db.commit()
        cursor.close()
        db.close()