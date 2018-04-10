# CollectionSlot and LayoutCollectionSlot

Collection slots are used inside collections. These slots are stored inside a collection, which in turn will contain the actual items in the collection. These slots are used to store all relevant data in one location.

## CollectionSlot

The `ICollectionSlot` interface allows you to implement your own collection slots. By default the `CollectionSlot<T>` type is used.

```csharp
using System;
using Devdog.InventoryPlus.Collections;

public class MyCollectionSlot<T> : CollectionSlot<T>
    where T : IEquatable<T>, IStackable
{
    public override void Set(T item, int amount)
    {
        base.Set(item, amount);

        // Implement your own behavior here...
    }
}
```

## LayoutCollectionSlot

The ILayoutCollectionSlot interface allows you to implement your own layout collection slot. By default the `LayoutCollectionSlot<T>` is used.

```csharp
using System;
using Devdog.InventoryPlus.Collections;

public class MyLayoutCollectionSlot<T> : LayoutCollectionSlot<T>
    where T : IEquatable<T>, IStackable
{
    public override void Set(T item, int amount)
    {
        base.Set(item, amount);

        // Implement your own behavior here...
    }
}
```

## Using a custom slot in a collection

To use your new [Collection](Collection.md) slot on any collection we'll have to tell the collection to generate new slots with our new type.

!!! danger
    Note that generating new slots will wipe all data from the collection.

!!! note
    [Layout Collections](LayoutCollection.md) require the slot to implement the `ILayoutCollectionSlot<T>` interface instead of `ICollectionSlot<T>`.

```csharp
var collection = new Collection<ItemDefinition>(10);
collection.GenerateSlots<MyCollectionSlot<ItemDefinition>>();
```

```csharp
var layoutCollection = new LayoutCollection<ItemDefinition>(4, 4);
layoutCollection.GenerateSlots<MyLayoutCollectionSlot<ItemDefinition>>();
```
