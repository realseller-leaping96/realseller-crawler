import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine
 
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
df_input = pd.read_sql_table('test_dup',conn)
conn.close()

######################중복행 탐지
print(df_input)  # 출력 DataFrame
print("\nDuplicated Data :\n")

duplicateDFRow = df_input[df_input.duplicated('text',keep='last')]
print(duplicateDFRow)

connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
if len(duplicateDFRow) > 0:
      del_list = duplicateDFRow['pk']
      ########################################중복행삭제
      
      with connection.cursor() as cursor:
            for d in del_list:
                  sql = "delete from test_dup where pk=%s"
                  cursor.execute(sql, d)
                  connection.commit()
            
            sql2_1= """
            ALTER TABLE test_dup AUTO_INCREMENT = 1;
            """
            cursor.execute(sql2_1)
            connection.commit()

            sql2_2="""
            SET @COUNT = 0;
            """
            cursor.execute(sql2_2)
            connection.commit()

            sql2_3="""
            UPDATE test_dup SET pk = @COUNT:=@COUNT+1;
            """
            cursor.execute(sql2_3)
            connection.commit()
      connection.close()