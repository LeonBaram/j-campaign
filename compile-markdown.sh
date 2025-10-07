#!/bin/sh
yeeval ./elbar.yml && \
    mustache ./elbar.yml ./elbar-rockseeker.template.md > ./elbar-rockseeker.md
