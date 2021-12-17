from __future__ import print_function, unicode_literals

from PyInquirer import prompt
from examples import custom_style_2

from credentials.credential_reader import ConfigReader
from query.query import Query
from query.query_by_pk import QueryByPk
from query.query_by_sk_timestamp import QueryBySkTimestamp

config_reader = ConfigReader("~/.aws/credentials")

profile_question = [
    {
        'type': 'list',
        'name': 'profile',
        'message': 'Please choose a profile',
        'choices': config_reader.get_profiles()
    }
]

selected_profile = prompt(profile_question, style=custom_style_2)
print("selected {} profile".format(selected_profile['profile']))
credentials = config_reader.get_credentials(selected_profile['profile'])
query_question = [
    {
        'type': 'list',
        'name': 'query',
        'message': 'Please select query',
        'choices': [
            'message_pk',
            'customer_time',
            'customer_msisdn'
        ]
    }
]

selected_query = prompt(query_question, style=custom_style_2)
print("selected {} query".format(selected_query['query']))

query: Query
response: list

if selected_query['query'] == 'message_pk':
    query_parameter_question = [
        {
            'type': 'input',
            'name': 'pk',
            'message': 'enter pk: ',
        }
    ]
    answer = prompt(query_parameter_question, style=custom_style_2)
    query = QueryByPk(credentials, answer['pk'])
    response = query.query()
    print(response)


if selected_query['query'] == 'customer_time':
    query_parameter_question = [
        {
            'type': 'input',
            'name': 'sk',
            'message': 'enter sk:',
        },
        {
            'type': 'input',
            'name': 'equation',
            'message': 'enter timestamp filter(from: >, >=, <, <=, =, btw):',
        },
        {
            'type': 'input',
            'name': 'timestamp',
            'message': 'enter timestamp(for btw, separate two low and high timestamp by ;):',
        }
    ]
    answer = prompt(query_parameter_question, style=custom_style_2)
    query = QueryBySkTimestamp(credentials, answer['sk'], answer['timestamp'].split(';'), answer['equation'])
    response = query.query()
    print(response)
