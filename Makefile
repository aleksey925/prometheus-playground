download-victoriametrics-plugin:
	bash ./script/download-victoriametrics-plugin.sh

legacy-run:
	docker compose up app grafana-legacy

run:
	docker compose up app grafana

down:
	docker compose down
