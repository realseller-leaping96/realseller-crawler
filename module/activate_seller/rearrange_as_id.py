import module.db_module as db_module

def rearrange_as_id():
    db_class = db_module.Database() #db연결 생성
    #테이블내에서 중복된 리뷰 삭제후 pk값 새로 부여하기
    db_class.engine_conn.close()
    sql2_1= """
    ALTER TABLE activate_seller AUTO_INCREMENT = 1;
    """
    db_class.db_conn.cursor().execute(sql2_1)
    db_class.db_conn.commit()

    sql2_2="""
    SET @COUNT = 0;
    """
    db_class.db_conn.cursor().execute(sql2_2)
    db_class.db_conn.commit()

    sql2_3="""
    UPDATE activate_seller SET as_id = @COUNT:=@COUNT+1;
    """
    db_class.db_conn.cursor().execute(sql2_3)
    db_class.db_conn.commit()
    db_class.db_conn.close()