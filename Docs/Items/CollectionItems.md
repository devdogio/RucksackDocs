# Collection Items

In this example we'll create an item that has a collection of it's own. This means the item can store items of it's own, like a bag or container item.

> We're inheriting from the built-in unity-dependent item instance. This is not required, but simply gives us the basic elements without having to redo all the work.

```csharp
using UnityEngine;
using Devdog.InventoryPlus.Collections;

[System.Serializable]
public class MyItemInstance : IUnityItemInstance, IEquatable<IUnityItemInstance>
{
	public ICollection<IItemInstance> collection { get; }

    public Guid ID { get; }
    public IItemDefinition itemDefinition { get; }
    public int maxStackSize
    {
        get { return itemDefinition.maxStackSize; }
    }
    
    // Add stats to the run-time item.
    public Stat[] stats = new Stat[0];
    
    // For (de)serialization...
    private MyItemInstance()
    { }
    
    public MyItemInstance(Guid ID, IItemDefinition itemDefinition)
    {
        if (itemDefinition == null)
        {
            throw new ArgumentException("Given ItemDefintiion is null!");
        }
        
        this.ID = ID;
        this.itemDefinition = itemDefinition;
    }
    
    // ... Removed for clarity
}
```