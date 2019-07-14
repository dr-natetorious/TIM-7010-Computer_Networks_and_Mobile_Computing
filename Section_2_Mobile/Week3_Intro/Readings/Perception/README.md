# Readings: User Perception of Security

## Investigating User Perception and Comprehension of Android Permission Models

Authors: Anthony Peruma, Jeffrey Palmerino and Daniel E. Krutz

The authors performed an inperson survey of 186 people and concluded:

1. The current model (prompt at runtime for dangerous api) versus old model (prompt at install time) does not make the user feel safer.
2. Propose an alternative model that does make people feel safer
3. There is no statistical relevance between application permissions and user ratings
4. Runtime permission models are more effective as the user has recall of granting it
5. Users generally understood the impact of the requested permission, but age does play a factor

### Related Works

There has been multiple efforts into measuring user comprehension of complex dialogs. One of those studies found that only 17% of participants read the warnings and 3% passed a permissions test afterwards. This aligns with my personal experience that we click accept until the app starts.

Others have proposed models that allow a subset of the requested permissions or running the application in a quarantinee mode. There have been expansions on this idea such as recommendation systems where expert users provide guidance.

A novel idea was to expose a settings pane and then when features of the application are enabled, then grant/revoke the permissions. This gives a granular approach that aligns with the users privacy concerns.

They investigated how permissions are added to apps and found that once they are added they typically are not removed. This leads to apps continuing to "collect dust."

### New Work

From the survey they found that users responded better to the runtime dialogs, and decided to augment it with additional information. They landed on displaying a short list of other applications that also use this permission.

### ... but wait a second

This made users feel more safe about approving permissions and continuing forward. However, there needs to be additional research is needed as they are disassociating the permission and associating the confidence in the application ring. -- `"If chrome does it, and I trust Google; then it must be safe"`.

There are also additional problems with the user flow as it halts the application and makes the user explicitly perform an action. This can be annoying especially if asked too many times. Basically they are describing the same challenges as `Windows Vista User Access Control (UAC)` as it was first released.

## Improving Android Permissions Models for Increased User Awareness and Security (2018)

Authors: Jeffrey Palmerino

This is a summary submission of the above effort. Wonder if his team mates know that he is taking all the credit on this second printing?
