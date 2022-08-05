# TODO

For now just a place to start building out code snippets to do things with the Archer APIs. 

config.yml refernences common Archer REST endpoints.

Set sensitive details as environment variables: 
$ gp env ARCH_HOST=https://HOST
$ gp env ARCH_INSTANCE=ArcherInstance
$ gp env ARCH_DOMAIN=[usually not set]
$ gp env ARCH_USER=username
$ gp env ARCH_PWD=Secret111!
$ eval $(gp env -e)

Careful w/environment variables. If you share your environment, your buddies may have access to these details. 