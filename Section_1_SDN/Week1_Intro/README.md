# Section 1: Week 2: Introduction to SDN

## Evolution to SDN

Traditional networks were built to be closed thick systems, that are deployed in a fairly static configuration.

Later the notion of virtualized network functions (NVF) (e.g. firewall or load balancer), reduced the opex and capex required to provision a device.

With virtualized networking those same thick systems could be duplicated in a shorter period of time. While this was an improvement it was still a thick closed layer.

Then the notion of software defined networks (SDN) was created to complement the NVF systems. This is accomplished through:

1. Standardizing the configuration across heterogenous networking functions (NF)
2. Decoupling that configuration from the data plane
3. Allowing for third party systems to extend the behavior of the management and control planes

For example; it is possible to trivial write a Python script that performs Network Access Controls Lists (NACL). Another script might implement a new multi-cast protocol. In either case the scripts need to register for the events of interest (e.g. rule matching) and then state the desired actions.

Afterwards, the data plane will receive the modified traffic flow and forward it to the required device endpoints.
