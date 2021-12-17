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

query_parameter__pk_question = [
    {
        'type': 'input',
        'name': 'pk',
        'message': 'enter pk: ',
    }
]

query_parameter__sk_question = [
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

query_parameter__msisdn_question = [
    {
        'type': 'input',
        'name': 'sk',
        'message': 'enter sk:',
    },
    {
        'type': 'input',
        'name': 'msisdn',
        'message': 'enter msisdn:',
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

next_step_question = [
    {
        'type': 'list',
        'name': 'next_step',
        'message': 'what do you want to do with the output rows:',
        'choices': [
            'create output',
            'send to queue'
        ]
    }
]

output_question = [
    {
        'type': 'list',
        'name': 'output_format',
        'message': 'please choose output format:',
        'choices': [
            'json',
            'csv'
        ]
    },
    {
        'type': 'input',
        'name': 'output_path',
        'message': 'please enter output path:',
    }
]

queue_question = [
    {
        'type': 'input',
        'name': 'queue_name',
        'message': 'please enter queue name:',
    }
]
