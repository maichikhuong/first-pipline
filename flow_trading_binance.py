import pandas as pd
import numpy as np

from time import *
from trading_bot.trading_binance import *
from connect_duckdb import *
from prefect import flow, get_run_logger, task, serve
from time import *
from prefect.deployments import Deployment


@task(name = 'crawling_binance')
def get_data():
    a = binance()
    return a


@task(name = 'insert_data')
def insert_data(a):
    create_insert_table(a)
    

@flow(name = 'crawling_binance_flow', retries=5, retry_delay_seconds=5, log_prints=True)
def flow_crawling_binance():
    a = get_data()
    print(a)
    insert_data(a)



if __name__ == "__main__":

        flow_crawling_binance_deploy = flow_crawling_binance.to_deployment("flow_crawling_binance"
                , version = 'my-first-deployment-flow_trading_binance'
                , description = 'support-trading-binance'
                )

        serve(flow_crawling_binance_deploy)
