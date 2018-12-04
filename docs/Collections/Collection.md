# Collections

Collections can store any reference type, so long these types implement the `IEquatable<T>, IStackable, IIdentifiable, ICloneable` interfaces. In other words, the type has to be equatable to itself, be stackable (can be set to 1), identifiable and cloneable.

## Collection API

See [Collection API](CollectionAPI.md) on how to use the collections through code.

## Collection groups

See [CollectionGroups](CollectionGroup.md) for more information.

## Item Equality

Item equality is used to identify if items can be stacked, as well as to find items in the collection. For example, when using `GetAmount()` this will get the amount of all items that are equatable to the given type.

## ICollection and Collection

By default the Collection class can be used to instantiate a new collection. if you, however, want more control over your types you can implement a new collection by inheriting from `CollectionBase<TSlotType, TElementType>`, or by implementing the `ICollection<T>` interface.

## Collection Owners

The ICollectionOwner interfaces (`IInventoryCollectionOwner`, `IEquipmentCollectionOwner`, `ICurrencyCollectionOwner`) are used to indicate an object owns a collection. This is the common interface used to find inventory, equipment and currency collections on an object.

## Creating a collection

Using the `ItemCollectionCreator` or the `UNetItemCollectionCreator` for UNet you can create a collection. These 2 components can be attached to any Unity object. Optionally, you can also manually create collections through code. See the [Collection API](CollectionAPI.md) docs for more info.

## CollectionBase

`CollectionBase<TSlotType, TElementType>` is an abstract base class that implements the `ICollection<T>` interface. The `CollectionBase<TSlotType, TElementType>` class has virtual members that can be overwritten to change the base behavior. If you want to implement your own collection type it's recommended to inherit from `CollectionBase<TSlotType, TElementType>`.

## Collection slots

The `CollectionBase<TSlotType, TElementType>` uses a [CollectionSlot](CollectionSlot.md) to store it's items and additional information into. This is done to make sure that all data relevant to the item is stored in the slot, and not on the item. Items are therefore never modified by the collection.

## Collection UI and input handling

The `ICollectionSlotUICallbackReceiver<T>` (UI) and `ICollectionSlotInputHandler<T>` (Input handling) can be implemented into custom components to extend existing collection components. When using these interfaces you don't need to modify or replace any existing components. See [Collection Slot UI](CollectionSlotUI.md)