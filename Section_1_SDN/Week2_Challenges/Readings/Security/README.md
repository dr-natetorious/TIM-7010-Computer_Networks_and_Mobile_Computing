# Challenges in Security

The core security risks to software defined networks are:

1. Information Discloser and Compromised Controller
2. Distributed Denial of Service Attacks

## Information Discloser and Compromised Controller

One solution for partially mitigating these scenarios is with [Muli-Party Computation](SMPC.md).

It is a cryptographic scheme that combines:

- Secure Multi-Party Computation Protocol (low computation / highly chatty protocol)
- Fully Homomorphic Encryption (high computation / low chatty protocol)

Afterwards the integrity of the system can be validated for `k controllers`, provided _at least one_ controller is not compromised.

## Distributed Denial of Service

These attacks [discussed in detail](DDos.md), come in two flavors:

- Network Layer Attacks (high volume, easy to detect)
- Application Layer Attacks (arbitrary volume, hard to detect)

Different strategies are required to detect each scenario. Afterward, the system can respond with a `resiliency strategy` such as increasing scale or blocking a user.

Application Layer (e.g. HttpGet-Flooding) is becoming an ever complex categorization problem of `human, evil bot, and good bot`. This cat and mouse game is the current "big picture strategy" used to address these issues.

One approach would be to dynamically deploy and configure NFV devices from SDN in response to changes in traffic patterns. Another solution would be to score the user traffic relative to the general population, this could be fed into a QoS model or some sort of priority queue structure.
