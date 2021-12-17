from __future__ import print_function, unicode_literals

from PyInquirer import prompt
from examples import custom_style_2
from pathlib import Path


from credentials.credential_reader import ConfigReader
from output import write_output
from query.query import Query
from query.query_by_pk import QueryByPk
from query.query_by_sk_msisdn import QueryByMsisdn
from query.query_by_sk_timestamp import QueryBySkTimestamp
from questions import query_question, query_parameter__pk_question, query_parameter__sk_question, \
    query_parameter__msisdn_question, next_step_question, output_question, queue_question
from queue import send_to_output

config_reader = ConfigReader("{}/.aws/credentials".format(str(Path.home())))

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

selected_query = prompt(query_question, style=custom_style_2)
print("selected {} query".format(selected_query['query']))

query: Query
response: list

if selected_query['query'] == 'message_pk':
    answer = prompt(query_parameter__pk_question, style=custom_style_2)
    query = QueryByPk(credentials, answer['pk'])
    response = query.query()
elif selected_query['query'] == 'customer_time':
    answer = prompt(query_parameter__sk_question, style=custom_style_2)
    query = QueryBySkTimestamp(credentials, answer['sk'], answer['timestamp'].split(';'), answer['equation'])
    response = query.query()
elif selected_query['query'] == 'customer_msisdn':
    answer = prompt(query_parameter__msisdn_question, style=custom_style_2)
    query = QueryByMsisdn(credentials, answer['sk'], answer['msisdn'], answer['timestamp'].split(';'), answer['equation'])
    response = query.query()
else:
    raise ValueError("wrong query!")

print("retrieved {} items".format(len(response)))
if len(response) == 0:
    print("done")
    exit()

next_step_answer = prompt(next_step_question, style=custom_style_2)
if next_step_answer['next_step'] == 'create output':
    output_answer = prompt(output_question, style=custom_style_2)
    write_output(output_answer, response)
    print("{} created.".format(output_answer['output_path']))
    exit()
elif next_step_answer['next_step'] == 'send to queue':
    queue_answer = prompt(queue_question, style=custom_style_2)
    send_to_output(credentials, queue_answer['queue_name'], response)
    exit()
else:
    exit()
