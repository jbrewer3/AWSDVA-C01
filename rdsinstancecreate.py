import boto3


client = boto3.client('rds')

response = client.create_db_instance(
    DBName='mytestrds',
    DBInstanceIdentifier='mysldb',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='jbrewer',
    MasterUserPassword='Jbrewer3',
    )
    
