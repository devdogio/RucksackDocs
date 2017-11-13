# Layout collections

Layout collections allow items to be stored that take up more than 1x1 slots. Items could for example take up 3 horizontal slots and 2 vertical slots, totalling at 6 occupied slots. 

Layout collection items have to implement the `IShapeOwner2D` interface to pass 'shape' of the item through to the collection. You can additionally implement your own `IShape` interface to define the shape of the item.

> Layout collections are slower than regular collections because it needs to validate if the item can be fitted with it's larger size. Therefore, if you don't use items with different sizes use the regular [Collection](Collection.md) instead.

> See [Collection](Collection.md) for additional details.

## Example of custom collection

```csharp
public sealed class MyLayoutCollection<TElementType> : LayoutCollection<TElementType>
    where TElementType : IEquatable<TElementType>, IShapeOwner2D, IStackable, IIdentifiable, ICloneable<TElementType>
    {
        public MyLayoutCollection(int slotCount, int columnCount)
            : base(slotCount)
        {

        }
    }
```