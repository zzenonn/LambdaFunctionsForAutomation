import json
import boto3
import os

region = os.environ['AWS_REGION']

def lambda_handler(event, context):
    
    client = boto3.client('ssm')
    
    response = client.start_automation_execution(
        DocumentName='AWS-StopEC2Instance',
        DocumentVersion='$DEFAULT',
        TargetParameterName='InstanceId',
        Targets=[
            {
                'Key': 'ResourceGroup',
                'Values': [
                    'DemoInstances',
                ]
            },
        ],
        MaxConcurrency='100%',
        MaxErrors='2',
        TargetLocations=[
        {
            'Accounts': [
                '883779074323',
            ],
            'Regions': [
                region,
            ],
            'TargetLocationMaxConcurrency': '100%',
            'TargetLocationMaxErrors': '2',
            'ExecutionRoleName': 'SSMAutomationRole'
        }
        ]
    )

    
    return {
        'statusCode': 200,
        'body': json.dumps('It Worked!')
    }

