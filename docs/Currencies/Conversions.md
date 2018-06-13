# Currency conversions

Currencies can be converted from one currency type to another. This can be useful for converting 1 gold to 100 silver, gems to gold, etc.

## Conversion table

The conversion table defines how currencies can be converted between each other.

```csharp
using System;
using System.Collections.Generic;
using Devdog.InventoryPlus.Currencies;

// Define currencies
var gold = new Currency(Guid.NewGuid(), "Gold", "GOLD", 2, double.MaxValue);
var silver = new Currency(Guid.NewGuid(), "Silver", "SILVER", 5, double.MaxValue);
var copper = new Currency(Guid.NewGuid(), "Copper", "COPPER", 5, double.MaxValue);
var diamonds = new Currency(Guid.NewGuid(), "Diamonds", "DIAMONDS", 0, double.MaxValue);
var guildCredits = new Currency(Guid.NewGuid(), "Guild Credits", "GUILD", 0, double.MaxValue);

// Define conversions between currencies
gold.conversionTable = new ConversionTable<ICurrency, double>(new Dictionary<ICurrency, ConversionTable<ICurrency, double>.Row>()
{
	{diamonds, new ConversionTable<ICurrency, double>.Row(0.01d)},
	{silver, new ConversionTable<ICurrency, double>.Row(100d)},
});

silver.conversionTable = new ConversionTable<ICurrency, double>(new Dictionary<ICurrency, ConversionTable<ICurrency, double>.Row>()
{
	{gold, new ConversionTable<ICurrency, double>.Row(0.01d)},
	{copper, new ConversionTable<ICurrency, double>.Row(100d)},
});

copper.conversionTable = new ConversionTable<ICurrency, double>(new Dictionary<ICurrency, ConversionTable<ICurrency, double>.Row>()
{
	{silver, new ConversionTable<ICurrency, double>.Row(0.01d)},
	{guildCredits, new ConversionTable<ICurrency, double>.Row(2d)},
});

// Create a converter object
var converter = new CurrencyDoubleConverter();
// Convert 3 gold into silver.
var result = converter.Convert(gold, 3, silver);

// Get all possible conversions from gold into other currencies.
var conversionsTable = converter.GetAllConversions(gold);
// Assert.AreEqual(5, conversionsTable.Count);
// Assert.AreEqual(0.01d, conversionsTable[diamonds].conversionRate);
// Assert.AreEqual(1.0d, conversionsTable[gold].conversionRate);
// Assert.AreEqual(100d, conversionsTable[silver].conversionRate);
// Assert.AreEqual(10000d, conversionsTable[copper].conversionRate);
// Assert.AreEqual(20000d, conversionsTable[guildCredits].conversionRate);
```