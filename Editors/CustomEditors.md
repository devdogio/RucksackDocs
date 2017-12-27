# Custom editors

The built-in editors can be extended or even overwritten to fit your need. This can be espcially useful when creating addons.

## Writing an editor page

```csharp

```


## Extending existing editor page

```csharp
// Make sure the priority is higher than the built-in item editor priority (default priority is 50).
[EditorPage("Items/Item", order: 10, priority: 100)]
public class CustomItemEditor : ItemEditor
{
	public override void Draw()
	{
		base.Draw();

		// Draw some extra elements.
	}
}
```


## Adding an editor page

Pages can be created by adding a single ```[EditorPage("Items/TabName")]``` attribute to your class.

## Overwriting an editor page

In case you want to completely replace an existing editor page you can add a higher priority to your ```[EditorPage("Items/TabName", 100)]``` attribute.

> Note that this will completely overwrite any existing tabs.