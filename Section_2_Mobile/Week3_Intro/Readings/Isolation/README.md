# Readings: Isolation Strategies

## Study of an effective way of Detecting Unexpected Permission Authorization to Mobile Apps (2017)

Authors: Manisha Patil and Prof. Dr.Dhanya Pramod

There are four layers that can be attacked:

- Application Layer
- Operating System Layer
- Hardware Layer
- Infrastructure Layer

![threats_to_mobile.png](threats_to_mobile.png)

## Application Layer

Previous research attempted to monitor the operating system events, such as linux kernel events. Others have used similar telemetry feeds combined with machine learning algorithms.

Researchers have also identified that the number of permissions required for modern applications is increasing. This is resulting in more attack surface through more complex interactions.

Some have proposed more granular permission models and allowing the user capabilities to twiddle them off/on. ~This relies on the user to be deeply technical and would be difficult to implement in pratice. To further compound these challenges it has been proposed that no one understands the permissions model and resulting in exceess rights.~

To protect the application others have created sandboxing and isolation technologies that can be repacked into an existing package. This is an interesting solution and typically repackaing is used for malicious purposes such as advertising revenue hijacking.

More common solutions involve taint flow analysis and decompiling during the installation phase. If the package is detected to be malicious (using heuristics); then it is quarintined or removed. Some anti-virus solutions run the suspicious malware remotely on emulators in the cloud. This enables the AV to monitor the telemetry.

## Research on Android Access Control based on Isolation Mechanism (2016)

Authors: Ying Peng, Mingxin Zhang, Jinlong Zheng, and Zhenjiang Qian

Privilege management is an important component of the Android security system, however it has defects due to:

- Coarse-Grained Authorization Mechanism (all or nothing at install time)
- Coarse-Grained Permissions (all or nothing over broad functionality)

Solutions to these issues have been difficult to gain traction, such as:

- no one tests applications with partial rights
- design is based on SELinux policy which does not align with the mobile paradigm
- trustzones (e.g., multiple virtual machines on single device) are impactical for most non technical users
- partial rights to devices are difficult to manage as developers do not fully understand what is needed

Applications are isolated as separate linux users and can chose to share the same group with related applications (e.g. Google Maps and Google Gmail). All permissions are declared at installation time and then inherited to components of the package. These are registered within the `AndroidManifest.xml`.

The authors propose going one step further and introduced a three-tier solution:

- Application Layer
- Virtual Memory Manager
- Trusted Root

Their model sounds like they copy pasted the approach used by desktop systems with `ring-0` and `ring-3` protected modes.
