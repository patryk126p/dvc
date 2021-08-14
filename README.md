# DVC

1. [Installation](https://dvc.org/doc/install)
2. Initialization
```
dvc init
git commit -m "initialize dvc"
```
3. Set remote
- create S3 bucket
- create IAM user with programmatic access and `AmazonS3FullAccess` permission
- (install and) [configure aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- ``dvc remote add -d s3remote s3://mybucket/path``
- commit changes
```
git add .dvc/config
git commit -m "configure dvc"
```
4. Track data
```
dvc add data/iris.data
git add data/iris.data.dvc data/.gitignore
git commit -m "add data"
dvc push
```
5. Get data from remote
```
dvc pull
```
6. [More info](https://dvc.org/doc/start/data-and-model-versioning)
