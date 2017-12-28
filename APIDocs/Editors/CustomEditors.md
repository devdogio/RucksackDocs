# Custom editors

The built-in editors can be extended or even overwritten to fit your need. This can be espcially useful when creating addons.

## Extending existing editor page

```csharp
// Make sure the priority is higher than the built-in item editor priority (default priority is 50).
[EditorPage("Items/Item", order: 10, priority: 100)]
public class ItemEditor : InventoryEditorCrudBase<UnityItemDefinition>
{
	public UnityEditor.Editor itemEditorInspector { get; set; }
	private UnityItemDefinitionDatabase[] _databases;
	
	public ItemEditor(EditorWindow window)
		: base("Item", "Items", "Items", window)
	{ }

	protected override bool MatchesSearch(UnityItemDefinition item, string searchQuery)
	{
		searchQuery = searchQuery ?? "";

		string search = searchQuery.ToLower();
		return (GetDisplayName(item).ToLower().Contains(search) ||
			item.description.ToLower().Contains(search) ||
			item.ID.ToString().Contains(search) ||
			GetTypeDisplayName(item).ToLower().Contains(search));
	}

	public override void EditItem(UnityItemDefinition item)
	{
		base.EditItem(item);
		if (item != null)
		{
			itemEditorInspector = UnityEditor.Editor.CreateEditor(item);
		}
	}

	protected override UnityItemDefinition CreateNewInstanceFromType(Type type)
	{
		var asset = (UnityItemDefinition)ScriptableObject.CreateInstance(type);
		asset.ResetID(System.Guid.NewGuid());

		return asset;
	}

	protected override IEnumerable<IDatabase<UnityItemDefinition>> GetProjectDatabases()
	{
		if (_databases == null)
		{
			_databases = Resources.FindObjectsOfTypeAll<UnityItemDefinitionDatabase>();
		}

		return _databases;
	}

	protected override void DrawDetailInternal(UnityItemDefinition item)
	{
		itemEditorInspector.OnInspectorGUI();
	}
}
```

## Adding an editor page

Pages can be created by adding a single ```[EditorPage("Items/TabName")]``` attribute to your class.

> Note that your class has to inherit from `EditorCrudBase<T>` or anything that inherits from it like `InventoryEditorCrudBase<T>`.

## Overwriting an editor page

In case you want to completely replace an existing editor page you can add a higher priority to your ```[EditorPage("Items/TabName", order: 20, priority: 100)]``` attribute.

> Note that this will completely overwrite any existing tabs.