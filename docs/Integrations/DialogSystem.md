# Dialog System

This integration provides components that work with the Dialog System asset.

## Getting Started

1. Set up your scene to work with Dialog System by adding the Dialog Manager prefab to your scene. The prefab is in the folder `Assets\Plugins\Pixel Crushers\Dialogue System\Prefabs.
2. Add the DialogSystemFactory component to your Managers object.

## Dialog System Quest Items 	
Quest items adds a quest to the player when used. 

![](Assets\DialogSystem_QuestItem.PNG)

- **Dialog System Quest ID:** the ID of the quest added to the player when the item is used.
- **Can Use After Quest Already Completed:** Set this to false if you only want the player to have the quest once.
- **Custom Conversation:** This is the conversation started when the item is used.	

## Conversation Trigger

This component links a Rucksack Trigger with a line of dialog spoken. 

1. Add a custom field to the Dailog Entry template called "LineTag", which should take a Text value.

   ![](Assets\DialogSystem_LineTag.PNG)

2. For the Dialog Entry you wish to trigger, set the LineTag to a suitable value.

   ![](Assets\DialogSystem_LineTag_Entry.PNG)

3. Add the ConversationTrigger on the same object as the Trigger, and set the lineTag field to the same value you used in the last step.

   ![](Assets\DialogSystem_ConversationTrigger.PNG)

In the demo scene, when the player answers "Yes" to the vendor, the vendor trigger is used, and so the Vendor window is displayed. This is implemented using the mechanism above.

## LUA Methods

There are a few methods registered that you can access from LUA. To use these, follow these steps:

1. Add a DialogSystemPlayer component to your player (next to InventoryPlayer).

2. Add a Unity Database Manager component to your _Managers object, and connect your items, currencies and equipment types databases.

   ![](Assets\DialogSystem_Databases.PNG)

The following methods are available:

- `CanAddCurrency`
- `AddCurrency`
- `CanRemoveCurrency`
- `RemoveCurrency`
- `GetCurrency`
- `CanAddItem`
- `AddItem`
- `CanRemoveItem`
- `RemoveItem`
- `GetItemCount`
- `EquipItem`
- `UnEquipItem`

There are also special methods available for vendors. To use these, add the DialogSystemVendor component to your vendor. The following methods are available:

- `CanBuyFromVendor`
- `CanSellToVendor`
- `SellToVendor`
- `BuyFromVendor`

