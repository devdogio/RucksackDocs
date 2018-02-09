# Currencies

Currencies represent a simple object that contains an amount of 'something'. Where something can be gold, guild credits, and so forth. Currencies can be used to purchase items from [vendors](../Vendors/Vendors.md).

## Custom currency

You can use the built-in `UnityCurrency` type, or define your own for more control.

```csharp
using System;
using Devdog.InventoryPlus.Currencies;

// Example of a simple custom currency implementation. Note that you can inherit from ScriptableObject to let Unity serialize the data for you.
public class MyCurrency : IUnityCurrency, ICloneable
{
	public Guid ID { get; private set; }

	private LocalizedString _name = new LocalizedString();
	public new string name
	{
		get { return _name.message; }
	}

	private LocalizedString _tokenName = new LocalizedString();
	public string tokenName
	{
		get { return _tokenName.message; }
	}

	public Sprite icon { get; private set; }
	public int decimals { get; private set; }
	public double maxAmount { get; private set; }

	public ConversionTable<ICurrency, double> conversionTable { get; set; }

	public MyCurrency()
	{
		conversionTable = new ConversionTable<ICurrency, double>();
	}
	
	public bool Equals(ICurrency other)
	{
		return ID.Equals(other?.ID);
	}

	public void ResetID(System.Guid id)
	{
		_guid = new SerializedGuid()
		{
			guid = id
		};
	}

	public object Clone()
	{
		var clone = (MyCurrency) MemberwiseClone();
		clone.ResetID(System.Guid.NewGuid());
		return clone;
	}
	
	public override string ToString()
	{
		return name;
	}
}
```