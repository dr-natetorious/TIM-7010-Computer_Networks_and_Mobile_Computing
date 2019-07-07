# Quality of Service in SDN

## Survey of Concepts for QoS improvements via SDN (2015)

To provide QoS, application flows need to be differentiated as they compete for bandwidth. These sources need to be allocated porportionally.

### What do traditional networks use

Traditional networking relies on:

- Integrated Services: Used by small networks that reserve router resources _per flow_.
- Differentiated Services: Course control based on the `8-bit DS field` in IP header (aka priority queued).

Both implementations are difficult to scale and be difficult to maintain end-to-end QoS.
