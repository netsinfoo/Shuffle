docker run \
	--env DOCKER_API_VERSION=1.40 \
	--env ENVIRONMENT_NAME="Shuffle" \
	--env BASE_URL="http://192.168.86.45:5001" \
	--env HTTP_PROXY="http://192.168.86.45:8082" \
	--env HTTPS_PROXY="https://192.168.86.45:8082" \
	--env SHUFFLE_PASS_WORKER_PROXY=true \
	--env SHUFFLE_PASS_APP_PROXY=true \
	-v /var/run/docker.sock:/var/run/docker.sock \
	ghcr.io/frikky/shuffle-orborus:nightly
