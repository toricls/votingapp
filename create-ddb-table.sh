#!/bin/bash

aws dynamodb create-table \
    --table-name restaurants \
    --attribute-definitions AttributeName=name,AttributeType=S \
    --key-schema AttributeName=name,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --region $AWS_REGION 

aws dynamodb put-item \
    --table-name restaurants \
    --item '{"name": {"S": "ihop"}, "restaurantcount": {"N": "0"}}' \
    --region $AWS_REGION 
    
aws dynamodb put-item \
    --table-name restaurants \
    --item '{"name": {"S": "outback"}, "restaurantcount": {"N": "0"}}' \
    --region $AWS_REGION 

aws dynamodb put-item \
    --table-name restaurants \
    --item '{"name": {"S": "bucadibeppo"}, "restaurantcount": {"N": "0"}}' \
    --region $AWS_REGION 

aws dynamodb put-item \
    --table-name restaurants \
    --item '{"name": {"S": "chipotle"}, "restaurantcount": {"N": "0"}}' \
    --region $AWS_REGION 