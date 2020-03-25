# https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html

aws ecr create-repository --repository-name xxx > /dev/null
aws ecr get-login --region eu-west-1 --no-include-email
docker login -u AWS -p HASHED_KEY_FROM_ABOVE
docker build -t xxx
docker tag xxx xxx
docker push xxx
