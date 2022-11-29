from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='sirene-geocodage',
    schedule_interval='48 7 1 * *',
    start_date=days_ago(10),
    tags=['etalab', 'insee', 'sirene', 'monthly', 'geocodage'],
    params={},
) as dag:

    t1 = SSHOperator(
        ssh_conn_id='SSH_FILES_DATA_GOUV_FR',
        task_id='test_bahs',
        command="ls",
        dag=dag)
        
    t1
