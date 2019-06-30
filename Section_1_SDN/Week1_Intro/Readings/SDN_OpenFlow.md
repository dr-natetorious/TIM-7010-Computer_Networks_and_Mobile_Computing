# SDN with OpenFlow; Azodolmolky (2013)

In [this textbook](https://ebookcentral.proquest.com/lib/ncent-ebooks/detail.action?docID=1477475&query=Software+Defined+Networking+with+OpenFlow), Azodolmolky covers the implementation of SDN through OpenFlow. he continues with Python based examples for implementing different aspects of the SDN system.

## Chapter 1: Introducing OpenFlow

The separation between policy and forwarding devices is implemented as `FlowTables` (FT). Each entry within the table maps `matching criteria` to zero or more `actions` that need be performed on the `flow`. These actions are limited to the developers imagination, such as conditionally dropping or duplicating the traffic. Performance metrics are also exposed and can be used for quota based systems and similar multi-tenant scenarios.

Pure OpenFlow compatible devices do not perform onboard controls and rely completely on the `controller` to provide forwarding rules. The controller can be thought of as the `Network Operating System`, and similar to a computer's operating system -- makes all the decisions around access and resource sharing.

The chapter concludes with a multi-page enumeration of the various features that are expressed within the OpenFlow messages. For instance messages can be passed to add or remove routes. More complicated policies can be expressed such as `barriers` and `queuing` to enforce order of operations.

## Chapter 2: Implementing the OpenFlow Switch

Many vendors have created OpenFlow compatible switches as their is minimal complexity. Because the logic is contained within the controller, it is possible to use simple ASIC hardware based systems. This provides very fast implementations that are cheap to maintain.

`Mininet` is a software based solution that can be used to simulate large scale software defined networks using minimal hardware (e.g. single laptop). A tutorial then followed for using `Wireshark` and `Mininet` to simulate and record traffic between 3 hosts.

## Chapter 3: The OpenFlow Controller

The controller implements (1) the interface to interact with network switches; and (2) provide the programmable API for network applications.

Under a `reactive control model`, a OpenFlow Switch needs to contact the controller each time the flow begins. The controller will then reply with the desired policy and the converation will continue for that session. `Proactive control models` instead broadcast the policy to each of the NF which must locally cache them. This gives a trade off between `centralized versus decentralized` design.

Note: Traditional networks are `packet switching networks` which means that an individual packet is self contained. OpenFlow based systems operate on a higher contruct called Flows. Since a flow spans multiple packets this results in easier management of the session. It is also possible to group multiple related flows into `aggregate flows`, such as (1) all traffic between two physical machines; or (2) all web server traffic.

The chapter concludes with example controllers such as NOX (C++), POX (Python), NodeFlow (JavaScript), Floodlight (Java), and OpenDayLight.

## Chapter 6: Network Slicing (Virtualization)

Network virtualization combines multiple workloads on the same physical hardware. It's worth mentioning that Software-defined Network ( SDN ) separates the data plane and the control plane, but the goal of network virtualization is to construct multiple virtual networks on top of a physical networking infrastructure.
