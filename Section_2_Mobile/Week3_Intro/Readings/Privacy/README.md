# Reading: Privacy Considerations

## The design of graph-based privacy protection mechanisms for mobile systems (2019)

Authors: Zhong Zhang, Sungha Yoon, and Minho Shin

This article discusses the notion of `elevation of privacy paths`. These vulnerabilities allow an attacker to use different `coarse sensors` as a mechanism to get more precise information.

They propose an algorithm to track a user without GPS that is based on various motion sensors on the device. This allows them to approximate the `pedestrian dead reckoning`.

### Issues with this scenario

It would be easier to track the users movement by periodically pinging some http endpoint and then use geo-ip. That would be crudely as simple without requiring the physics calculations.
