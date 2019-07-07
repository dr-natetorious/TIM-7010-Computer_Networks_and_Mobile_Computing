# Quality of Service in SDN

## Survey of Concepts for QoS improvements via SDN (2015)

To provide QoS, application flows need to be differentiated as they compete for bandwidth. These sources need to be allocated porportionally.

### What do traditional networks use

Traditional networking relies on:

- Integrated Services: Used by small networks that reserve router resources _per flow_.
- Differentiated Services: Course control based on the `8-bit DS field` in IP header (aka priority queued).

Both implementations are difficult to scale and maintain end-to-end QoS. Bandwidth Brokers have been introduced to partially mitigate these limitations, but require that all routers along the path support them. Even after deployed to all routers, the protocol is implemented differently be vendors and it is not possible to holistically apply across the global internet.

### What do SDN enables systems do

Rules can be configured per flow and then be applied at either

- QoS for a specific tenant or a business customer flow
- QoS for a specific application flow

These are typically implemented as `virtual slicing` of available bandwidth, which uses _resource reservations_ or _per-flow dynamic routing_. More advanced scenarios will en-queue the packets based on policy being exceeded.

### Future work

The concept of Control Exchange Points (CXP) has been proposed as an architectual model to improve end-to-end  QoS across the internet. However, it requires all ISPs to play nicely with each other.

Most of the investigation into SDN/QoS has been performed on small topologies and is largely unproven on larger scales.

## B4: Experience with a Globally-Deployed Software Defined WAN (2013)

Google connected each of their data centers through a private WAN using OpenFlow. This is one of the largest published implementations of SDN
