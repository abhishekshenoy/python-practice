from google.cloud import bigquery


def get_bq_datasets():
    client = bigquery.Client()
    dataset_list = client.list_datasets(project="wmt-hnw-infra-poc")
    print(dataset_list.__sizeof__())
    print("abhishek")
