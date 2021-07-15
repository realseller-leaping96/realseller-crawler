import module.db_module as db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)

db_class = db_module.Database() #db연결 생성
#price_list 테이블 없을경우 정의해주기
try:    
    with db_class.cursor as cursor:
        sql =( """
            CREATE TABLE if not exists `price_list` (
            `price_id` INT(11) NOT NULL AUTO_INCREMENT,
            `model_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `model_code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `price` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `storage` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            PRIMARY KEY (`price_id`) USING BTREE
            )
        """ )
        cursor.execute(sql)
        db_class.db_conn.commit()
        cursor.execute("DELETE FROM price_list;")
        db_class.db_conn.commit()
        
finally:
     db_class.db_conn.close()