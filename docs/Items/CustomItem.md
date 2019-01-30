# Creating custom items

See [Items](Items.md) for a detailed description about item instances and item definitions.

## Item Registry

The `ItemRegistry` is responsible for keeping track of all item instances.
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
using Devdog.General2;
using Devdog.Rucksack;
using Devdog.Rucksack.Items;
using System;

using UnityEngine;

[System.Serializable]
public class MyItemInstance : UnityItemInstance, IEquatable<MyItemInstance>
{
	// For (de)serialization...
	protected MyItemInstance()
	{ }

	public MyItemInstance(Guid ID, IUnityItemDefinition itemDefinition)
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

		// Fetch a custom component from your player object and check its level.
		var myComponent = character.GetComponent<MyComponent>();
		if (myComponent.playerLevel < ((MyItemDefinition)itemDefinition).level)
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
using Devdog.Rucksack.Items;
using UnityEngine;

public class MyItemDefinition : UnityItemDefinition
{
	[SerializeField]
	private int _level;
	public int level
	{
		get { return _level; }
	}
}
```

## Item Factory binding

The `ItemFactory` is a simple static class that is used to create new item instances of item definition types.

!!! note
​	For each custom item definition type you have to register a binding with an instance type in the item factory.

```csharp
// Create a binding between the UnityItemDefinition and the UnityItemInstance.
// When you're trying to create a new instance of UnityItemDefinition this will ensure a new instance of UnityItemInstance will be returned.
ItemFactory.Bind<UnityItemDefinition, UnityItemInstance>();

// Creates a new instance for the given itemDefinition. Based on the itemDefinition type and the set bindings a new instance will be returned.
var inst = ItemFactory.CreateInstance(itemDefinition, System.Guid.NewGuid());
```