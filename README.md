### Votingapp

This is a simple API service built for various tests purposes. It puts and stores "votes" in a DynamoDB table. You can vote by just CURLing (or similar) to 4 APIs: 
```
/api/outback
/api/bucadibeppo
/api/ihop
/api/chipotle
```
In addition to vote, you can query the status by CURLing (or similar) the `/api/getvotes` API. Note that there is an experimental feature in the code to artificially consume more memory/CPU. This is available by hitting the `/api/getheavyvotes` API. The amount of artificial load is determined by two variables (`MEMSTRESSFACTOR` and `CPUSTRESSFACTOR` which default to `1`). You can tweak the amount of load by, for example, setting them to `0.1` if you want less overhead or `10` if you want more overhead. 

### How to set up the application

This is a classic Python application. To use it with AWS App Runner you can build the image upfront (a `Dockerfile` is provided) or you can provide the source code directly. The only requirements creating the DDB table and set the proper permissions. In the [preparation](/preparation) folder there are instructions and code to make this happen. 

#### Variables

- `DDB_AWS_REGION` this variable is required and needs to be set to the region of the DDB table.
- `DDB_TABLE_NAME` this variable is optional and contains the DDB table name (default: `votingapp-restaurants`)
- `MEMSTRESSFACTOR` and `CPUSTRESSFACTOR` are optional and governs the behaviour of the artificial load (experimental)




