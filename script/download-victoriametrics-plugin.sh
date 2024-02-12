#!/bin/bash
PLUGIN_DIR="./config/grafana/plugins"
LATEST=$(curl -s https://api.github.com/repos/VictoriaMetrics/grafana-datasource/releases/latest | grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' | head -1) && \
curl -L https://github.com/VictoriaMetrics/grafana-datasource/releases/download/$LATEST/victoriametrics-datasource-$LATEST.tar.gz -o "$PLUGIN_DIR"/plugin.tar.gz && \
tar -xf "$PLUGIN_DIR"/plugin.tar.gz -C "$PLUGIN_DIR"/ && \
rm "$PLUGIN_DIR"/plugin.tar.gz
