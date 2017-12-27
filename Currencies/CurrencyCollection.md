# Currency Collection

Currency collection can store a set of currencies and there amounts. Currency collections will also fire events when their contents change.

```csharp
using System;
using Devdog.InventoryPlus.Currencies;

var currencies = new CurrencyCollection();
var gold = new Currency(Guid.NewGuid(), "Gold", "GOLD", 2, 999f);
var silver = new Currency(Guid.NewGuid(), "Silver", "SILVER", 2, 999f);
var copper = new Currency(Guid.NewGuid(), "Copper", "COPPER", 2, 999f);

// Add 2 gold do this collection
var addResult = currencies.Add(gold, 2);

// Remove 10 gold
var removeResult = currencies.Remove(gold, 10f);
if(removeResult.error == null)
{
	// 10 Gold got removed.
}
else{
	// Couldn't remove 10 gold. See removeResult.error for details.
}

// Set gold to 999
var setResult = currencies.Set(gold, 999f);

// Clear the collection and remove all currencies stored in it.
currencies.Clear();
```

## Events

```csharp
currencies.OnCurrencyChanged += (sender, result) => {
	// result.currency changed
	// result.amountBefore
	// result.amountAfter
};
```