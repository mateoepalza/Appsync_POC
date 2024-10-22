requirements:
	pip install -r requirements-dev.txt && pip install -r ./src/shared/requirements.txt

build:
	sam build

deploy:
	sam deploy \
		--stack-name="appsync-poc" \
		--parameter-overrides="Stage=lab" \
		--capabilities=CAPABILITY_IAM \
		--resolve-s3 \
		--no-confirm-changeset \
		--no-fail-on-empty-changeset