Here the consumer dag is scheduled not based on time but based on the data updates by producer.dag.

# Data Processing DAGs

This repository contains two Airflow DAGs for data processing tasks: "producer" and "consumer".

## Producer DAG

The "producer" DAG is responsible for updating a dataset daily by appending "Producer Update" to a file located at "/tmp/my_file.txt".

### Overview

This DAG is part of a data processing pipeline and is scheduled to run daily, starting from January 1, 2022. It consists of a single task named "update_dataset_task" that updates the dataset file.

### Task

#### update_dataset_task

This task executes the `update_dataset` function, which appends "Producer Update" to the dataset file "/tmp/my_file.txt". The task is implemented using Airflow's `@task` decorator.

## Consumer DAG

The "consumer" DAG is responsible for reading data from a dataset daily by printing the contents of a file located at "/tmp/my_file.txt".

### Overview

This DAG is part of a data processing pipeline and is scheduled to run daily, starting from January 1, 2022. It consists of a single task named "read_dataset_task" that reads the dataset file.

### Task

#### read_dataset_task

This task executes the `read_dataset` function, which reads the contents of the dataset file "/tmp/my_file.txt" and prints them. The task is implemented using Airflow's `@task` decorator.

## Dependencies

- Airflow


