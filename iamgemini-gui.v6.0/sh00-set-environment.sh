export GCP_REGION='us-central1'
export GCP_PROJECT='work-mylab-machinelearning'
export AR_REPO='iamgemini-priyambodocom-artifactregistry'  
export SERVICE_NAME='iamgemini-priyambodo-com' 

echo $GCP_REGION
echo $GCP_PROJECT
echo $AR_REPO
echo $SERVICE_NAME

#authenticate your laptop to google cloud
gcloud components update
gcloud init	#Authorizes access and performs other common setup steps.
gcloud auth login #Authorizes access only.
gcloud auth application-default login
gcloud config set project work-mylab-machinelearning

gcloud auth application-default set-quota-project $GCP_PROJECT
gcloud config set billing/quota_project $GCP_PROJECT

gcloud config list
gcloud auth list