prometheus-playground
=====================

It is set up that allow you run and try work with metrics. You can manage 
metrics and observe the results. As a backend here you can use `prometheus` and 
`victoria metrics`, this allows you to compare their work on the same data set.

## Usage

> In first time run you need to run `make download-victoriametrics-plugin`

You can run the project using one of the following commands:

- `make run`
- `make legacy-run`

After running the project, you will have fully set up grafana with datasource and dashboard.

URLs:

- new grafana http://localhost:3000/dashboards/ (login/password admin/admin)
- legacy grafana http://localhost:3001/dashboards/ (login/password admin/admin)
- prometheus http://localhost:9090/
- victoria metrics http://localhost:8428/

> The `request` folder contains http requests that you can perform to interact with the project.

References:

- https://grafana.com/blog/2019/12/04/how-to-explore-prometheus-with-easy-hello-world-projects/ - basic guide
- https://prometheus.io/docs/prometheus/latest/getting_started/ - a good, short description of how to write a prometheus config file
- https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/
- https://grafana.com/docs/grafana/latest/alerting/migrating-alerts/roll-back/ - manual how to enable old alerts
- https://grafana.com/docs/grafana/latest/administration/provisioning/#data-sources - how configure data sources and dashboards automatically
- https://github.com/VictoriaMetrics/grafana-datasource?tab=readme-ov-file#install-via-docker - how to install victoria metrics plugin to grafana
