# Collection API

Collections are simple and light weight classes that can be used to store your items. So, how can they be used?

```csharp
var collection = new Collection<IItemInstance>();
```

Optionally, you can also use the built-in builder type.

```csharp
var builder = new CollectionBuilder<IItemInstance>();
var collection = builder.SetLogger(logger)
	.SetSize(slotCount)
	.SetSlotType<CollectionSlot<IItemInstance>>()
	.Build();
```

Here we're creating a collection of type IItemInstance. This means the collection can only store IItemInstance objects, or anything that inherits from IItemInstance.

## Registries

Collections have to be indexed in collection registries so it can be looked up at a later time.

It is recommended to register the collection by name and GUID. The name defines it's UI binding, while the ID defines it's unique instance (ID should always be unique per collection).

```csharp
using Devdog.InventoryPlus.Collections;

// Registering an item
CollectionRegistry.byID.Register(collectionGuid, collection);
CollectionRegistry.byName.Register(collectionName, collection);

// Un-Registering an item
CollectionRegistry.byID.UnRegister(collectionGuid, collection);
CollectionRegistry.byName.UnRegister(collectionName, collection);

// Getting an item from the registry
var collectionByID = CollectionRegistry.byID.Get(collectionGuid);
var collectionByName = CollectionRegistry.byName.Get(collectionName);
```

## Item Equality

In the example below 2 items that have the same item definition are considered equal, and can therefore be stacked. When calling a method like `GetAmount(myItem);` this will return the total amount of items equatable to "myItem".

```csharp
public class UnityItemInstance : IUnityItemInstance, IEquatable<UnityItemInstance>
{
	public bool Equals(IUnityItemInstance other)
	{
		return Equals((IItemInstance) other);
	}

	public bool Equals(UnityItemInstance other)
	{
		return Equals((IItemInstance) other);
	}

	public virtual bool Equals(IItemInstance other)
	{
		return itemDefinition.Equals(other?.itemDefinition);
	}
}
```

## API

To **get an item** from the collection use the sub ([]) operator.

```csharp
var item = collection[0];
```

To **add an item** we simply call the Add method.

```csharp
collection.Add(myItem);
```

Want to **add more than 1** item to the collection? Simply add a 2nd parameter to the method call.

```csharp
collection.Add(myItem, 3);
```

Want to **remove an item**?

```csharp
collection.Remove(myItem);
```

Want to **remove more than 1 item** from the collection? Simply add a 2nd parameter to the method call.

```csharp
collection.Remove(myItem, 3);
```

**Finding an item** in the collection.

```csharp
var index = collection.IndexOf(myItem);
```

.. Note:: IndexOf uses item equality to find items equatable to "myItem". If you want to find the index of a specific instance use `IndexOf(o => ReferenceEquals(o, myItem));` instead.

Using a **predicate to find** your item in the collection.

```csharp
var index = collection.IndexOf(o => o.name.Contains("Apple"));
```

Getting the **amount of items** in a collection.

```csharp
var amount = collection.GetAmount(myItem);
```

> Note that GetAmount uses item equality to find items equatable to "myItem". And thus will sum up the amount of equatable items in the collection.

Get the **amount of items at a specific index**.

```csharp
var amount = collection.GetAmount(3);
```

The **GetCanAddAmount** method will return the total amount of items you can add to this collection of the given type.

```csharp
var canAdd = collection.GetCanAddAmount(myItem);
```

## Using results

Most collection methods return a `Result<T>` type. Results store both the value and an optional error. When the error is empty the action is considered a success and the result field will be filled. If the error is not empty the action did not succeed and the collection remains unaffected.

```csharp
var added = collection.Add(myItem);

// added.error
// added.result
```

When our item is successfully added to the collection we can find information about the placement in the added.result variable. If the placement, however, went wrong for whatever reason, we'll get an error objects back in the added.error variable.

### Error objects

Errors can be compared to check which error was thrown when trying to place this item. All built-in errors can be found in the static `Errors` class.

```csharp
var added = collection.Add(myItem);
if(added.error == Errors.CollectionFull)
{
    // Aww, the collection is full; Can't place this item.
}
```

## Events

Collections also have built-in events. These will be fired when an item is added, removed or when a slot changes. These events can be very useful to repaint UI elements or to display messages to the player when the collection has changed.

> Event callbacks don't have an error object, as the event will *only* fire if the action has succeeded.

```csharp
collection.OnAddedItem += (sender, result) =>
{
    // result.affectedSlots = The slots changed by this action. If the stack is split between multiple slots this will return you all the modified slots.
    // result.item = The placed item.
    // result.amount = The placed amount
};
```

## Collection restrictions

Collection restrictions allow you to restrict your collection when adding or removing items. For example, you may want to prevent the user from removing a quest item from the collection. By using the restrictions you can prevent the user from dropping, selling, or in any other way removing the item from the collection.

```csharp
using System;
using Devdog.InventoryPlus.Collections;

public class MyRestriction<T> : ICollectionRestriction<T>
    where T: IEquatable<T>
{
    public Result<bool> CanAdd(T item)
    {
        return true;
    }

    public Result<bool> CanRemove(T item)
    {
        // You can also return an Error here to make it clear why the action failed.
        return false;
    }
}
```

To activate the restriction on a collection it has to be added to the collection's restrictions first.

```csharp
collection.restrictions.Add(new MyRestriction<IItemInstance>());
```

## Collection simulations

Want to do some crazy things? Using a collection simulation you can test if certain actions will succeed. For example, you may want to add 2 items, remove 3, move something around, and then add some more. Rather than running a 100 tests to make sure the action is valid, you can simply simulate the action and see if it succeeds.

```csharp
using (var sim = new CollectionSimulation<ItemDefinition>(collection))
{
    // Do crazy things here.
    var addResult = sim.collection.Add(someItem, 3);
    var removeResult = sim.collection.Remove(someItem, 5);

    if(addResult.error != null || removeResult.error != null)
    {
        // Whoops, something went wrong.
    }
}
```

After the using() block the sim.collection will be cleaned up by the garbage collector, and the original collection remains unchanged.

## Example of a custom collection

Of course, you can also implement your own collection if you so desire. To do this you can inherit from `CollectionBase<TSlotType, TElementType>` or implement the `ICollection<T>` interface.

```csharp
using System;
using Devdog.InventoryPlus.Collections;

public sealed class MyCollection<TElementType> : CollectionBase<ICollectionSlot<TElementType>, TElementType>
    where TElementType : IEquatable<TElementType>, IStackable, IIdentifiable, ICloneable<TElementType>
{
    public string name { get; set; }

    public Collection(int slotCount)
        : base(slotCount)
    {
        GenerateSlots<CollectionSlot<TElementType>>();
    }

    public override string ToString()
    {
        return name;
    }
}
```