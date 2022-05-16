
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

Connect VPN

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

github_epam_diploma_task

k -n development get svc 

k -n all get statefulset


external-ip
[host]:9090

`SONARQUBE_HOST`
`SONARQUBE_TOKEN`

To use exclusions to analyze only the specified subset(s) of files in sonar.sources, go to Project Settings > General Settings > Analysis Scope > Files.

Source File Inclusions
Test File Inclusions  add **/__init__.py

https://helm.sh/docs/intro/install/

helm repo add stable https://charts.helm.sh/stable

Using Helm chart to deploy opeator

helm search repo stable/prometheus-operator -o yaml




:::::::::::::::::
:::::::::::::::::
helm repo add stable https://charts.helm.sh/stable
helm repo update



stable/prometheus-operator  no longer valid. Use helm repo add prometheus-community https://prometheus-community.github.io/helm-charts instead 


helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update
helm -n monitoring install [RELEASE_NAME] prometheus-community/kube-prometheus-stack
helm -n monitoring install prometheus prometheus-community/kube-prometheus-stack
::::::::::::::::::::::::
::::::::::::::::::::::::



Prerequisites
Kubernetes 1.16+
Helm 3+

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update


Install Chart
# Helm
$ helm install release-0.7 prometheus-community/kube-prometheus-stack






helm install prometheus --namespace monitoring  stable/prometheus-operator
helm install --generate-name --namespace monitoring  stable/prometheus-operator
helm install prometheus   stable/prometheus-operator
k -n monitoring apply -f .\k8s\monitoring\prometh-nodeport.yml

:::::::::::::::::

helm install prometheus --namespace development  stable/prometheus-operator
k -n development apply -f .\k8s\monitoring\prometh-nodeport.yml
k  -n development get svc

:::::::::::::::

helm uninstall prometheus --namespace monitoring  stable/prometheus-operator 



The Prometheus Operator has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=prometheus"

Visit https://github.com/coreos/prometheus-operator for instructions on how
to create & configure Alertmanager and Prometheus instances using the Operator.



k get configmap


 k -n monitoring apply -f .\k8s\monitoring\prometh-nodeport.yml

#
k  -n monitoring get svc



k  apply -f .\k8s\monitoring\rbac.yaml
https://medium.com/kubernetes-tutorials/monitoring-your-kubernetes-deployments-with-prometheus-5665eda54045
https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/




Grapana (default log and pass)

 k  -n development describe pod prometheus-grafana-69b659948c-wk5kl  

  Environment:
      GF_SECURITY_ADMIN_USER:      <set to the key 'admin-user' in secret 'prometheus-grafana'>      Optional: false
      GF_SECURITY_ADMIN_PASSWORD:  <set to the key 'admin-password' in secret 'prometheus-grafana'>  Optional: false

kubectl -n development get secret prometheus-grafana -o yaml 
apiVersion: v1
data:
  admin-password: cHJvbS1vcGVyYXRvcg==
  admin-user: YWRtaW4=

echo 'cHJvbS1vcGVyYXRvcg==' | base64 --decode
admin
prom-operator
#