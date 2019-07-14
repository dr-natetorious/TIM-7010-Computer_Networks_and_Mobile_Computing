# Reading: Privacy Considerations

## The design of graph-based privacy protection mechanisms for mobile systems (2019)

Authors: Zhong Zhang, Sungha Yoon, and Minho Shin

This article discusses the notion of `elevation of privacy paths`. These vulnerabilities allow an attacker to use different `coarse sensors` as a mechanism to get more precise information.

They propose an algorithm to track a user without GPS that is based on various motion sensors on the device. This allows them to approximate the `pedestrian dead reckoning`.

### Issues with this scenario

It would be easier to track the users movement by periodically pinging some http endpoint and then use geo-ip. That would be crudely as simple without requiring the physics calculations.

## Preventing Data Over-Collection using Dynamic Permission Mapping in Mobile Cloud Framework (2017)

Authors: Chandru. T, Dinesh Ram.S, Praveen .A and Mrs.Geetha

This article proposes a solution for detecting data leaks using (1) Lucene search engine and (2) Levenshtein-distance technique. They perform these searches as part of a deep packet inspection and then drop the traffic if it violates the rules.

Deploying sequential scans of plaintext is difficult to scale and it requires passing mulitple filters over the same document several times. This can delay the availability of the transaction and impact the user performance.

To mitigate these challenges the authors propose first pushing the plaintext through Lucene based search engine, then measuring the distance of each token to a search term. Each token can be measured independently across a cluster of nodes to speed up the detection.

### Issue with this scenario

They also suggest proxying all outbound traffic for a critical application through a cloud based solution. Since this proxy would be receiving all traffic from all users of the protected application, it would need to be fully trusted. There is concern that the traffic has secrets in the first place, which introduces additional privacy challenges _while trying to mitigate_ privacy.

The device would also have a performance overhead of needing to send the traffic twice - (1) the cloud solution and (2) the original destination. If the cloud solution forwards the traffic then it would need to handle certificates for the device, and that would be limited to only enterprise environments.
