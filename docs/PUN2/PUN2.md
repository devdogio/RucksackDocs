# PUN2 networking

PUN2 multiplayer support is built-in, and can be used with minimal setup. First you have to download and set up [Photon Unity Network (PUN v2)](https://doc.photonengine.com/en-us/pun/v2/getting-started/initial-setup).


!!! warning
	In order to use PUN2 you'll have to download the package from the [devdog.io website](https://devdog.io/unity-assets/rucksack-multiplayer-inventory-system/community-bonus/). Optionally, a mirror package is also available.

## Server authority

The server is authoritative, meaning that the server decides everything for the player. The player can request certain actions from the server (such as using an item), however, the server will always validate and decide if the action is permitted. This prevents cheating, but does add a roundtrip to the server for each networked action.

!!! Warning "Warnings: "
	1. Current implementation chooses the first player in the room as the master server. If the master server leavs or drops out clients can't send and validate their requests.
	2. Messages are not buffered, new clients connected mid-game will not see old players' equipped items.

## PUN2ItemFactory

The `PUN2ItemFactory` adds bindings to the item factory for PUN2 specific item types. This makes sure that all items created through `ItemFactory` are PUN2 compatible. You can add this component to any object in your scene. For consistency attaching it to a _Managers or _PUN2 object is recommended.

## PUN2ActionsBridge

The PUN2ActionsBridge is the enter and exit point for all player actions. This component must be added to the player.

## PUN2InitPlayer

The `PUN2InitPlayer` is a simple component that registers your player locally whenever the server gives permission (OnStartAuthority). Attach this component to your player and disable `init on start` on your default Player component.

## Permission system

Collections and objects in the world can have permissions assigned to them in the `PUN2PermissionsRegistry`. By default the user has no permission to any object or collection; All permission have to be set explicitly.

```csharp
using Devdog.Rucksack;

var player = <ASSIGN YOUR PLAYER>;
var bridge = player.GetComponent<PUN2ActionsBridge>();

// Create a server collection. This should only be created on the server side; The client has to receive a client collection with the same ID and name.
var collection = new PUN2ServerCollection<IItemInstance>(bridge.photonView, 10);
collection.collectionName = "Inventory";
collection.ID = System.Guid.NewGuid();

PUN2PermissionsRegistry.collections.SetPermission(collection, bridge.photonView, ReadWritePermission.ReadWrite);
```

For simplicity there's built-in methods on the PUN2ActionsBridge that allow you to create collections easily on both the server and client with a single call.

```csharp
using Devdog.Rucksack;

var player = <ASSIGN PLAYER>;
var bridge = player.GetComponent<PUN2ActionsBridge>();

var collectionGuid = System.Guid.NewGuid();

// This will create a collection of 10 slots on both the client and server.
// The server will create a PUN2ServerCollection<T> while the client will create a PUN2ClientCollection<T>.
// The PUN2ServerCollection<T> will auto. start replicating it's changes to the client collection.
bridge.Server_AddCollectionToServerAndClient(
	/*collectionName: */ "Inventory",
	/*collectionGuid: */ collectionGuid,
	/*slotCount: */ 10
);

// Don't forget to set the permission for this player.
// This will set the permission on the server and notify the client it received read permission on this collection.
// NOTE that the collection has to exist before setting permission.
bridge.Server_SetCollectionPermissionOnServerAndClient(
	/*collectionGuid: */ collectionGuid,
	/*permission: */ ReadWritePermission.Read
);
```

## Input validation

The `PUN2ActionsBridge` uses replicates and validators to sync data between server and client. To make sure the client doesn't send some information that could crash the server or allow the player to cheat all data has to be validated. This is done by the validators.

The validators make sure the GUID data is a consistent byte length, that indices are not out of range and that the player has permission to even perform the action in the first place.

## Registries

Registries are used to index certain types. These are useful for the server to quickly find types it needs at an O(1) lookup speed. It's important to register your run-time types, otherwise the server won't be able to properly replicate actions.

## Run-time items

Items can be created / generated at run-time. Item instances can contain run-time information, while the item definitions are persistent objects.

### How run-time items are created

Item instances have to be registered on the client. This can be done through the `PUN2ActionsBridge`. Note that items are also auto. registered on the client through collection replication.

!!! note
	Registering items on clients manually is only needed if you want to pre-load it, the item is not in a collection, or need the item before it's replciated through a collection.

```csharp
using Devdog.Rucksack;

var player = <ASSIGN PLAYER>;
var bridge = player.GetComponent<PUN2ActionsBridge>();

// Tell this client to register the item instance on their local client.
bridge.Server_TellClientToRegisterItemInstance(itemInstance);
```
