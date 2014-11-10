
# README

The linuxStatus.py file is an example of how to utilize the EPAgent RESTful interface to send bulk metrics.  The script monitors a Linux host, gathering statistics about CPU usage, load averages, and memory usage for the host.  It submits those statistics as metrics (formatted in JSON) to CA APM Enterprise Manager via the EPAgent RESTful interface on a 15-second harvest cycle.  Metrics are submitted to the http://<epagenthost-port>/apm/metricFeed URL.

The script is fully functional and requires that the Requests module for Python be installed.

Additional details are available on the [CA APM Developer Community](http://bit.ly/caapm_dev/).
