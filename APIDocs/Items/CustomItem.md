# Creating custom items

See [Items](Items.md) for a detailed description about item instances and item definitions.

## Item Registry

The `ItemRegistry` is responsible for keeping track of all run-time items.
Keep in mind that if you're going to create a new item instance you'll have to register it with the item registry.

```csharp
// Registering an item in the registry.
ItemRegistry.Register(itemGuid, item);

// Un-Registering an item from the registry.
ItemRegistry.UnRegister(itemGuid);

// Getting an item from the registry
var item = ItemRegistry.Get(itemGuid);
```

## Item Instance

```csharp
[System.Serializable]
public class MyItemInstance : UnityItemInstance, IEquatable<MyItemInstance>
{
    public Guid ID { get; }
    public IItemDefinition itemDefinition { get; }
    public int maxStackSize
    {
        get { return itemDefinition.maxStackSize; }
    }
    
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
    
	public override Result<bool> CanUse(Character character, ItemContext useContext)
	{
		var canUse = base.CanUse(character, useContext);
		if (canUse.result == false)
		{
			return canUse;
		}
		
		var myComponent = character.GetComponent<MyComponent>();
		if(myComponent.playerLevel < ((MyItemDefinition)itemDefinition).level)
		{
			return new Result<bool>(false, new Error(123, "Player level is too low"));
		}

		return true;
	}

	public override Result<ItemUsedResult> DoUse(Character character, ItemContext useContext)
	{
		// Do something fancy here...

		return new Result<ItemUsedResult>(new ItemUsedResult(useContext.useAmount, false, 0f));
	}

	public bool Equals(MyItemInstance other)
	{
		return base.Equals(other);
	}
}
```

## Item Definition

```csharp
using System;
using Devdog.General;
using Devdog.InventoryPlus.CharacterEquipment;
using Devdog.InventoryPlus.CharacterEquipment.Items;
using UnityEngine;

public class MyItemDefinition : UnityItemDefinition
{
	[SerializeField]
	private int _level;
	public int level
	{
		get { return _level; }
	}

	public override IItemInstance CreateInstance(Guid instanceGuid)
	{
		return new MyItemInstance(instanceGuid, this);
	}
}
```

## Example item stats


```csharp

```