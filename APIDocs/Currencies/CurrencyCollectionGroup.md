# Currency Collection Group

Currency collection groups, like regular [collection groups](../Collections/CollectionGroup.md), group together collections. These groups are easier to manage than a traditional array of currency collections. The collection group is also responsible for priority handling and filters on collections.

```csharp
using System;
using Devdog.InventoryPlus.Collections;

var col1 = new CurrencyCollection();
var col2 = new CurrencyCollection();
var group = new CurrencyCollectionGroup<ICurrency>(new CurrencyCollectionGroup<ICurrency>.Slot[]
{
	new CurrencyCollectionGroup<ICurrency>.Slot(col1, new CurrencyCollectionPriority<ICurrency>()), 
	new CurrencyCollectionGroup<ICurrency>.Slot(col2, new CurrencyCollectionPriority<ICurrency>(60, 60, 60)), // Set a higher priority
});


var added = group.Add(gold, 100d);
// Assert.AreEqual(0d, col1.GetAmount(gold));
// Assert.AreEqual(100d, col2.GetAmount(gold));
```