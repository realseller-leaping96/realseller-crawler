import re
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CreateTable
from sqlalchemy import create_engine, Table, Column, Integer, MetaData
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


class CreateTableIfNotExists(CreateTable):
    pass


@compiles(CreateTableIfNotExists)
def compile_create_table_if_not_exists(element, ddlcompiler, **kw):
    default_create_ddl = ddlcompiler.visit_create_table(element, **kw)
    default_create_ddl = default_create_ddl.lstrip()
    create_if_not_exists = re.sub(
        r"^CREATE TABLE ", "CREATE TABLE IF NOT EXISTS ", default_create_ddl, flags=re.IGNORECASE
    )
    return create_if_not_exists


engine = create_engine('mysql+mysqldb://root:123123@localhost/gidseller')
metadata = MetaData()
table = Table(
    "some_table",
    metadata,
    Column("id", Integer, primary_key=True),
)
engine.execute(CreateTableIfNotExists(table))