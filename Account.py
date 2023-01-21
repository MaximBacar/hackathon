from datetime import datetime

class Account:

    SUBSCRIPTION_KEYS = ('service_name', 'gross_price', 'start_date', 'end_date', 'pay_periods')
    TRANSACTION_KEYS = ()

    def __init__(self, transactions : list[dict]):
        self._firstName = None
        self._lastName = None
        self._email = None
        self._password_HASH = None

        self._transactions : list[dict]= []
        self._subscriptions : list[dict] = []


    def _add_tx(self):
        pass

    def _add_subscription(self, service_name : str, gross_price : float, start_date : datetime, end_date : datetime, pay_periods : int):
        '''
        `service_name` Name of the subscription (Ex. Netflix, Apple Music, Rent)
        `gross_price` Gross price (without tax) of the subscription for a period
        `start_date` Date when the subscription started
        `end_date` Date when the subscription will end
        `pay_periods` Periods for each time the service is paid
        '''
        subscription = {
            'service_name'  : service_name,
            'gross_price'   : gross_price,
            'start_date'    : start_date,
            'end_date'      : end_date,
            'pay_periods'   : pay_periods
        }

        self._subscriptions.append(subscription)




    



    
