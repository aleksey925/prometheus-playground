prometheus-playground
=====================

This project shows how metrics are exported from a python application to prometheus.

The command to run all services: `docker-compose up`

### application

- The command to get the index page. During page opening, the my_app_open_page_total 
metric is incremented.

    ```curl localhost:8000/```

- Command to retrieve metrics from an application:

    ```curl localhost:8000/metrics```

### grafana

- UI http://127.0.0.1:3000/ (login/password admin/admin)

Manual how to enable old alerts https://grafana.com/docs/grafana/latest/alerting/migrating-alerts/roll-back/.


### prometheus

- UI prometheus: http://localhost:9090

- The command to reload prometheus config:

    ```curl -X POST localhost:9090/-/reload```


References:

- https://grafana.com/blog/2019/12/04/how-to-explore-prometheus-with-easy-hello-world-projects/ - basic guide
- https://prometheus.io/docs/prometheus/latest/getting_started/ - a good, short description of how to write a prometheus config file
- https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/
