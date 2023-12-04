
# Load environment variables from .env file
source .env

pytest --cov --cov-report xml --junitxml=test_report.xml &&

docker run \
    --rm \
    -e SONAR_HOST_URL="$SONAR_HOST_URL" \
    -e SONAR_TOKEN="$SONAR_TOKEN" \
    -v "$(pwd):/usr/src" \
    sonarsource/sonar-scanner-cli -X
