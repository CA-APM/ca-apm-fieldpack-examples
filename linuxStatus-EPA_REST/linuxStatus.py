#!/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#note above line is for MacPorts python (with Requests module) 
#!/usr/bin/env python

# This is a simple Collector Program who's intent is to demonstrate how
# we can collect simple Metrics and submit them to CA Wily via
# the RESTful interface that is part of the EPAGent.
#
# This script will collect system statistics from a Linux Host.  The
# statistics are stored under the following groups:
#
#       CpuUsage:
#           Information harvested from /proc/stat file and providing 
#           detailed information on how the CPU is being used over time.
#
#       Load:
#           Information harvested from /proc/loadavg file and reports the load1,
#           load5, and load10 load average for the host being monitored
#
#       MemInfoKB:
#           Information harvested from the /proc/meminfo file and reports
#           on memory statistics for the host being monitored.
#
# The metrics will be default be reported under 'linuxStats|<hostname>|...'.  As
# multiple hosts can report to a single EPAgent's RESTful interace.  The inclusion
# the <hostname> in the metric path gives a opportunity to disambiguate those
# usages.
#
# Requirements:
#
#   This script requires the 'requests' python package in order to process the
#   RESTful queries.  This can be obtained in one of the following ways:
#
#       # yum install python-requests
#                   or
#       # pip install requests
#                   or
#       # easy_install requests
#
# Usage:
#
#        Usage: linuxStatus.py [options]
#
#        Options:
#          -h, --help            show this help message and exit
#          -v, --verbose         verbose output
#          -H HOSTNAME, --hostname=HOSTNAME
#                                hostname EPAgent is running on
#          -p PORT, --port=PORT  port EPAgent is connected to
#          -m METRICPATH, --metric_path=METRICPATH
#                                metric path header for all metrics
#
#

import json
import optparse
import random
import requests
import socket
import sys
import time



def collectCpuInfo(metricDict, cpuHistory, metricPath):
    """
    This function collects CPU Information and reports iteration
    via metrics.  The data is harvested from the /proc/stat file.

    The first line of information in that file is formatted as
    follows:

      cpu <user> <nice> <system> <idle> <iowait> <irq> <softirq>

    Note:  These values are total since host booted.  To give
           usage over the interval being monitored must keep track
           of the previous values, so that they can be subtracted for
           this cycles count.
    """

    procStatFile = open("/proc/stat")
    statLines = procStatFile.readlines()
    procStatFile.close()

    cpuLine = statLines[0].split()
    if not "cpu" in cpuLine[0]:
        print "collection of CPU Info failed"
        return

    user = int(cpuLine[1])
    nice = int(cpuLine[2])
    system = int(cpuLine[3])
    idle = int(cpuLine[4])
    iowait = int(cpuLine[5])
    irq = int(cpuLine[6])
    softirq = int(cpuLine[7])

    # Do we have history we can rely on, or is this the first iteration
    if cpuHistory.has_key('user'):
        curUser = user - cpuHistory['user']
        curNice = nice - cpuHistory['nice']
        curSystem = system - cpuHistory['system']
        curIdle = idle - cpuHistory['idle']
        curIowait = iowait - cpuHistory['iowait']
        curIrq = irq - cpuHistory['irq']
        curSoftirq = softirq - cpuHistory['softirq']
        totalCPU = curUser + curNice + curSystem + curIdle + curIowait \
            + curIrq + curSoftirq

        # submit metrics to metricDict
        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:user'
        m['value']= "{0}".format(int(float(curUser)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:nice'
        m['value']= "{0}".format(int(float(curNice)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:system'
        m['value']= "{0}".format(int(float(curSystem)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)


        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:idle'
        m['value']= "{0}".format(int(float(curIdle)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:iowait'
        m['value']= "{0}".format(int(float(curIowait)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:irq'
        m['value']= "{0}".format(int(float(curIrq)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|CpuUsage:softirq'
        m['value']= "{0}".format(int(float(curSoftirq)/totalCPU * 100 + .5))
        metricDict['metrics'].append(m)

    # Store current usages for comparison on next harvest cycle
    cpuHistory['user'] = user
    cpuHistory['nice'] = nice
    cpuHistory['system'] = system
    cpuHistory['idle'] = idle
    cpuHistory['iowait'] = iowait
    cpuHistory['irq'] = irq
    cpuHistory['softirq'] = softirq


def collectLoadAvg(metricDict, metricPath):
    """
    Collect data from /proc/loadavg and submit them
    as metrics for harvesting
    """

    # Harvest loadaverage stats from /proc/loadavg
    procLoadavgFile = open("/proc/loadavg")
    loadavgLines = procLoadavgFile.readlines()
    procLoadavgFile.close()

    if len(loadavgLines) < 1:
        print "collection of loadAverage statistics failed"
        return

    loadLine = loadavgLines[0].split()
    load1 = int(float(loadLine[0]) + 0.5)
    load5 = int(float(loadLine[1]) + 0.5)
    load15 = int(float(loadLine[2]) + 0.5)

    # submit metrics to metricDict
    m = {}
    m['type'] = 'IntCounter'
    m['name'] = metricPath + '|Load:load1'
    m['value']= "{0}".format(load1)
    metricDict['metrics'].append(m)

    m = {}
    m['type'] = 'IntCounter'
    m['name'] = metricPath + '|Load:load5'
    m['value']= "{0}".format(load5)
    metricDict['metrics'].append(m)

    m = {}
    m['type'] = 'IntCounter'
    m['name'] = metricPath + '|Load:load15'
    m['value']= "{0}".format(load15)
    metricDict['metrics'].append(m)

def collectMemInfo(metricDict, metricPath):
    """
    Raw conversion of all data stored in /proc/meminfo
    into metrics to be harvested
    """

    procMemFile = open("/proc/meminfo")
    memfileLines = procMemFile.readlines()
    procMemFile.close()

    if len(memfileLines) < 1:
        print "collection of loadAverage statistics failed"
        return

    # Convert memfileLines into metrics
    for l in memfileLines:
        elems = l.split()
        m = {}
        m['type'] = 'IntCounter'
        m['name'] = metricPath + '|MemInfoKB:{0}'.format(elems[0][:-1])
        m['value']= "{0}".format(elems[1])
        metricDict['metrics'].append(m)





def main(argv):

    parser = optparse.OptionParser()
    parser.add_option("-v", "--verbose", help = "verbose output", 
        dest = "verbose", default = False, action = "store_true")

    parser.add_option("-H", "--hostname", default = "localhost",
        help = "hostname EPAgent is running on", dest = "hostname")
    parser.add_option("-p", "--port", help = "port EPAgent is connected to",
        type = "int", default = 8080, dest = "port")
    parser.add_option("-m", "--metric_path", help = "metric path header for all metrics",
        dest = "metricPath", default = "linuxStats|{0}".format(socket.gethostname()))

    (options, args) = parser.parse_args();

    if options.verbose == True:
        print "Verbose enabled"

    # Configure URL and header for RESTful submission
    url = "http://{0}:{1}/apm/metricFeed".format(options.hostname,
        options.port)
    headers = {'content-type': 'application/json'}

    if options.verbose:
        print "Submitting to: {0}".format(url)

    submissionCount = 0
    cpuHistory = {}

    while True:
        # Metrics are collected in the metricDict dictionary.
        metricDict = {'metrics' : []}

        collectCpuInfo(metricDict, cpuHistory, options.metricPath)
        collectLoadAvg(metricDict, options.metricPath)
        collectMemInfo(metricDict, options.metricPath)

        #
        # convert metric Dictonary into a JSON message via the
        # json package.  Post resulting message to EPAgent RESTful
        # interface.
        #
        r = requests.post(url, data = json.dumps(metricDict),
            headers = headers)

        if options.verbose:
            print "jsonDump:"
            print json.dumps(metricDict, indent = 4)

            print "Response:"
            print r.text

            print "StatusCode: {0}".format(r.status_code)

        submissionCount += 1
        print "Submitted metric: {0}".format(submissionCount)
        time.sleep(15)

if __name__ == "__main__":
    main(sys.argv)
