
# DIPLOMA

Using API https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/ get all data about “The Beatles" \
and store it into your DB: \
 kind \
 , collectionName \
 , trackName \
 , collectionPrice \
 , trackPrice \
 , primaryGenreName \
, trackCount \
, trackNumber \
, releaseDate \
 Output the data by collectionName (the collectionName is set)
in form of a table and sort them by releaseDate in ascending order.

Environment variables and config

export `AWS_ACCESS_KEY_ID`=your_access_key \
export `AWS_SECRET_ACCESS_KEY`=your_secret_key \
export `AWS_DEFAULT_REGION`=your_region \


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

export AWS_ACCESS_KEY_ID=your_access_key \
export AWS_SECRET_ACCESS_KEY=your_secret_key \
export AWS_DEFAULT_REGION=your_region


## Create Infrastructure

To create Infrastructure run

```
  terraform apply 
```

aws eks update-kubeconfig --region us-east-2 --name abelovn-eks


cat .kube/config | base64

`KUBE_CONFIG_DATA`


k -n development apply -f k8s/secrets.yml 
k -n development apply -f k8s/app-depl.yml
k -n development apply -f k8s/app-loadbalancer.yml
k -n development apply -f k8s/app-hpa.yml
k  apply -f .\k8s\sonar\sonar.yml

k  -n cicd get svc
external-ip
[host]:9090

`SONARQUBE_HOST`
`SONARQUBE_TOKEN`
