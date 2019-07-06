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

### ANSwer: Combining NFV and SDN Features for Network Resilience Strategies

The authors proposed a solution that uses monitoring at the SDN controller level to detect network anomalies.

When an anomaly is detected the system will attempt to remediate by deploying various complementary NFV devices.

For instance, if a virtual honeypot is being attacked; then the SDN module will deploy additional an IDS/IPS solutions to that flow.

As the attacks subside the additional protections can be terminated to improve network latency.
