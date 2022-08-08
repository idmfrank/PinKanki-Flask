# TODO

For now just a place to start building out code snippets to do things with the Archer APIs. 

config.yml refernences common Archer REST endpoints.

Set sensitive details as environment variables:<br>
`
$ gp env ARCH_HOST=https://HOST<br>
$ gp env ARCH_INSTANCE=ArcherInstance<br>
$ gp env ARCH_DOMAIN=[usually not set]<br>
$ gp env ARCH_USER=username<br>
$ gp env ARCH_PWD=Secret111!<br>
$ eval $(gp env -e)<br>
`
Careful w/environment variables. If you share your environment, your buddies may have access to these details. 