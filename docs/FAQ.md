# FAQ

### Errors on import

Getting errors like `cannot be used because it is not part of the C# 4.0 language specification` when importing Rucksack? Make sure you're using .Net 4.6 and that you're using Unity 2017.3+

### Can I use Rucksack for a singleplayer game?

Absolutely! Rucksack comes with singleplayer components and multiplayer components. In most cases it would be recommended to create a multiplayer game and run as a host (both server and client). If you intend to build a singleplayer game, and never want to support multiplayer you can use the singleplayer components. 

### Does Rucksack work with Photon / other network libraries?

Short answer: No. Rucksack only has a pre-built integration with UNet. All other networking libraries are not officially supported. Other networking systems, like photon, can be implemented manually.

### Is Rucksack compatible with Inventory Pro?

Rucksack is not compatible with Inventory Pro. Inventory pro is a singleplayer only inventory solution which strongly leans towards RPG and survival games. Rucksack is multiplayer ready and game-agnostic, meaning that it does not have any game specific integrations and due to it's flexibility can support any game type.

### The difference between Rucksack and Inventory Pro

| Feature | Rucksack | Inventory Pro |
| ------------- |:-------------:|:--------------:|
| Multiplayer | ✅ | ❌ |
| Authoritative server | ✅ | ❌ |
| Modular design | ✅ | ❌ |
| Modular UI system | ✅ | ❌ |
| Modular input system | ✅ | ❌ |
| .Net 4.6 | ✅ | ❌ |
| Item Inheritance | ✅ | ❌ |
| NPC equipment | ✅ | ❌ |
| NPC inventory | ✅ | ❌ |
| Inventory | ✅ | ✅ |
| Player Equipment | ✅ | ✅ |
| Vendor | ✅ | ✅ |
| Bank | ✅ | ✅ |
| Item editor | ✅ | ✅ |
| Stat system | ❌ | ✅ |
| Crafting | ❌ | ✅ |

#### Feature descriptions

- **Multiplayer**: A full fledged multiplayer integration based on UNet.
- **Authoritative server**: Server authority over all actions (cheat proof).
- **Modular Design**: All components are modular, ranging from input to vendors and collections.
- **Net 4.6**: Rucksack uses the latest version of .Net for future compatibility and ease of use.
- **Item Inheritance**: Create variations of items through [Item Inheritance](Items/Items.md#item-definition).
- **NPC Equipment**: Visually equip items to any character, such as, your NPCs.
- **NPC Inventory**: Give any object or instance it's own inventory.

### How do I add or remove items from a player's inventory?

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

### UNet is not working, why?

Unity deprecated UNet in 2019+. Because of this we've decided to split the package off into it's own separate .unity package, downloadable from the [devdog.io](https://devdog.io/unity-assets/rucksack-multiplayer-inventory-system/community-bonus/) website.

### What if I'm using Unity 2019+ and want to utilize networking?

For 2019+ we have a package on the [devdog.io](https://devdog.io/unity-assets/rucksack-multiplayer-inventory-system/community-bonus/) website named mirror. [Mirror](https://github.com/vis2k/Mirror) is a community driven replacement for UNet, that is more stable and has (almost) the same API and method signatures and UNet, making migrations very simple. 

### How do I create an item instance?

Item instances can be created through the ItemFactory factory. The ItemFactory will return a new instance based on the item definition you pass into it. See [Items](Items/Items.md) for more info.

```csharp
public UnityItemDefinition definition;

// Create the instance
var inst = ItemFactory.CreateInstance(definition, System.Guid.NewGuid());
```

### What's the difference between an item instance and an item definition?

An item definition is a persistent data structure that defines the item. The item instance is an instance object that wraps the definition and adds any run-time values. For example, an instance item can contain randomized generated stats at run-time, while the definition contains persistent information, like the item name, icon, etc.

You can of course create multiple instances of the same definition, while there is generally only 1 definition per specific item.

### What is a collection group?

A collection group is a group of collections that adds priority to each collection. For example, putting 2 collections into a single group where collection A has a priority of 5 and collection B has a priority of 10, all items will be stored in collection B first, as it has the highest priority.
See [Collection Group](Collections/CollectionGroup.md) for more info.

### How do I check if a collection / player contains an item?

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

### How do I equip / un-equip an item?

By calling the `IEquippableCharacter<TEquippableItemType>` Equip or EquipAt methods. See [Equipment](CharacterEquipment/Equipment.md) for more info.

### How do I make NPC's with their own equipment?

Any character that contains a component that implements `IEquippableCharacter<TEquippableItemType>` is considered an equippable character. You can use the `UnityEquippableCharacter` component, or implement your own if you want more control. See [Equipment](CharacterEquipment/Equipment.md) for more info.

### How do I extend the existing items / implement my own item behavior?

See [Custom items](Items/CustomItem.md).

### How do I implement a character controller?

See [Custom Character Controller](General/CharacterController.md) for a description.
