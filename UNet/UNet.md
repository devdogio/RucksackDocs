# UNet networking

UNet multiplayer support is built-in, and can be used with minimal setup.

## Server authority

The server is authoritative, meaning that the server decides everything for the player. The player can request certain actions from the server (such as using an item), however, the server will always validate and decide if the action is permitted. This prevents cheating, but does add a roundtrip to the server for each networked action.

## UNetActionsBridge

The UNetActionsBridge is the enter and exit point for all player actions.

### Naming convention

- Server_* Methods can only be invoked on the server.
- Client_* Methods can only be invoked on the clients.
- TargetRpc_* Methods can only be invoked on the server and relay their message to the client.
- Cmd_* Methods can only be invoked on the client and relay their message to the server.

!!! danger
	The client requires authority over the object to call Cmd_* methods. (see NetworkIdentity).

## Permission system

Collections and objects in the world can have permissions assigned to them in the `UNetPermissionsRegistry`. By default the user has no permission to any object or collection; All permission have to be set explicitly.

```csharp
var player = <ASSIGN YOUR PLAYER>;

// Create a server collection. This should only be created on the server side; The client has to receive a client collection with the same ID and name.
var collection = new UNetServerCollection<IItemInstance>(player.identity, 10);
collection.collectionName = "Inventory";
collection.ID = System.Guid.NewGuid();

UNetPermissionsRegistry.collections.SetPermission(collection, player.identity, ReadWritePermission.ReadWrite);
```

For simplicity there's built-in methods on the UNetActionsBridge that allow you to create collections easily on both the server and client with a single call.

```csharp
using Devdog.InventoryPlus;

var player = <ASSIGN PLAYER>;
var bridge = player.GetComponent<UNetActionsBridge>();

var collectionGuid = System.Guid.NewGuid();

// This will create a collection of 10 slots on both the client and server.
// The server will create a UNetServerCollection<T> while the client will create a UNetClientCollection<T>.
// The UNetServerCollection<T> will auto. start replicating it's changes to the client collection.
bridge.Server_AddCollectionToServerAndClient(new AddCollectionMessage(){
	owner = player.identity,
	collectionName = "Inventory",
	collectionGuid = collectionGuid,
	slotCount = 10
});

// Don't forget to set the permission for this player.
// This will set the permission on the server and notify the client it received read permission on this collection.
// NOTE that the collection has to exist before setting permission.
bridge.Server_SetCollectionPermissionOnServerAndClient(new SetCollectionPermissionMessage(){
	collectionGuid = collectionGuid,
	permission = ReadWritePermission.Read
});
```

## Input validation

The `UNetActionsBridge` uses replicates and validators to sync data between server and client. To make sure the client doesn't send some information that could crash the server or allow the player to cheat all data has to be validated. This is done by the validators.

The validators make sure the GUID data is a consistent byte length, that indices are not out of range and that the player has permission to even perform the action in the first place.

## Registries

Registries are used to index certain types. These are useful for the server to quickly find types it needs at an O(1) lookup speed. It's important to register your run-time types, otherwise the server won't be able to properly replicate actions.

## Run-time items

Items can be created / generated at run-time. Item instances can contain run-time information, while the item definitions are persistent objects.

### How run-time items are created

Item instances have to be registered on the client. This can be done through the `UNetActionsBridge`. Note that items are also auto. registered on the client through collection replication.

!!! note
	Registering items on clients manually is only needed if you want to pre-load it, the item is not in a collection, or need the item before it's replciated through a collection.

```csharp
using Devdog.InventoryPlus;

var player = <ASSIGN PLAYER>;
var bridge = player.GetComponent<UNetActionsBridge>();

// Tell this client to register the item instance on their local client.
bridge.Server_TellClientToRegisterItemInstance(itemInstance);
```

### Network serialization

TODO