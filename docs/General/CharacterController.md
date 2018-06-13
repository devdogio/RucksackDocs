# Custom Character Controller

When using your own character controller you're required to implement the IInventoryPlayerController interface. The IPlayerInputCallbacks (in the namespace Devdog.General) is used to enable / disable the controller when the UI requests it.

```csharp
using UnityEngine;
using Devdog.General2;

public class MyPlayerController : MonoBehaviour, IPlayerInputCallbacks
{
    public virtual void SetInputActive(bool val)
    {
        // This method is called by UIWindow's and other blocking elements that request the player controller to be deactivated.
        // Enable / disable your controller.
        enabled = val;
    }
}
```