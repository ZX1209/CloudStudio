# ip

> Show / manipulate routing, devices, policy routing and tunnels.

- List interfaces with detailed info:

`ip a`

- Display the routing table:

`ip r`

- Make an interface up/down:

`ip link set {{interface}} up/down`

- Add/Delete an ip address to an interface:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Add a default route:

`ip route add default via {{ip}} dev {{interface}}`


## man page
IP - COMMAND SYNTAX
   OBJECT
       address
              - protocol (IP or IPv6) address on a device.

       addrlabel
              - label configuration for protocol address selection.

       l2tp   - tunnel ethernet over IP (L2TPv3).

       link   - network device.

       maddress
              - multicast address.

       monitor
              - watch for netlink messages.

       mroute - multicast routing cache entry.

       mrule  - rule in multicast routing policy database.

       neighbour
              - manage ARP or NDISC cache entries.

       netns  - manage network namespaces.

       ntable - manage the neighbor cache's operation.

       route  - routing table entry.
       mrule  - rule in multicast routing policy database.

       neighbour
              - manage ARP or NDISC cache entries.

       netns  - manage network namespaces.

       ntable - manage the neighbor cache's operation.

       route  - routing table entry.

       rule   - rule in routing policy database.

       tcp_metrics/tcpmetrics
              - manage TCP Metrics

       token  - manage tokenized interface identifiers.

       tunnel - tunnel over IP.

       tuntap - manage TUN/TAP devices.

       xfrm   - manage IPSec policies.

       The names of all objects may be written in full or abbreviated form, for example address can be abbreviated as addr or just a.

  COMMAND
       Specifies the action to perform on the object.  The set of possible actions depends on the object type.  As a rule, it is possible to add, delete and show (or list ) objects, but some
       objects do not allow all of these operations or have some additional commands. The help command is available for all objects. It prints out a list of available commands and argument
       syntax conventions.

       If no command is given, some default command is assumed.  Usually it is list or, if the objects of this class cannot be listed, help.