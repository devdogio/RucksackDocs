# Collection UI

A collection UI is a UI representation of a collection.

## CollectionUIBase<T>

The `CollectionUIBase<T>` class is a useful helper class that you can use to implement a custom collection UI. You're not required to use this base class.

## Slots

Slots represent a single item and all of it's information in the collection. See [Slot UI](CollectionSlotUI.md) for more details.

## Custom collection UI

### UIQueuedMonoBehaviour<T>

The `UIQueuedMonoBehaviour<T>` is a base class that queue's up changes and repaints everything at once when the UI becomes visible. If the UI is already visible at the time of the change a repaint will occur instantly.

Elements that are affected multiple times will only be queued once, and thus, will only repaint once.

```csharp
public sealed class ItemCollectionUI : CollectionUIBase<IItemInstance>
{
	protected override CollectionSlotUIBase CreateUIElement(int index)
	{
		var inst = (CollectionSlotUIBase<IItemInstance>)base.CreateUIElement(index);
		
		// Do something to newly created UI slot instance.

		return inst;
	}

	protected override void Repaint(int slot)
	{
		base.Repaint(slot);

		// Do something else.
		// Note that you can also handle the repaint in a custom slot class.
	}
}
```