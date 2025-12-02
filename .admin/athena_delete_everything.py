#%%
import time
import logging
import boto3

def run_query(database_name, query: str, s3_output: str = "s3://ceu-athena-admin-output/query-output") -> None:
    """Generic function to run athena query and ensures it is successfully completed

    Parameters
    ----------
    query : str
        formatted string containing athena sql query
    s3_output : str
        query output path
    """
    global athena_client
    start_response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": database_name},
        ResultConfiguration={
            "OutputLocation": s3_output,
        },
    )
    query_id = start_response["QueryExecutionId"]
    print(f"Query({database_name}): query_id={query}")

    while True:
        finish_state = athena_client.get_query_execution(QueryExecutionId=query_id)[
            "QueryExecution"
        ]["Status"]["State"]
        if finish_state == "RUNNING" or finish_state == "QUEUED":
            time.sleep(10)
        else:
            break

    assert finish_state == "SUCCEEDED", f"query state is {finish_state}"
    logging.info(f"Query {query_id} complete")
#%%

# Initialize a boto3 client for Athena
session = boto3.Session(profile_name='de2')
athena_client = session.client('athena')

# Function to delete all tables in a database
def delete_tables(database_name):
    # List all tables in the database
    tables = athena_client.list_table_metadata(CatalogName='AwsDataCatalog', DatabaseName=database_name)

    # Delete each table
    for table in tables['TableMetadataList']:
        table_name = table['Name']
        run_query(database_name, f"DROP TABLE {table_name}")
        print(f"Deleting table {table_name} in database {database_name}")
 
# List all databases
databases = athena_client.list_databases(CatalogName='AwsDataCatalog')

# Delete tables in each database, then delete the database
for db in databases['DatabaseList']:
    db_name = db['Name']
    #print(f"Deleting tables in database {db_name}")
    #delete_tables(db_name)

    print(f"Deleting database {db_name}")
    run_query('default', f"DROP DATABASE {db_name} CASCADE")

print("All Athena tables and databases have been deleted.")
# %%
