# Reading: Permissions

## Android Permissions Demystified (2011)

Authors: Adrienne Porter Felt, Erika Chin, Steve Hanna, Dawn Song, David Wagner

This article explores the mechanics of Android permissions and discusses the challenges of running with least privileges.

To determine what permissions are actually required, they enabled permission auditing on the Android kernel. Next they generated unit tests and attempted to maximize the code coverage across the official Android SDK.

There were challenges invoking all methods as some required precisely configured data structures or similar memory allocations. Manual tests were created for targeted areas that could not be covered through automation.

Afterwards, they discovered that there are many disconnects between the implementation and the documentation of the required permissions. They suspected some of these were vulnerabilitys and similar elevation paths.

## Role-based Privilege Isolation: A Novel Authorization Model for Android Smart Devices (2011)

Authors: Batsayan Das, Lakshmipadmaja Maddali, and Harshita Vani Nallagonda

The article describes a `Role based Privilege Isolation` model which uses roles to categorize the desired behavior and sharing of data.

While Android already has systems in place for sandboxing applications it does not have protections against the application being compromised, e.g., through cross-site scripting attacks.

They propose creating _multiple personas_ such as "browsing secure banking" versus "random surfing", and then run the applications in the _desired context_. This reduces the attack surface as these different `roles` are isolated from each other.

Most alternative solutions do not address the scenario of an app is compromised, and attacks another instance of itself. Their solution addresses these scenarios by allowing multiple roles per app and therefore limiting the (1) data, (2) permissions, and (3) functional or app usage categorization.

### What is the key idea of this work

The main idea is to have introduce *multiple application contexts* to Android a traditionally "single user model". That is not to say that Android which is based on Linux is truly a single user model (e.g. DOS 1.0) but there is not clear separations between different use cases.

![android_role_arch.png](android_role_arch.png)
![android_role_comp.png](android_role_comp.png)

