from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, DoubleType
from pyspark.sql.functions import *
from google.oauth2 import service_account
import pandas as pd
import json


def extract_data():
    loan_data = spark.read \
        .option("header", True) \
        .option("quote", '"') \
        .option("escape", '"') \
        .option("multiLine", True) \
        .csv("loan.csv")

    columns_selected = ['id',
                    'member_id',
                    'loan_amnt',
                    'funded_amnt',
                    'issue_d',
                    'recoveries',
                    'total_rec_prncp',
                    'total_rec_int',
                    'purpose',
                    'total_pymnt',
                    'mths_since_last_record',
                    'dti',
                    'mths_since_last_delinq',
                    'annual_inc',
                    'total_acc',
                    'acc_now_delinq',
                    'pub_rec',
                    'open_acc',
                    'inq_last_6mths',
                    'delinq_2yrs',
                    'installment',
                    'earliest_cr_line',
                    'int_rate',
                    'emp_length',
                    'term',
                    'total_rev_hi_lim',
                    'initial_list_status',
                    'verification_status',
                    'addr_state',
                    'home_ownership',
                    'grade',
                    'sub_grade',
                    'loan_status'
                    ]
    
    loan_data = loan_data.select(*columns_selected)

    return [(loan_data, 'loan_data')]


def load_data(data_list):

    numeric_columns = [
        'loan_amnt', 'funded_amnt', 'recoveries', 'total_rec_prncp',
        'total_rec_int', 'total_pymnt', 'dti', 'annual_inc',
        'installment', 'int_rate', 'total_rev_hi_lim',
        'mths_since_last_record', 'mths_since_last_delinq',
        'total_acc', 'acc_now_delinq', 'pub_rec', 'open_acc',
        'inq_last_6mths', 'delinq_2yrs'
    ]
    
    db_id = 'credit_analytics'
    service_account_info = json.load(open('credit_analytics_service_acc.json'))
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info)

    for tb_data, tb_name in data_list:
        if isinstance(tb_data, pd.DataFrame):
            tb_data_df = tb_data
        else:
            tb_data_df = tb_data.toPandas()

        for col_name in numeric_columns:
            if col_name in tb_data_df.columns:
                tb_data_df[col_name] = pd.to_numeric(tb_data_df[col_name], errors='coerce')

        tb_data_df.to_gbq(credentials=credentials,
                          destination_table=db_id + "." + tb_name,
                          if_exists='replace')


if __name__ == "__main__":

    # Create a Spark session
    spark = SparkSession.builder \
    .appName("Credit_Initial_Load") \
    .config("spark.executor.memory", "6g") \
    .config("spark.driver.memory", "6g") \
    .getOrCreate()

    load_data(extract_data())