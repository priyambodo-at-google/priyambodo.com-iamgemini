#/bin/bash
docker build -t iamgemini-gui-v6 .
docker run -v apikey.json:/apikey.json -e GOOGLE_APPLICATION_CREDENTIALS=apikey.json -p 8080:8080 iamgemini-gui-v6

#push Docker to Google Artifact Registry (optional)
docker tag iamgemini-gui-v6 gcr.io/work-mylab-machinelearning/iamgemini-gui-v6
docker push gcr.io/work-mylab-machinelearning/iamgemini-gui-v6