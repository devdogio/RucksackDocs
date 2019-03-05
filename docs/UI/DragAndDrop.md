# Drag and Drop

Drag and drop is handled through the `DragAndDropUtility`. Drag actions can be invoked by input handlers on slots or other UI elements.

You can drag any UI element in the Unity UI.

## Drag and drop utility

Manually using the `DragAndDropUtility`.

```csharp
// Start a drag action
var beginResult = DragAndDropUtility.BeginDrag(new DragAndDropUtility.Model(GetComponent<RectTransform>(), null), eventData);

// Update the drag action
DragAndDropUtility.Drag(eventData);

// End the drag action and get the result of the placement.
var endResult = DragAndDropUtility.EndDrag(eventData);
```

## Events

Drag and drop events can be useful to adjust your UI when the user starts or completes a drag operation.

```csharp
DragAndDropUtility.OnBeginDrag += (model, data) =>
{
	// Drag operation started. This is called only once per drag operation.
};

DragAndDropUtility.OnDrag += (model, data) => 
{
	// Drag operation is ongoing. Called each frame.
};

DragAndDropUtility.OnEndDrag += (model, data) =>
{
	// Drag operation ended. This is called only once per drag operation.
};
```

## IDropArea

An IDropArea is a area on which the dragged object can be dropped. The drop area does not have to accept the dragged item, for example, the player might drag an item onto the vendor window to sell it, but the vendor can decline the drag and drop action.

A Collection slot drag handler is an example of an `IDropArea`.

```csharp
using Devdog.General;
using Devdog.Rucksack.UI;

public sealed class MyCustomDropArea : MonoBehaviour, IDropArea
{
	public Result<bool> CanDropDraggingItem(DragAndDropUtility.Model model, PointerEventData eventData)
	{
		// Only accept items on this drop area.
		var item = model.dataObject as IItemInstance;
		if (item == null)
		{
			return new Result<bool>(false, Errors.UIDragFailedIncompatibleDragObject);
		}

		return true;
	}

	public void DropDraggingItem(DragAndDropUtility.Model model, PointerEventData eventData)
	{
		var beginSlot = model.source.GetComponent<CollectionSlotUIBase>();
		var fromCol = beginSlot.collection;
		var fromIndex = beginSlot.collectionIndex;

		// Do something with dragged item here...
	}
}
```

## IDropAreaSourceOverwriter

The `IDropAreaSourceOverwriter` allows you to overwrite the callback receiver for a drag event. By default the object on which you complete the drag (`IDropArea`) receives the `CanDropDraggingItem` and `DropDraggingItem` calls. However, when you implement the `IDropAreaSourceOverwriter` on the drag source (the object that you started dragging) it will receive the `CanDropDraggingItemOnTarget` and `DropDraggingItemOnTarget` calls instead.

This is useful if you want the source to clean up resources when the item is dragged out of it's drop area.

```csharp
using Devdog.General;
using Devdog.Rucksack.UI;

public sealed class EquipmentCollectionSlotDragHandler : MonoBehaviour, IDropAreaSourceOverwriter
{
	public Result<bool> CanDropDraggingItemOnTarget(DragAndDropUtility.Model model, List<IDropArea> targetDropArea, PointerEventData eventData)
	{
		foreach (var dropArea in targetDropArea)
            {                
                
                if (dropArea.CanDropDraggingItem(model, eventData).result)
                {
                    return true;
                }
            }

            return new Result<bool>(false, Errors.UIDragFailedIncompatibleDragObject);
	}

	public void DropDraggingItemOnTarget(DragAndDropUtility.Model model, List<IDropArea> targetDropArea, PointerEventData eventData)
	{
		foreach (var dropArea in targetDropArea)
            {
	    	var c = dropArea as UnityEngine.Component;
		if(c == null)
		{
		    continue;
		}
		
                var targetSlot = c.GetComponent<CollectionSlotUIBase>() as CollectionSlotUIBase<IItemInstance>;
                
                if (targetSlot != null)
                {
                    var itemInTargetSlot = targetSlot.current;	//eg. Grab Item from target slot
                    //Do something with with this item
		    
		    dropArea.DropDraggingItem(model, eventData);	//<<< Start drop action where "model" is dragging item
                }

                eventData.Use();
                break;
            }
	}
}
```

## IDragAndDropHandler

If you want absolute control over the drag and drop behavior you can implement the `Devdog.InventoryPlus.UI.IDragAndDropHandler` interface and set the drag handler on the `DragAndDropUtility`.

!!! note
	This is a global drag handler used for all drag and drop behavior. If you want to implement custom drag and drop behavior for some UI element create a component + IDropArea instead.

```csharp
using Devdog.Rucksack.UI;

public class MyDragAndDropHandler : IDragAndDropHandler
{
	// ... Implement interface here ...
}
```

And finally, set your drag handler in the `DragAndDropUtility`.

```csharp
using Devdog.Rucksack.UI;

// Call somewhere at game init.
DragAndDropUtility.handler = new MyDragAndDropHandler();
```
