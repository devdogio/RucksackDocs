# Text Mesh Pro

## Demo

The integration comes with a replacement UI that shows how to use all the TextMesh Pro components with Rucksack. To change the UI of a demo scene to use the TextMesh Pro UI, open the demo scene, select the _Managers object in the hierarchy, and on the `DemoSceneLoader` component, change the *Scene Name* to `TMP_SurvivalUI_Partial`.

## Slots

Rucksack comes with three slot types. For each of these, there is a corresponding TextMesh Pro component  that you need to *add with* the existing slot UI.

| uGUI                         | TextMesh Pro                     |
| ---------------------------- | -------------------------------- |
| `ItemCollectionSlot`         | `TMP_ItemCollectionSlot`         |
| `EquipmentCollectionSlotUI`  | `TMP_EquipmentCollectionSlotUI`  |
| `ItemVendorCollectionSlotUI` | `TMP_ItemVendorCollectionSlotUI` |

## Currencies

There are two components that can be used *instead* of their uGUI counterparts.

| uGUI                 | TextMesh Pro             |
| -------------------- | ------------------------ |
| `CurrencyUI`         | `TMP_CurrencyUI`         |
| `CurrencyCollection` | `TMP_CurrencyCollection` |

## Tooltip

There are two components that can be used instead of their uGUI counterparts.

| uGUI                           | TextMesh Pro                       |
| ------------------------------ | ---------------------------------- |
| `ItemCollectionTooltipHandler` | `TMP_ItemCollectionTooltipHandler` |
| `ItemTooltipUI`                | `TMP_ItemTooltipUI`                |

## Extension Methods

Rucksack defines a class `UIMonobehaviour` that has some convenience methods for setting text fields only if they are linked (that is, not null). The TextMesh Pro integration defines extension methods for this class that allows you to conveniently set `TMP_Text` fields when they are linked in the inspector. 

``` csharp
public class MyUIComponent: UIMonoBehaviour
{
   TMP_Text title;
   
   public void SetTitle(string titleString)
   {
      this.Set(title, titleString); //this is necessary because we are extending 
      								//from the class for which an extension is defined.
   }
}
```

