# FAQ

## How do I add or remove items from a player's inventory?

```csharp
// Assign in inspector or fill through code.
public InventoryPlayer player;

// In your code (where item is an IItemInstance object)
var result = player.itemCollectionGroup.Add(item, 1);
if(result.error == null)
{
	// Success!
}
else{
	// Whoops, something went wrong! See result.error for details.
}
```

## How do I create an item instance?

Item instances can be created through the ItemFactory factory. The ItemFactory will return a new instance based on the item definition you pass into it. See [Items](../APIDocs/Items/Items.md) for more info.

```csharp
public UnityItemDefinition definition;

// Create the instance
var inst = ItemFactory.CreateInstance(definition, System.Guid.NewGuid());
```

## What's the difference between an item instance and an item definition?

An item definition is a persistent data structure that defines the item. The item instance is an instance object that wraps the definition and adds any run-time values. For example, an instance item can contain randomized generated stats at run-time, while the definition contains persistent information, like the item name, icon, etc.

You can of course create multiple instances of the same definition, while there is generally only 1 definition per specific item.

## What is a collection group?

A collection group is a group of collections that adds priority to each collection. For example, putting 2 collections into a single group where collection A has a priority of 5 and collection B has a priority of 10, all items will be stored in collection B first, as it has the highest priority.
See [Collection Group](../APIDocs/Collections/CollectionGroup.md) for more info.

## How do I check if a collection / player contains an item?

The `IInventoryCollectionOwner` is an interface used on objects or characters that defines it has an inventory collection available. We can grab this component, and through it, the inventories.

```csharp
var collectionOwner = someObject.GetComponent<IInventoryCollectionOwner>();
if(collectionOwner != null)
{
	// This object has an inventory collection
	var itemCount = collectionOwner.itemCollectionGroup.GetAmount(someItem);
	// Do something here...
}
```

## How do I equip / un-equip an item?

By calling the `IEquippableCharacter<TEquippableItemType>` Equip or EquipAt methods. See [Equipment](../APIDocs/CharacterEquipment/Equipment.md) for more info.

## How do I make NPC's with their own equipment?

Any character that contains a component that implements `IEquippableCharacter<TEquippableItemType>` is considered an equippable character. You can use the `UnityEquippableCharacter` component, or implement your own if you want more control. See [Equipment](../APIDocs/CharacterEquipment/Equipment.md) for more info.

## How do I extend the existing items / implement my own item behavior?

See [Custom items](../APIDocs/Items/CustomItem.md).

## How do I implement a character controller?

See [Custom Character Controller](General/CharacterController.md) for a description.