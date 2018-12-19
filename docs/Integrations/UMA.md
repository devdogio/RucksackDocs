# UMA
This integration allows you to equip items using UMA's skinned mesh technology.

## Getting Started.

Using UMA with Rucksack requires these step steps below. This assumes that you already set up your scene to work with Rucksack, and imported the UMA package. 

1. Set up your scene to work with UMA by adding the UMA_DCS prefab. The prefab is in th folder `Assets/UMA/Getting Started`.
2. Add the UMAFactory component to your Managers object.
3. Set up your character by adding and configuring the Dynamic character avatar. You can remove meshes and meshrenderers since this will be taken care of by UMA.
4. Create the items that can be equipped to your character. Below is more information on how to do that.

## Item Types

This integration supports two types of item.

- **UMAEquippableItemDefinition:** This item works by modifying slots of the UMA character.
- **UMARecipeItemDefinition:** This item applies a UMA recipe to a character.

!!! warning "Note"
    It is not possible to use both types of items on a character at the same time. 

## Creating Items

You can create UMAEquipableItems and UMARecipeItem using the Main Editor.

![](Assets\UMA_Items.PNG)

## Configuring Items

Once the item is created, you can set up its properties. Most properties are the same as for other equipable items (although you need not in general set up the mounting point.)

Below is the setup for a UMAEquipableItems.

![](Assets\UMA_EditItem.PNG)

Below is a description of the UMA-specific properties. UMA Equip Slot and UMA Overlay Data Asset will be marked red if they are not set, since they are required fields.   

- **Uma Equip slot:** The slot where the item will be equipped. For example Male torso.
- **UMA Override color:** You can override the color of an UMA equipable.
- **UMA Overlay data asset:** The visual object that will be equipped onto the player. For example Jeans.
- **UMA Slot data asset:**  The visual slot where the item will be stored. 99% of the time this will have the same name as the UMA Overlay data asset.
- **UMA Replace slot:** When equipping certain things it can be useful to hide others. For example when equipping jeans you'll likely want to hide the legs underneath them.

And this is the setup for UMARecipeItm. The only field different from a general UnityEquippable item is the **Recipe**, that takes the recipe to apply to a character.

![](Assets\UMA_Recipe_Item.PNG)

