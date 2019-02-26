from flask_caching import Cache
from redis import Redis
from scoring_engine.config import config


cache = Cache(config={
    'CACHE_TYPE': config.cache_type,
    'CACHE_REDIS_HOST': config.redis_host,
    'CACHE_REDIS_PORT': config.redis_port,
    'CACHE_REDIS_PASSWORD': config.redis_password,
})

redis_cache = Redis(
    host=config.redis_host, 
    port=config.redis_port, 
    password=config.redis_password
)

redis_cache.set('teams_count', -1);
redis_cache.set('round_number', -1);
