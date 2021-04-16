import pung


container = punq.Container()

container.register("DI_CONFIG", instance=get_config())
config = container.resolve("DI_CONFIG")

instance_client = Manager(
    host=config['db']['host'],
    port=config['db']['port'],

)
container.register("DI_DATABASE_CLIENT", Manager, host=config['db']['host'], port=config['db']['port'])
