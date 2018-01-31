# Vendors

Vendors allow a customer, such as the player, to buy and sell products from and to the vendor.

## Vendor types

Of course, vendors aren't restricted to just buying/selling items. Vendors can be re-used to sell any type of product, such as skills for skill points.

## Registries

Vendors have to be indexed in vendor registries so it can be looked up at a later time.

```csharp
using System;
using Devdog.InventoryPlus.Vendors;

// Registering a vendor
VendorRegistry.itemVendors.Register(vendorGuid, vendor);

// Un-Registering a vendor
VendorRegistry.itemVendors.UnRegister(vendorGuid);

// Getting a vendor from the registry
var vendor = VendorRegistry.itemVendors.Get(vendorGuid);
```

## API

### Products

The item vendor keeps track of products. These products contain the actual item to purchase as well as its buy and sell price. The reason a product wrapper is used is to give the developer extra freedom when buying and selling to customers.
For example: You may want to give certain players a discount, while making others pay more.

```csharp
using System;
using Devdog.General;
using Devdog.InventoryPlus.Items;
using Devdog.InventoryPlus.Collections;
using UnityEngine;

// Creating a product is simple.
private static VendorProduct<IItemInstance> ToProduct(CollectionItemInstance item)
{
	return new VendorProduct<IItemInstance>(item, item.itemDefinition.buyPrice, item.itemDefinition.sellPrice);
}
```

### Customers

A `Customer<T>` is a simple wrapper class that defines a customer that wisher to buy or sell something to a vendor. Any object can be a customer, but as an example we'll use the regular player.

```csharp
using System;
using Devdog.General;
using Devdog.InventoryPlus.Collections;
using UnityEngine;

// Create the vendor's collections and the vendor.
var vendorCollection = new Collection<IVendorProduct<IItemInstance>>(10);
var vendorCurrencies = new CurrencyCollection(); // You can swap this for InfiniteCurrencyCollection if you want to ignore vendor currencies.
var vendor = new Vendor<IItemInstance>(_vendorCollection, _vendorCurrencies);

// Create the customer wrapper object for our player.
var customer = new Customer<IItemInstance>(Guid.NewGuid(), player, player.itemCollectionGroup, player.currencyCollectionGroup);

var result = vendor.BuyFromVendor(_customer, _item1, 5);
if(result.error == null)
{
	// Yay, the customer bought the item.
}
else
{
	// Whoops, the item could not be bought. Check result.error for more details.
}
```