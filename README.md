
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
k -n development get svc 


external-ip
[host]:9090

`SONARQUBE_HOST`
`SONARQUBE_TOKEN`

https://helm.sh/docs/intro/install/

helm repo add stable https://charts.helm.sh/stable

helm search repo stable/prometheus-operator -o yaml

helm install prometheus --namespace monitoring  stable/prometheus-operator


NAME: prometheus
LAST DEPLOYED: Sun May 15 18:07:23 2022
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES:
*******************
*** DEPRECATED ****
*******************
* stable/prometheus-operator chart is deprecated.
* Further development has moved to https://github.com/prometheus-community/helm-charts
* The chart has been renamed kube-prometheus-stack to more clearly reflect
* that it installs the `kube-prometheus` project stack, within which Prometheus       
* Operator is only one component.

The Prometheus Operator has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=prometheus"

Visit https://github.com/coreos/prometheus-operator for instructions on how
to create & configure Alertmanager and Prometheus instances using the Operator.



kubectl port-forward service/prometheus-prometheus-oper-prometheus 9090:9090

#

