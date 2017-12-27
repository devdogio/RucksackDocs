# Character Equipment


## Equipment editor

The ![Equipment Editor](../Editors/Editors.md) can be used to define equipment types. These types identify where an item can be equipped on a character.

## Mounpoints

A mountpoint is a location where items can be equipped onto. These mountpoints can be defined as Unity MonoBehaviours, but can also be kept as just plain data objects.

The `IMountPoint<T>` interface can be implemented to define your own mountpoints.

The mountpoints are responsible for visualizing the items onto the characters. By default the following mount points are included.

- `ClothMeshMountPoint` (For equipping cloth meshes, ex: cape)
- `SkinnedMeshMountPoint` (For equipping skinned / animated items, ex: pants)
- `StaticMeshMountPoint`(For equipping static meshes, ex: sword)

## UnityEquippableCharacter

The `UnityEquippableCharacter` is the built-in equippable character class for equippable characters. This class can be used 9/10 times. If you like more customization you can implement the `IEquippableCharacter<T>` interface.

## IEquippableCharacter<T>

The `IEquippableCharacter<T>` interface can be used to define an equippable character. This can be your main player, an NPC, or even a spaceship. The built-in `UnityEquippableCharacter` can be used in most cases.
