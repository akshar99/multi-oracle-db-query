import oracledb
import pandas as pd

# List of servers to connect to in the format DBINSTANCENAME_HOSTNAME.COM
servers = [
    '"DB1_host1.example.com"',
    '"DB2_host2.example.com"',
    '"DB3_host3.example.com"'
]

# Convert the server list to a dictionary {DBINSTANCENAME: HOSTNAME.COM}
server_dict = {}
for server in servers:
    parts = server.replace('"', '').split('_')
    if len(parts) == 2:
        db_instance, hostname = parts
        server_dict[db_instance] = hostname

# Sample user credentials
uid = "sample_user"
pwd = "sample_password_123"

# List to store query results
results = []

# Generic health check query (this can be replaced with any valid SQL query)
health_check_query = """
SELECT 'DB Name' AS EID, 'Status' AS STATUS, sysdate AS Last_Active, 'Created' AS Created, 
       'Profile' AS Profile, name AS DB, host_name AS Host_name
FROM v$database
JOIN v$instance;
"""

# Iterate over each server connection string and run the query
for db_instance, hostname in server_dict.items():
    dsn = f"{hostname}/{db_instance}"
    try:
        with oracledb.connect(user=uid, password=pwd, dsn=dsn) as connection:
            with connection.cursor() as cursor:
                for row in cursor.execute(health_check_query):
                    results.append(row)
    except oracledb.OperationalError as oe:
        oe_object, = oe.args
        print(dsn)
        print("Message: ", oe_object.message)
        print("Error Full Code: ", oe_object.full_code)
    except oracledb.InterfaceError as ie:
        ie_object, = ie.args
        print(dsn)
        print("Message: ", ie_object.message)
        print("Error Full Code: ", ie_object.full_code)
    except oracledb.IntegrityError as ige:
        ige_object, = ige.args
        print(dsn)
        print("Message: ", ige_object.message)
        print("Error Full Code: ", ige_object.full_code)
    except oracledb.DatabaseError as de:
        de_object, = de.args
        print(dsn)
        print("Message: ", de_object.message)
        print("Error Full Code: ", de_object.full_code)

# Create a DataFrame from the results and save to a CSV file
df = pd.DataFrame(results, columns=['EID', 'STATUS', 'Last_Active', 'Created', 'Profile', 'DB', 'Host_name'])
df.to_csv("Health_Check_Report.csv", index=False)

print(df.head())
