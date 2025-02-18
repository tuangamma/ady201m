import pandas as pd
from sqlalchemy import create_engine

# Thông tin kết nối SQL Server
server = 'TUNADODAIHOC/SQLEXPRESS'
database = 'ADY'  # Thay bằng tên database của bạn
driver = 'ODBC Driver 17 for SQL Server'
# driver = 'SQL Server Native Client 11.0'

# Đường dẫn file CSV

# Tạo chuỗi kết nối với Windows Authentication

# connection_string = (
#     f"mssql+pyodbc://@{server}/{database}?"
#     f"driver={driver.replace(" ", "+")};trusted_connection=yes"
# )

# engine = create_engine(connection_string)
# print(engine)
# print("đã kết nối được")
# data_csv = ["AI_Scores.csv", "AI_Students.csv", "SB_Scores.csv", "SB_Students.csv", "SE_Scores.csv", "SE_Students.csv"]

# # Đọc dữ liệu từ file CSV
# for x in data_csv:
#     df = pd.read_csv('Data_import_SQL/'+x)
#     # Ghi dữ liệu lên SQL Server
#     df.to_sql(x[:-4], con=engine, if_exists='replace', index=False)
#     print("Upload thành công!")

# Tạo connection string đúng chuẩn
connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}&trusted_connection=yes"
)

# Tạo engine kết nối
engine = create_engine(connection_string)

# Danh sách file CSV
data_csv = ["AI_Scores.csv", "AI_Students.csv", "SB_Scores.csv", "SB_Students.csv", "SE_Scores.csv", "SE_Students.csv"]

# Đọc và nhập dữ liệu vào SQL Server
for x in data_csv:
    df = pd.read_csv(f'Data_import_SQL/{x}')
    df.to_sql(x[:-4], con=engine, if_exists='replace', index=False)
    print(f"Upload {x} thành công!")