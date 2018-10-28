# Realistic FPS Prefab

This integration provides components that work with the RFPSP asset. 

It provides the following items:

- Weapons
- Ammunition
- Food
- Drinks
- HealthPacks

These items all work with the setup of RFPSP. For example, if you pickup a weapon, it becomes available as a weapon you can use to shoot; using Food will reduce your player's hunger and boost its health.

## Getting Started

To setup your scene to use these items, you need to do the following:

1. Define the items you will need, including weapons and ammunition. This is done just like creating normal items through the *Main Editor*. More details on how to setup items are given below. 
2. Add the **_Managers** object to your scene, with all required managers. Also add the following components to the _Managers object:
   1. `FPSGame`
   2. `RFPSPItemFactory`
      ![](Assets\RFPSP_Managers.PNG)
3. Add the following components to your FPS Player object, and configure the collections you will need.
   1. `Player`
   2. `InventoryPlayer`
   3. `DropHandler` 
      ![](Assets\RFPSP_Player.PNG)
4. Add the Weapon component to each weapon under **FPS Weapons**, and link in the appropriate item definition file for that weapon. 
   ![](Assets\RFPSP_Weapons.PNG)
5. RFPSP only allows you to have one weapon of each type. To have this same behavior on a collection, you need to add the `WeaponRestrictionBehaviour` on your player (next to the creator script), and specify the collection name.
6. The `FPSGame` component provide a function that toggles pausing the game (which allows you to use the mouse to interact with the UI). Add an action to this method on show and hide for all `UIWindows` that need mouse interaction. You can also call this function for other purposes.
   ![](Assets\RFPSP_UIWindow.PNG)

## Tips for setting up items

- Use triggers to make it possible for items to get picked up. 
- Do not add any of these scripts to your items: `AmmoPickup`, `WeaponPickup`, `FoodPickup`, `DrinkPickup`, `HealthPickup`.
- Remember to add the type of Ammunition each weapon uses in the item definition.
  ![](Assets\Weapon.PNG)

## Running the Demo

1. Set the path to the Database in the *Main Editor* to `Assets/RFPSP Integration/FPS Databases`.
2. Open the *FPS Prefab Sandbox* scene in `Assets/RFPSP Integration/Demo`.
3. Run the game.