# question_draw
# CREATE TABLE `question_draw` (
#   `draw_id` varchar(255) DEFAULT NULL,
#   `id` int NOT NULL AUTO_INCREMENT,
#   `question_id` int DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

table1='question'
table2='draw'
# table1

# D:\proj\python\my_util_py_pub\csv_to_mysql_ddl.py
# D:\proj\python\my_util_py_pub\link_table_create_make.py
ddl_sql = f"""CREATE TABLE `{table1}_{table2}` (
   
  `id` int NOT NULL AUTO_INCREMENT,
   `{table1}_id` int  DEFAULT NULL,
  `{table2}_id` int DEFAULT NULL,
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """

    # D:\question_draw.sql

print(ddl_sql)