# Trigger Selector

A trigger selector is responsible for selecting a single trigger based on some criteria. For example, when the player presses a button to use a trigger the trigger selector is responsible for picking the best trigger within the player's range.

> See `Assets/Create/Devdog` to create a trigger selector scriptable object.

![](Assets/TriggerSelector.png)

## Third person games

When building a third person game your character can generally use trigger (object) within the player's range. This is generally based on the player's location and viewing direction (favoring items in front of the player). For this exact use case there's a built-in trigger selector called the `RangeBestTriggerSelector`.

## First person games

When building a first person game you generally want to select the trigger your player is directly looking at. This can be done through the `RaycastBestTriggerSelector`.

## Custom trigger selector

You can also implement your own custom trigger selector by inheriting from `BestTriggerSelectorBase`. The trigger selector will receive the character in question and all of it's in range triggers.