# Equippable Character

A custom equippable character. When an item is equipped or un-equipped the `MyEquippableCharacter` can re-generate a set of stats for this particular character.

```csharp
public class MyEquippableCharacter : UnityEquippableCharacter
{
	public override Result<bool> Equip(IEquippableItemInstance item, int amount = 1)
	{
		var result = base.Equip(item, amount);
		if(result.error == null)
		{
			CalculateCharacterStats();
		}

		return result;
	}

	public override Result<bool> EquipAt(int index, IEquippableItemInstance item, int amount = 1)
	{
		var result = base.EquipAt(index, item, amount);
		if(result.error == null)
		{
			CalculateCharacterStats();
		}

		return result;
	}

	public override Result<bool> UnEquip(IEquippableItemInstance item, int amount = 1)
	{
		var result = base.UnEquip(item, amount);
		if(result.error == null)
		{
			CalculateCharacterStats();
		}

		return result;
	}

	public override Result<bool> UnEquipAt(int index, int amount = 1)
	{
		var result = base.UnEquipAt(index, amount);
		if(result.error == null)
		{
			CalculateCharacterStats();
		}

		return result;
	}

	protected void CalculateCharacterStats()
	{
		// Calculate the player's stats based on the equipment.
		foreach(var item in equippableCharacter.collection)
		{
			// Calculate item stats
		}
	}
}
```