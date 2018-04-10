# UIWindow

Windows represent a single window pane in your UI. A window can be shows and hidden and contains events to synchronize it with other UI elements.

UI windows get disabled when hidden to reduce resource usage and increases drawing performance.

## Using a UIWindow

```csharp
using UnityEngine;
using Devdog.General.UI;

public class MyClass : MonoBehaviour
{
	// Assign in Unity inspector.
	public UIWindow myWindow;

	private void MyMethod()
	{
		myWindow.Show();
	}

	private void MyHideMethod()
	{
		myWindow.Hide();
	}

	private void MyToggleMethod()
	{
		// Show if hidden, hide if shown.
		myWindow.Toggle();
	}
}
```

## Input handlers

Input handlers are responsible for showing / hiding the window when the user performs an action or input. The `IUIWindowInputHandler` can be implemented to create your own UI window input handler.

```csharp
using UnityEngine;
using Devdog.General.UI;

[RequireComponent(typeof(UIWindow))]
public sealed class MyUIWindowInputHandler : MonoBehaviour, IUIWindowInputHandler
{
	public KeyCode keyCode = KeyCode.None;

	private UIWindow _window;
	private void Awake()
	{
		_window = GetComponent<UIWindow>();
	}

	private void Update()
	{
		if (Input.GetKeyDown(keyCode))
		{
			_window.Toggle();
		}
	}
}
```

## Visuals

The `UIWindowVisuals` component can handle the visuals for a window, such as show and hide animations and audio.

## Window events

`UIWindow` events can be used to synchronize UI elements, enable / disable controllers, etc.

!!! danger
	Don't forget to unsubscribe your events when your object gets destroyed or disabled.

```csharp
using UnityEngine;
using Devdog.General.UI;

public class MyEventListenerClass : MonoBehaviour
{
	// Assign in Unity inspector.
	public UIWindow myWindow;

	private void MyMethod()
	{
		myWindow.OnShow += OnShow;
		myWindow.OnHide += OnHide;
	}

	private void OnDestroy()
	{
		// Remove / cleanup event listeners on destroy.
		myWindow.OnShow -= OnShow;
		myWindow.OnHide -= OnHide;
	}

	private void OnShow()
	{
		// Called when the window is hidden.
	}

	private void OnHide()
	{
		// Called when the window is shown.
	}
}
```