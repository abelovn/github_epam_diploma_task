
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

alias kubectl -> k

k -n development apply -f k8s/secrets.yml 
k -n development apply -f k8s/app-depl.yml
k -n development apply -f k8s/app-loadbalancer.yml
k -n development apply -f k8s/app-hpa.yml
::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::
Production environment

production
k -n production apply -f k8s/secrets-prod.yml 
k -n production apply -f k8s/app-depl-prod.yml
k -n production apply -f k8s/app-hpa-prod.yml
k -n production apply -f k8s/app-loadbalancer-prod.yml

::::::::::::::::::::::::::
::::::::::::::::::::::::::
k  apply -f .\k8s\sonar\sonar.yml
k  apply -f .\k8s\sonar\sonar.yml

k  -n cicd get svc

github_epam_diploma_task

k -n development get svc 

k -n all get statefulset

:::::::::::::::::::
kubernetes dashboard

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.1/aio/deploy/recommended.yaml
k apply -f .\k8s\dashboard\dashboard-adminuser.yaml
k apply -f .\k8s\dashboard\admin-role-binding.yml  
kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"
get token
k proxy
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login
::::::::::::::::::::::::::::


external-ip
[host]:9090

`SONARQUBE_HOST`
`SONARQUBE_TOKEN`

To use exclusions to analyze only the specified subset(s) of files in sonar.sources, go to Project Settings > General Settings > Analysis Scope > Files.

Source File Inclusions
Test File Inclusions  add **/__init__.py

### Prometheus and Grafana stack

1. Add repo: `$ helm repo add stable https://charts.helm.sh/stable
`
2. Update: `$ helm repo update`
3. Helm install: `$ helm install prometheus --namespace monitoring  stable/prometheus-operator`




N. Expose ports:
```sh
k -n monitoring apply -f .\k8s\monitoring\prometh-nodeport.yml

k -n monitoring apply -f .\k8s\monitoring\grafana-nodeport.yml
```

Add target
k -n monitoring apply -f  .\k8s\monitoring\servicemonitor-depl.yml
k -n development apply -f  .\k8s\monitoring\service-depl.yml

k -n monitoring apply -f  .\k8s\monitoring\servicemonitor-depl.yml
k -n development apply -f  .\k8s\monitoring\service-depl.yml

#
k  -n monitoring get svc







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




### Elastic stack

1. Install custom resource definitions and the operator with its RBAC rules: `$ kubectl apply -f https://download.elastic.co/downloads/eck/1.0.1/all-in-one.yaml`
2. Namespace for Elastic: `$ kubectl apply -f ./k8s/logging/namespace-kube-logging.yaml`
3. Create Statefulset Elasticsearch `$ kubectl apply -f ./k8s/logging/elasticsearch_statefulset.yaml`
4. Elastic cluster: `$ kubectl apply -f ./k8s/logging/elastic-cluster.yaml`
5. Kibana: `$ kubectl apply -f ./k8s/logging/kibana.yaml`

6.   Filebeat deployment set: `kubectl apply -f ./k8s/logging/filebeat-kubernetes.yaml`
        > **NOTE**: checkout password for "elastic" user:
        > `kubectl get secret -n kube-logging quickstart-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode`
        > replace password in the configuration file `filebeat-kubernetes.yaml` line 93

7. Expose ports for elastic and kibana:
```sh

```


kubectl create -f https://download.elastic.co/downloads/eck/2.2.0/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/2.2.0/operator.yaml

k -n development apply -f .\k8s\logging\1namespace-kube-logging.yaml
k -n development apply -f .\k8s\logging\2elasticksearch-svc.yaml
k -n development apply -f .\k8s\logging\3elasticsearch_statefulset.yaml
k -n development apply -f .\k8s\logging\4elastic-cluster.yaml
k -n development apply -f .\k8s\logging\5kibana.yaml
k -n development apply -f .\k8s\logging\6filebeat-kubernetes.yaml
k -n development apply -f .\k8s\logging\es-srv-nodeport.yml
k -n development apply -f .\k8s\logging\kb-srv-nodeport.yml


:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
Horizontal Pod Autoscaler On EKS Cluster

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl get deployment metrics-server -n kube-system


#start fix sonar cube
#$##№

Get token for k8s dashboard
kubectl -n kubernetes-dashboard get secret $(kubectl -n 
kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"
