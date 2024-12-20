export GCP_REGION='us-central1'
export GCP_PROJECT='work-mylab-machinelearning'
export AR_REPO='iamgemini-priyambodocom-artifactregistry'  
export SERVICE_NAME='iamgemini-priyambodo-com' 

#authenticate your laptop to google cloud
gcloud init	#Authorizes access and performs other common setup steps.
gcloud auth login #Authorizes access only.
gcloud auth application-default login

gcloud auth application-default set-quota-project $GCP_PROJECT
gcloud config set billing/quota_project $GCP_PROJECT
