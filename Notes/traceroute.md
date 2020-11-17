The format of each hop line is as follows:

The name of the device or, if the device doesn’t identify itself, the IP address.
The IP address.
The time it took round trip for each of the three tests. If an asterisk is here, it means there wasn’t a response for that test. If the device doesn’t respond at all, you’ll see three asterisks, and no device name or IP address.

# traceroute

> Print the route packets trace to network host.

- Traceroute to a host:

`traceroute {{host}}`

- Disable IP address and host name mapping:

`traceroute -n {{host}}`

- Specify wait time for response:

`traceroute -w {{0.5}} {{host}}`

- Specify number of queries per hop:

`traceroute -q {{5}} {{host}}`

- Specify size in bytes of probing packet:

`traceroute {{host}} {{42}}`
