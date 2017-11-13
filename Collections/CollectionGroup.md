# Collection Group

A [Collection](Collection.md) group allows you to bundle multiple collections together, and run methods on all of them at once. So, why is this useful?

Imagine your player has 3 inventories and you wish to add an item to the player's inventory. Instead of finding in what collection you want to add the item, simply use a `CollectionGroup`.

## Priorities

Each entry in a collection group can have a priority. Items will be added to the collections in order of priority.

> Here we're giving col1 a priority of 60. This will place new items in col1. Once col1 is full, the items will be placed in col0.

```csharp
	var col0 = new Collection<IItemInstance>(5) {name = "Collection0"};
	var col1 = new Collection<IItemInstance>(5) {name = "Collection1"};
	
	var group = new CollectionGroup<IItemInstance>(new []
	{
		new CollectionGroup<IItemInstance>.Slot(col0), 
		new CollectionGroup<IItemInstance>.Slot(col1, new CollectionPriority<IItemInstance>(60, 60, 60)), 
	});
```