# Databases

Databases can be used to retrieve data from a specific source. This database can load data on your local computer, from the cloud, etc. The database has sync and async methods to retrieve and set data.

## Implementing a custom database

Below you'll find a Mongo database example.

> Note that you most likely don't want to create a direct connection to your database for security reasons. This a demo only.

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Linq;
using Devdog.InventoryPlus.Database;

// TODO: Add your own namespace.

public class MongoDatabase<T> : IDatabase<T>
	where T : class, IIdentifiable
{
	public MongoClient client { get; }
	public IMongoDatabase database { get; }
	public IMongoCollection<T> collection { get; }
	
	private readonly ICache<T> _cache;
	private readonly ILogger _logger;

	public MongoDatabase(string connectionString, string databaseName, string collectionName, ILogger logger = null, ICache<T> cache = null)
	{
		client = new MongoClient(connectionString);
		database = client.GetDatabase(databaseName);
		collection = database.GetCollection<T>(collectionName);

		_logger = logger ?? new Logger($"[{GetType().Name}] ");
		_cache = cache ?? new NullCache<T>(_logger);
	}
	
	public void Preload(IEnumerable<IIdentifiable> ids)
	{
		_logger.LogVerbose("Preloading set of items.");
		
		// TODO: Check _cache to see which are already loaded.
		throw new NotImplementedException();
	}
	
	public Result<T> Get(IIdentifiable identifier)
	{
		if (_cache.Contains(identifier))
		{
			_logger.LogVerbose($"Retrieved {identifier} from cache");
			return new Result<T>(_cache.Get(identifier));
		}

		_logger.LogVerbose($"Fetching {identifier} from database");
		var item = collection.Find(new BsonDocument("_id", identifier.ID)).FirstOrDefault();
		if (item == null)
		{
			return new Result<T>(null, Errors.DatabaseItemNotFound);
		}
		
		_cache.Set(identifier, item);
		return new Result<T>(item);
	}

	public Result<T> Get(Expression<Func<T, bool>> selector)
	{
		// TODO: Add caching...
		
		var result = collection.AsQueryable<T>().Where(selector).FirstOrDefault();
		return result ?? new Result<T>(null, Errors.DatabaseItemNotFound);
	}

	public Task<Result<T>> GetAsync(IIdentifiable identifier, CancellationToken cancellationToken = default(CancellationToken))
	{
		return Task.Factory.StartNew(() => Get(identifier), cancellationToken);
	}

	public Task<Result<T>> GetAsync(Expression<Func<T, bool>> selector, CancellationToken cancellationToken = new CancellationToken())
	{
		return Task.Factory.StartNew(() => Get(selector), cancellationToken);
	}

	public Result<IEnumerable<T>> GetAll()
	{
		throw new NotImplementedException();
	}

	public Task<Result<IEnumerable<T>>> GetAllAsync(CancellationToken cancellationToken = default(CancellationToken))
	{
		return Task.Factory.StartNew(GetAll, cancellationToken);
	}

	public Result<bool> Set(IIdentifiable identifier, T item)
	{
		_logger.LogVerbose($"Upserting {identifier} into database");
		collection.FindOneAndReplace(new BsonDocument("_id", identifier.ID), item, new FindOneAndReplaceOptions<T>(){ IsUpsert = true });
		_cache.Set(identifier, item);
		
		return new Result<bool>(true);
	}

	public Task<Result<bool>> SetAsync(IIdentifiable identifier, T item, CancellationToken cancellationToken = default(CancellationToken))
	{
		return Task.Factory.StartNew(() => Set(identifier, item), cancellationToken);
	}

	public void Dispose()
	{ }
}
```