from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

my_file=Dataset("/tmp/my_file.txr")

With DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2022,1,1),
    catchup=false,
)as dag:
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri,"a+") as f:
            f.write("Producer Update")
    update_dataset()