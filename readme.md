 # Docker
 docker build -f Dockerfile -t streamlit-app:latest .
 docker run -p 8501:8501 streamlit-app:latest   

# OAuth
For OAuth flow, run oAuthMain.py file


 # AWS

 Down load the AWS CLI
 https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

 ## build the image
 docker build -f Dockerfile -t streamlit-app:latest .
 ## tag the image
 docker tag streamlit-app:latest public.ecr.aws/e3w4k9h3/streamlit:latest

 ## Push the image
 docker push public.ecr.aws/e3w4k9h3/streamlit-app:latest