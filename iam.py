#import boto3 library
import boto3
import csv

##creating a function to return all policies and put that into a csv file
def createIAMpolicies():
    #creating a client for the IAM
    client = boto3.client('iam')
    # listing all the policies within the client 
    resp = client.list_policies(Scope='All')
    # going into the Policies (dict)
    policies = resp['Policies']

    # for items in policies:
    #     print(items['PolicyName'])
    #     print(items['PolicyId'])
    #     print(items['Arn'])
    # writing new iam.csv file with write permission
    with open('iam.csv', 'w', newline='') as f:
        # w as a writer in the file
        w = csv.writer(f)
        # write first row to set the coloumns
        w.writerow(['Policy Name', 'PolicyID', 'Arn'])
        # going though each item in the policies
        for items in policies:
            # writing each row with policy name, policy id, and ARN
            w.writerow([items['PolicyName'], items['PolicyId'], items['Arn']])

    print('CSV successfully created')


createIAMpolicies()