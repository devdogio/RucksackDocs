# Collections

Collections can store any reference type by default, so long these types implement the `IEquatable<T>, IStackable, IIdentifiable, ICloneable<T>` interfaces. In other words, the type has to be equatable to itself, be stackable (can be set to 1), identifiable and cloneable.

> All items stored in a collection are never modified by the collection itself. This is beneficial because it allows us to duplicate the collection without ever needing to duplicate the items. On top of this it also simplifies serialization, as all relevant data is in the same location, the slot.

### ICollection and Collection

By default the Collection class can be used to instantiate a new collection. if you, however, want more control over your types you can implement a new collection by inheriting from `CollectionBase<TSlotType, TElementType>`, or by implementing the `ICollection<T>` interface.

### CollectionBase

`CollectionBase<TSlotType, TElementType>` is an abstract base class that implements the `ICollection<T>` interface. The `CollectionBase<TSlotType, TElementType>` class has virtual members that can be overwritten to change the base behavior. If you want to implement your own collection type it's recommended to inherit from `CollectionBase<TSlotType, TElementType>`.

### Collection slots

The `CollectionBase<TSlotType, TElementType>` uses a [CollectionSlot](CollectionSlot.md) to store it's items and additional information into. This is done to make sure that all data relevant to the item is stored in the slot, and not on the item. Items are therefore never modified by the collection.

### Collection groups
See [CollectionGroups](CollectionGroup.md) for more information.

## Using collections

Collections are simple and light weight classes that can be used to store your items. So, how can they be used?

```csharp
var collection = new Collection<ItemDefinition>();
```

Here we're creating a collection of type ItemDefinition. This means the collection can only store ItemDefinition objects, or anything that inherits from ItemDefinition.

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

Using a **predicate to find** your item in the collection.

```csharp
var index = collection.IndexOf(o => o.name.Contains("Apple"));
```

Getting the **amount of items** in a collection.

> This will return the total amount of equatable items in this collection.

```csharp
var amount = collection.GetAmount(myItem);
```

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

When our item is successfully added to the collection we can find information about the placement in the added.result variable. If the placement, however, wen't wrong for whatever reason, we'll get an error objects back in the added.error variable.

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

To use the restriction in a collection it has to be added first.

```csharp
collection.restrictions.Add(new MyRestriction<ItemDefinition>());
```

## Collection simulations

Want to do some crazy things? Using a collection simulation you can test if certain actions will succeed. For example, you may want to add 2 items, remove 3, move something around, and then add some more. Rather than running a 100 tests to make sure the action is valid, you can simply simulate the action, see if it succeeds.

```csharp
using (var sim = new CollectionSimulation<ItemDefinition>(collection))
{
    // Do crazy things here.
    var addResult = sim.collection.Add(someItem, 3);
    var removeResult = sim.collection.Remove(someItem, 5);

    if(addResult.error != null || removeResult.error != null)
    {
        // Whoops, something wen't wrong.
    }
}
```

After the using() block the sim.collection will be cleaned up by the garbage collector, and the original collection remains unchanged.

## Example of a custom collection

Of course, you can also implement your own collection if you so desire. To do this you can inherit from `CollectionBase<TSlotType, TElementType>` or implement the `ICollection<T>` interface.

```csharp
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