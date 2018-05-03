import psycopg2

db = psycopg2.connect("dbname=news user=vagrant")
c = db.cursor()

popular_sql = '''SELECT title, count(path) FROM articles
        JOIN log on log.path LIKE '%' || articles.slug || '%'
        WHERE log.status = '200 OK'
        GROUP BY articles.title
        ORDER BY count DESC LIMIT 4;'''


c.execute(popular_sql)
pop_result = c.fetchall()


views_1 = (pop_result[0])[1]
views_2 = (pop_result[1])[1]
views_3 = (pop_result[2])[1]
views_4 = (pop_result[3])[1]

first = '''"'''+(pop_result[0])[0]+'''"'''+' -- '+str(views_1)+' views'
second = '''"'''+(pop_result[1])[0]+'''"'''+' -- '+str(views_2)+' views'
third = '''"'''+(pop_result[2])[0]+'''"'''+' -- '+str(views_3)+' views'

popular_articles = [first, second, third]

print ('---------------------------------------------------------')
print (popular_articles[0])
print (popular_articles[1])
print (popular_articles[2])
print ('---------------------------------------------------------')

authors_sql = '''SELECT name, count(path)
                FROM authors
                JOIN articles
                    ON articles.author = authors.id
                JOIN log
                    ON log.path LIKE '%' || articles.slug || '%'
                WHERE log.status = '200 OK'
                AND log.status = '200 OK'
                GROUP BY authors.name
                ORDER BY count DESC;'''

c.execute(authors_sql)
aut_result = c.fetchall()

views_1 = (aut_result[0])[1]
views_2 = (aut_result[1])[1]
views_3 = (aut_result[2])[1]
views_4 = (aut_result[3])[1]

first = (aut_result[0])[0] + ' -- ' + str(views_1) + ' views'
second = (aut_result[1])[0] + ' -- ' + str(views_2) + ' views'
third = (aut_result[2])[0] + ' -- ' + str(views_3) + ' views'
fourth = (aut_result[3])[0] + ' -- ' + str(views_4) + ' views'

popular_authors = [first, second, third, fourth]

print (popular_authors[0])
print (popular_authors[1])
print (popular_authors[2])
print (popular_authors[3])
print ('---------------------------------------------------------')


all_status_create ='''CREATE VIEW all_status as
                SELECT time::date as ad, ROUND(count(status),4) as acount FROM log
                GROUP BY log.time::date
                ORDER BY acount DESC;'''

c.execute(all_status_create)

bad_status_create ='''CREATE VIEW bad_status as
                    SELECT time::date as bd, ROUND(count(status),4) as bcount FROM log
                    WHERE log.status != '200 OK'
                    GROUP BY log.time::date
                    ORDER BY bcount DESC;'''

c.execute(bad_status_create)

combo_status_create = '''CREATE VIEW combo_view as
                        SELECT bcount / acount as pct, ad
                        FROM all_status, bad_status
                        WHERE ad = bd;'''

c.execute(combo_status_create)

percent_call = '''SELECT ROUND(pct,4) from combo_view
                WHERE pct > 0.01;'''

c.execute(percent_call)
percent_status = c.fetchall()
percentage = round(((percent_status[0][0])*100),2)

error_date_call ='''SELECT TO_CHAR(ad, 'Mon DD'), TO_CHAR(ad, 'YYYY')
                    FROM combo_view
                    WHERE pct > 0.01;'''
c.execute(error_date_call)
error_date_status = c.fetchall()
error_mon_day = error_date_status[0][0]
error_yr = error_date_status[0][1]

error_result = error_mon_day+', '+error_yr+' -- '+str(percentage)+"% errors"

print (error_result)
print ('---------------------------------------------------------')



drop_views = '''DROP VIEW all_status, bad_status, combo_view;'''

c.execute(drop_views)

db.close()

#authors_1 = author +' -- '+str(views_1)+' views'
